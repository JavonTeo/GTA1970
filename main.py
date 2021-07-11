import pygame
import math
import movement

pygame.init()
# game constants
screen = pygame.display.set_mode((1500, 900))  # display resolution
movement.screen = screen
clock = pygame.time.Clock()
floor = pygame.image.load('desertground.jpg')
pygame.display.set_caption("GTA 1970")
game_floor = pygame.transform.scale(floor, (1500, 150))
ground_value = 717
temp_added = False  # temp bool value for smooth attack animation
moving = False

# character
characterX = 10  # base character X value
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
            if not movement.attack:  # prevents attack animation during movement
                if event.key == pygame.K_RIGHT:
                    characterX_change = 3
                    movement.face_right = True
                    movement.face_left = False
                    if movement.sliding or movement.fall:  # prevent running animation when falling or sliding
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
                    if movement.sliding or movement.fall:  # prevent running animation when falling or sliding
                        movement.right = False
                        movement.left = False
                        movement.idling = False
                    else:
                        movement.right = False
                        movement.left = True
                        movement.idling = False
                        moving = True

                elif movement.movement_counter == 0:  # if not moving , then default is idling
                    movement.right = False
                    movement.left = False
                    movement.idling = True
                    movement.fall = False

                if event.key == pygame.K_DOWN:
                    if not movement.jump and not movement.fall:  # prevent sliding animation when jumping and falling
                        moving = True
                        movement.sliding = True
                        movement.right = False
                        movement.left = False
                        movement.idling = False

                if event.key == pygame.K_UP:
                    if not movement.sliding:
                        if not movement.jump and not movement.jump_state:  # if not jumping  aka jump = False
                            movement.jump = True
                            moving = True
                            movement.idling = False
                            characterY_change = -5
                            movement.fall = False
                            movement.right = False

            if event.key == pygame.K_SPACE:
                if not moving:
                    if movement.movement_counter == 1:  # loops thru attack type
                        if movement.attack_counter + 1 == 4:
                            movement.attack_counter = 0
                        movement.attack_counter += 1
                        if not movement.jump and not movement.attack:  # actual attack conditions
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
        if movement.attack_action_complete is False:  # if attack haven't start
            if movement.attack_counter == 1:
                movement.attack_count_1 += 1
                if movement.attack_count_1 + 1 >= 30:  # loops thru attack frames
                    movement.attack_count_1 = 0
                    movement.attack_action_complete = True
                    movement.attack = False  # resets attack counter to enable attack again
                if movement.face_right:
                    movement.attack_right_1(characterX, characterY)
                elif movement.face_left:
                    movement.attack_left_1(characterX, characterY)

            elif movement.attack_counter == 2:
                movement.attack_count_2 += 1
                if movement.attack_count_2 + 1 >= 36:
                    movement.attack_count_2 = 0
                    movement.attack_action_complete = True
                    movement.attack = False
                if movement.face_right:
                    movement.attack_right_2(characterX, characterY)
                elif movement.face_left:
                    movement.attack_left_2(characterX, characterY)

            elif movement.attack_counter == 3:
                movement.attack_count_3 += 1
                if movement.attack_count_3 + 1 >= 36:
                    movement.attack_count_3 = 0
                    movement.attack_action_complete = True
                    movement.attack = False
                if movement.face_right:
                    movement.attack_right_3(characterX, characterY)
                elif movement.face_left:
                    movement.attack_left_3(characterX, characterY)

    if movement.attack:  # smoothes out attack animation
        if not temp_added:
            movement.movement_counter += 1
            temp_added = True
    else:
        if temp_added:
            movement.movement_counter -= 1
            temp_added = False

    if movement.attack_action_complete:  # default idle after attack completion
        movement.idling = True
    if moving:
        movement.attack_counter = 0

    if movement.attack_count_1 > 0 or movement.attack_count_2 > 0 or movement.attack_count_3 > 0:  # prevent moving while attack animation going on
        movement.right = False
        movement.left = False
        movement.idling = False
    movement.attack_action_complete = False

    # jump animation
    if characterY_change > 0:                      # prevent double jumping
        movement.jump_state = True
    elif characterY_change == 0:
        movement.jump_state = False

    if movement.jump_count + 1 >= 40:              # looping thru animation
        movement.jump_count = 0
    movement.jump_count += 1
    if movement.fall_count + 1 >= 12:
        movement.fall_count = 0
    movement.fall_count += 1

    if movement.jump:                                # actual jump
        if movement.sliding:
            pass
        elif movement:
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

    if movement.movement_counter >= 1 and not movement.sliding:         # smooth transit from falling to running
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
    if movement.walk_count + 1 >= 36:               # loop thru walking animation
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
    if movement.idle_count + 1 >= 24:           # loop thru idle animation
        movement.idle_count = 0
    movement.idle_count += 1
    if movement.movement_counter == 0 or movement.idling:
        if movement.fall:
            pass
        else:
            if movement.face_right:
                movement.idle_movement(characterX, characterY)
            elif movement.face_left:
                movement.idle_movement_left(characterX, characterY)
    if movement.movement_counter == -1:         # prevents character disappear after landing
        if movement.face_right:
            movement.idle_movement(characterX, characterY)
        elif movement.face_left:
            movement.idle_movement_left(characterX, characterY)
        movement.movement_counter += 1

    # slide animation
    if movement.slide_count + 1 >= 12:         # loop thru sliding animation
        movement.slide_count = 0
    movement.slide_count += 1

    if movement.sliding:
        if characterX_change > 0:  # slide right
            movement.right = False
            movement.slide_right(characterX, characterY)
            characterX_change = 2
        elif characterX_change < 0:  # slide left
            movement.left = False
            movement.slide_left(characterX, characterY)
            characterX_change = -2
        else:
            movement.crouch = True  # no sliding, default is crouch
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

    # display enemy
    screen.blit(enemy, (enemyX, enemyY))
    pygame.display.update()
