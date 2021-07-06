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
movement.jump = False


# enemy
enemy = pygame.image.load('bomb.png')
enemyX = 700
enemyY = ground_value
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
                if movement.sliding or movement.fall:
                    movement.right = False
                    movement.left = False
                    movement.idling = False

                else:
                    movement.right = True
                    movement.left = False
                    movement.idling = False


            elif event.key == pygame.K_LEFT:
                characterX_change = -3
                if movement.sliding or movement.fall:
                    movement.right = False
                    movement.left = False
                    movement.idling = False
                else:
                    movement.right = False
                    movement.left = True
                    movement.idling = False

            elif movement.movement_counter == 0:
                movement.right = False
                movement.left = False
                movement.idling = True
                movement.fall = False

            if event.key == pygame.K_DOWN:
                if not movement.jump:
                    movement.sliding = True
                    movement.right = False
                    movement.left = False
                    movement.idling = False

            if event.key == pygame.K_UP:
                if not movement.sliding:
                    if not movement.jump:       # if not jumping  aka jump = False
                        movement.jump = True
                        movement.idling = False
                        characterY_change = -1
                        movement.fall = False
                        movement.right = False

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

            if event.key == pygame.K_UP:
                movement.jump = False
                movement.fall = True
                if not movement.jump:
                    characterY_change = 2

            if event.key == pygame.K_DOWN:
                movement.sliding = False
                movement.crouch = False
                movement.idling = True

                if movement.movement_counter >= 1:
                    if characterX_change > 0 and not movement.sliding:
                        movement.right = True
                        characterX_change = 3
                    elif characterX_change < 0 and not movement.sliding:
                        movement.left = True
                        characterX_change = -3

    # floor limit
    if characterY >= ground_value:
        characterY = ground_value
        movement.fall = False
        if not movement.fall and not movement.jump:
            characterY_change = 0



    # jump animation
    # jump ceiling, force jump release
    if characterY <= 669:
        movement.jump = False
        movement.fall = True
    # looping thru animation
    if movement.jump_count + 1 >= 40:
        movement.jump_count = 0
    movement.jump_count += 1
    if movement.fall_count + 1 >= 12:
        movement.fall_count = 0
    movement.fall_count += 1
    # actual jump
    if movement.jump:
        if movement.sliding:
            pass
        else:
            if characterX_change >= 0:
                movement.jump_right(characterX, characterY)
            elif characterX_change < 0:
                movement.jump_left(characterX, characterY)
            movement.right = False
            movement.left = False
    elif movement.fall:
        characterY_change = 2
    print(movement.idling)
    #TODO
    # CHARACTER DISAPPEAR AFTER LANDING

    if movement.movement_counter >= 1 and not movement.sliding:
        if characterX_change > 0:
            movement.right = True
        elif characterX_change < 0:
            movement.left = True

    if movement.fall:
        if characterX_change >= 0:
            movement.fall_right(characterX, characterY)
        elif characterX_change < 0:
            movement.fall_left(characterX, characterY)
        movement.right = False
        movement.left = False


    # Left right animation
    if movement.walk_count + 1 >= 36:
        movement.walk_count = 0
    movement.walk_count += 1
    if movement.right:
        if movement.jump:
            pass
        else:
            movement.right_run(characterX, characterY)
            movement.idling = False
    if movement.left:
        if movement.jump:
            pass
        else:
            movement.left_run(characterX, characterY)
            movement.idling = False



    # idle animation
    if movement.idle_count + 1 >= 24:
        movement.idle_count = 0
    if movement.movement_counter == 0:
        if movement.fall:
            pass
        else:
            movement.idle_movement(characterX, characterY)
    movement.idle_count += 1
    # slide animation
    if movement.slide_count + 1 >= 12:
        movement.slide_count = 0
    movement.slide_count += 1
    if movement.sliding:
        #sliding right
        if characterX_change > 0:
            movement.right = False
            movement.slide_right(characterX, characterY)
            characterX_change = 2
        #sliding left
        elif characterX_change < 0:
            movement.left = False
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
