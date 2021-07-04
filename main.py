import pygame
import math
import movement


pygame.init()

screen = pygame.display.set_mode((1500, 900))
movement.screen = screen
clock = pygame.time.Clock()
floor = pygame.image.load('desertground.jpg')
pygame.display.set_caption("GTA 1970")
game_floor = pygame.transform.scale(floor, (1500, 150))
ground_value = 717

# character
characterX = 10
characterY = ground_value
characterX_change = 0
characterY_change = 0
jump_counter = 0
jump = False

# enemy
enemy = pygame.image.load('bomb.png')
enemyX = 700
enemyY = ground_value
Kspace_released = False
wentforkill = False
movement.movement_counter = 0
movement.walk_count = 0
running = True
while running:
    clock.tick(60)
    dist = abs(enemyX - characterX)
    screen.fill((31, 187, 255))
    screen.blit(game_floor, (0, 750))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # press down
        if event.type == pygame.KEYDOWN:
            movement.movement_counter += 1
            if event.key == pygame.K_RIGHT:
                characterX_change = 3
                if not movement.sliding:
                    movement.right = True
                    movement.left = False
                    movement.idling = False
                else:
                    movement.right = False
                    movement.left = False
                    movement.idling = False

            elif event.key == pygame.K_LEFT:
                characterX_change = -3
                if not movement.sliding:
                    movement.right = False
                    movement.left = True
                    movement.idling = False
                else:
                    movement.right = False
                    movement.left = False
                    movement.idling = False

            else:
                movement.right = False
                movement.left = False
                movement.idling = True

            if event.key == pygame.K_DOWN:
                movement.sliding = True
                movement.right = False
                movement.left = False
                movement.idling = False

            if event.key == pygame.K_SPACE:
                if not jump:
                    jump = True
                    movement.idling = True
                    characterY_change = -3
            if event.key == pygame.K_q:
                # jump to enemy
                if characterX < enemyX:
                    characterX_change = 2
                elif characterX > enemyX:
                    characterX_change = -2

        # release
        elif event.type == pygame.KEYUP:
            movement.movement_counter -= 1
            if event.key == pygame.K_RIGHT:
                characterX_change = 0
                movement.right = False
                movement.idling = True

            if event.key == pygame.K_LEFT:
                characterX_change = 0
                movement.left = False
                movement.idling = True

            if event.key == pygame.K_SPACE:
                Kspace_released = True
                jump = False
                characterY_change = 3

            if event.key == pygame.K_DOWN:
                movement.sliding = False
                movement.crouch = False
                movement.idling = True
                if movement.movement_counter >= 1:
                    if characterX_change > 0:
                        movement.right = True
                        characterX_change = 3
                    else:
                        movement.left = True
                        characterX_change = -3

            if event.key == pygame.K_q:
                if characterX < enemyX:
                    characterX_change = 2
                    wentforkill = True
                elif characterX > enemyX:
                    characterX_change = -2
                    wentforkill = True


    if Kspace_released and characterY >= ground_value:
        characterX_change = 0
        Kspace_released = False

    if wentforkill == True:
        if dist <= 5:
            characterX_change = 0
            wentforkill = False

    if characterY >= ground_value:
        characterY = ground_value

    if jump:
        jump_counter += 1
    elif not jump:
        if jump_counter > 0:
            jump_counter -= 1

    if jump_counter >= 100:
        characterY_change = 3
        if characterY >= ground_value:
            characterY_change = 0



    # Left right animation
    if movement.walk_count + 1 >= 36:
        movement.walk_count = 0
    movement.walk_count += 1
    if movement.right:
        movement.right_run(characterX, characterY)
        movement.idling = False
    if movement.left:
        movement.left_run(characterX, characterY)
        movement.idling = False
    # idle animation
    if movement.idle_count + 1 >= 24:
        movement.idle_count = 0
    if movement.movement_counter == 0 or movement.idling is True:
        movement.idle_movement(characterX, characterY)
    movement.idle_count += 1

    # slide animation
    if movement.slide_count + 1 >= 12:
        movement.slide_count = 0
    movement.slide_count += 1
    if movement.sliding:
        if characterX_change > 0:
            movement.slide_right(characterX, characterY)
            characterX_change = 2
        elif characterX_change < 0:
            movement.slide_left(characterX, characterY)
            characterX_change = -2
        else:
            movement.crouch = True

    if movement.crouch_count + 1 >= 24:
        movement.crouch_count = 0
    movement.crouch_count += 1
    if movement.crouch:
        movement.idling = False
        if movement.movement_counter > 1:
            movement.crouch = False
        movement.crouch_movement(characterX, characterY)
    characterX += characterX_change
    characterY += characterY_change

    screen.blit(enemy, (enemyX, enemyY))
    pygame.display.update()
