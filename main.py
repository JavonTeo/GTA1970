import pygame
import math
import movement


pygame.init()
#game constants
screen = pygame.display.set_mode((1500, 900))
movement.screen = screen
clock = pygame.time.Clock()
floor = pygame.image.load('desertground.jpg')
pygame.display.set_caption("GTA 1970")
game_floor = pygame.transform.scale(floor, (1500, 150))
ground_value = 717
attack_animation = [0,1,2]
temp_added = False
moving = False

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
            # prevents attack animation during movement
            if not movement.attack:
                # if not movement.attack:
                if event.key == pygame.K_RIGHT:
                    characterX_change = 3
                    movement.face_right = True
                    movement.face_left = False
                    if movement.sliding or movement.fall:
                        movement.right = False
                        movement.left = False
                        movement.idling = False

                    else:
                        movement.right = True
                        movement.left = False
                        movement.idling = False
                        moving = True

                elif event.key == pygame.K_LEFT:
                    characterX_change = -3
                    movement.face_left = True
                    movement.face_right = False
                    if movement.sliding or movement.fall:
                        movement.right = False
                        movement.left = False
                        movement.idling = False
                    else:
                        movement.right = False
                        movement.left = True
                        movement.idling = False
                        moving = True

                elif movement.movement_counter == 0:
                    movement.right = False
                    movement.left = False
                    movement.idling = True
                    movement.fall = False

                if event.key == pygame.K_DOWN:
                    if not movement.jump:
                        moving = True
                        movement.sliding = True
                        movement.right = False
                        movement.left = False
                        movement.idling = False

                if event.key == pygame.K_UP:
                    if not movement.sliding:
                        if not movement.jump:       # if not jumping  aka jump = False
                            movement.jump = True
                            moving = True
                            movement.idling = False
                            characterY_change = -1
                            movement.fall = False
                            movement.right = False

            if event.key == pygame.K_SPACE:
                if not moving:
                    if movement.movement_counter == 1:
                        #if movement.attack_counter + 1 == 4:
                            #movement.attack_counter = 0
                        movement.attack_counter = 1
                        if not movement.jump and not movement.attack:
                            movement.attack = True
                            moving = False
                            movement.idling = True
                            movement.fall = False
                            movement.right = False
                            movement.left = False

        # release
        elif event.type == pygame.KEYUP:
            movement.movement_counter -= 1

            if event.key == pygame.K_RIGHT:
                characterX_change = 0
                movement.right = False
                moving = False
                if movement.movement_counter == 0 or not moving:
                    movement.idling = True
                movement.attack_action_complete = False

            if event.key == pygame.K_LEFT:
                characterX_change = 0
                movement.left = False
                moving = False
                if movement.movement_counter == 0 or not moving:
                    movement.idling = True
                movement.attack_action_complete = False

            if event.key == pygame.K_UP:
                movement.jump = False
                movement.fall = True
                moving = False
                if not movement.jump:
                    characterY_change = 2
                movement.attack_action_complete = False

            if event.key == pygame.K_DOWN:
                movement.sliding = False
                movement.crouch = False
                movement.idling = True
                moving = False
                movement.attack_action_complete = False
                if movement.movement_counter >= 1:
                    if characterX_change > 0 and not movement.sliding:
                        movement.right = True
                        characterX_change = 3
                    elif characterX_change < 0 and not movement.sliding:
                        movement.left = True
                        characterX_change = -3

            if event.key == pygame.K_SPACE:
                if movement.movement_counter == 1:
                    if movement.attack_action_complete:
                        movement.attack = False
                        movement.attack_action_complete = False
                    if not movement.attack and not movement.jump:
                        movement.idling = True
    print(moving)
    # floor limit
    if characterY >= ground_value:
        characterY = ground_value
        movement.fall = False
        if not movement.fall and not movement.jump:
            characterY_change = 0


    # jump ceiling, force jump release
    if characterY <= 669:
        movement.jump = False
        movement.fall = True
        if characterX_change == 0:
            movement.movement_counter -= 1


    # attack animation

    # attack move
    if movement.attack and characterX_change == 0:
        if movement.attack_counter == 1:
            if movement.attack_action_complete is False:
                movement.attack_action_complete = False
                movement.attack_count_1 += 1
                if movement.attack_count_1 + 1 >= 30:
                    movement.attack_count_1 = 0
                    movement.attack_action_complete = True
                    movement.attack = False
                if movement.face_right:
                    movement.attack_right_1(characterX, characterY)
                elif movement.face_left:
                    movement.attack_left_1(characterX, characterY)
    if movement.attack:
        if not temp_added:
            movement.movement_counter += 1
            temp_added = True
    else:
        if temp_added:
            movement.movement_counter -= 1
            temp_added = False


    if movement.attack_action_complete:
        movement.idling = True

    #prevent moving while animation going on
    if movement.attack_count_1  > 0 or movement.attack_count_2  > 0 or movement.attack_count_3 > 0:
        movement.right = False
        movement.left = False
        movement.idling = False
    movement.attack_action_complete = False

    # jump animation


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
            if characterX_change > 0:
                movement.jump_right(characterX, characterY)
            elif characterX_change < 0:
                movement.jump_left(characterX, characterY)
            elif characterX_change == 0:
                if movement.face_left:
                    movement.jump_left(characterX, characterY)
                elif movement.face_right:
                    movement.jump_right(characterX, characterY)
            movement.right = False
            movement.left = False
    elif movement.fall:
        characterY_change = 2
    #TODO
    # CHARACTER DISAPPEAR AFTER LANDING

    if movement.movement_counter >= 1 and not movement.sliding:
        if characterX_change > 0:
            movement.right = True
        elif characterX_change < 0:
            movement.left = True

    if movement.fall:
        if characterX_change > 0:
            movement.fall_right(characterX, characterY)
        elif characterX_change < 0:
            movement.fall_left(characterX, characterY)
        elif characterX_change == 0:
            if movement.face_left:
                movement.fall_left(characterX, characterY)
            elif movement.face_right:
                movement.fall_right(characterX, characterY)
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
    if movement.movement_counter == 0 or movement.idling:
        if movement.fall:
            pass
        else:
            if movement.face_right:
                movement.idle_movement(characterX, characterY)
            elif movement.face_left:
                movement.idle_movement_left(characterX, characterY)
    movement.idle_count += 1
    if movement.movement_counter == -1:
        if movement.face_right:
            movement.idle_movement(characterX, characterY)
        elif movement.face_left:
            movement.idle_movement_left(characterX, characterY)
        movement.movement_counter += 1


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


    #offset the falling animation


    #display enemy
    screen.blit(enemy, (enemyX, enemyY))
    pygame.display.update()
