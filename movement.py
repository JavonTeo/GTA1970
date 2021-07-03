# GAME REFRESH RATE IS 6 FRAME

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("GTA 1970")
background = pygame.image.load("background.jpg")
left = False
right = False
idling = True
sliding = False
characterX = 300
characterY = 300
characterX_change = 0
walk_count = 0
idle_count = 0
slide_count = 0
movement_counter = 0
running = True

# character model
run_right = [pygame.image.load("./Individual Sprites/adventurer-run-00.png"),
             pygame.image.load("./Individual Sprites/adventurer-run-01.png"),
             pygame.image.load("./Individual Sprites/adventurer-run-02.png"),
             pygame.image.load("./Individual Sprites/adventurer-run-03.png"),
             pygame.image.load("./Individual Sprites/adventurer-run-04.png"),
             pygame.image.load("./Individual Sprites/adventurer-run-05.png")]


def right_run(x, y):
    screen.blit(run_right[walk_count // 6], (x, y))


run_left = []
for image in run_right:
    run_left.append(pygame.transform.flip(image, True, False))


def left_run(x, y):
    screen.blit(run_left[walk_count // 6], (x, y))


idle = [pygame.image.load('./Individual Sprites/adventurer-idle-00.png'),
        pygame.image.load('./Individual Sprites/adventurer-idle-01.png'),
        pygame.image.load('./Individual Sprites/adventurer-idle-02.png'),
        pygame.image.load('./Individual Sprites/adventurer-idle-03.png')]


def idle_movement(x, y):
    screen.blit(idle[idle_count // 6], (x, y))


right_slide = [pygame.image.load('Individual Sprites/adventurer-slide-00.png'), pygame.image.load('Individual Sprites/adventurer-slide-01.png')]
left_slide= []
for item in right_slide:
    left_slide.append(pygame.transform.flip(item, True, False))


def slide_right(x, y):
    screen.blit(right_slide[slide_count // 6], (x, y))


def slide_left(x, y):
    screen.blit(left_slide[slide_count // 6], (x, y))


while running:
    clock.tick(60)
    screen.blit(background, (0, 0))

    # movement bind
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # press down
        if event.type == pygame.KEYDOWN:
            movement_counter += 1
            if event.key == pygame.K_RIGHT:
                characterX_change = 3
                if not sliding:
                    right = True
                    left = False
                    idling = False
                else:
                    right = False
                    left = False
                    idling = False
            elif event.key == pygame.K_LEFT:
                characterX_change = -3
                if not sliding:
                    right = False
                    left = True
                    idling = False
                else:
                    right = False
                    left = False
                    idling = False
            else:
                right = False
                left = False
                idling = True
            if event.key == pygame.K_DOWN:
                sliding = True
                right = False
                left = False
                idling = False

        # release key
        elif event.type == pygame.KEYUP:
            movement_counter -= 1
            if event.key == pygame.K_RIGHT:
                characterX_change = 0
                right = False
                idling = True
            if event.key == pygame.K_LEFT:
                characterX_change = 0
                left = False
                idling = True
            if event.key == pygame.K_DOWN:
                sliding = False
                idling = True
                if movement_counter >= 1:
                    if characterX_change > 0:
                        right = True
                    else:
                        left = True
                pygame.event.clear(pygame.KEYDOWN)

    # Left right animation
    if walk_count + 1 >= 36:
        walk_count = 0
    walk_count += 1
    if right:
        right_run(characterX, characterY)
    if left:
        left_run(characterX, characterY)

    # idle animation
    if idle_count + 1 >= 24:
        idle_count = 0
    if movement_counter == 0:
        idle_movement(characterX, characterY)
    idle_count += 1

    # slide animation
    if slide_count + 1 >= 12:
        slide_count = 0
    slide_count += 1
    if sliding:
        if characterX_change > 0:
            slide_right(characterX, characterY)
        else:
            slide_left(characterX, characterY)

    characterX += characterX_change
    pygame.display.update()
