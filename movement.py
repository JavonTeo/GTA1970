# GAME REFRESH RATE IS 6 FRAME

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1500, 900))
clock = pygame.time.Clock()
pygame.display.set_caption("GTA 1970")
left = False
right = False
idling = True
sliding = False
crouch = False
characterX = 300
characterY = 300
characterX_change = 0
characterY_change = 0
walk_count = 0
idle_count = 0
slide_count = 0
crouch_count = 0
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


right_slide = [pygame.image.load('Individual Sprites/adventurer-slide-00.png'),
               pygame.image.load('Individual Sprites/adventurer-slide-01.png')]
left_slide = []
for item in right_slide:
    left_slide.append(pygame.transform.flip(item, True, False))


def slide_right(x, y):
    screen.blit(right_slide[slide_count // 6], (x, y))


def slide_left(x, y):
    screen.blit(left_slide[slide_count // 6], (x, y))


crouching = [pygame.image.load('./Individual Sprites/adventurer-crouch-00.png'),
             pygame.image.load('./Individual Sprites/adventurer-crouch-01.png'),
             pygame.image.load('./Individual Sprites/adventurer-crouch-02.png'),
             pygame.image.load('./Individual Sprites/adventurer-crouch-03.png')]


def crouch_movement(x, y):
    screen.blit(crouching[crouch_count // 6], (x, y))



