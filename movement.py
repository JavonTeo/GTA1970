# GAME REFRESH RATE IS 6 FRAME

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1500, 900))  # set display resolution
clock = pygame.time.Clock()
pygame.display.set_caption("GTA 1970")
left = False  # basic movement var
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
jump = False
jump_count = 0
jump_state = False
fall = False
fall_count = 0
attack = False
attack_number = 0
attack_action_complete = False
attack_counter = 0
attack_count_1 = 0
attack_count_2 = 0
attack_count_3 = 0
face_right = True
face_left = False
# skill variables. ALL SKILLS TO BE ADDED FROM HERE
skill_activated = False  # GLOBAL VARIABLE FOR ALL SKILLS WHEN ACTIVATED TO PREVENT MOVEMENT
dash = False  # dash skill
charge = False
charge_counter = 0
dash_moved = 0
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


idle_left = []
for image in idle:
    idle_left.append(pygame.transform.flip(image, True, False))


def idle_movement_left(x, y):
    screen.blit(idle_left[idle_count // 6], (x, y))


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


jumping_right = [pygame.image.load('./Individual Sprites/adventurer-jump-00.png'),
                 pygame.image.load('./Individual Sprites/adventurer-jump-01.png'),
                 pygame.image.load('./Individual Sprites/adventurer-jump-02.png'),
                 pygame.image.load('./Individual Sprites/adventurer-jump-03.png')]


def jump_right(x, y):
    screen.blit(jumping_right[jump_count // 10], (x, y))


jumping_left = []
for item in jumping_right:
    jumping_left.append(pygame.transform.flip(item, True, False))


def jump_left(x, y):
    screen.blit(jumping_left[jump_count // 10], (x, y))


falling_right = [pygame.image.load('./Individual Sprites/adventurer-fall-00.png', ),
                 pygame.image.load('./Individual Sprites/adventurer-fall-01.png', )]


def fall_right(x, y):
    screen.blit(falling_right[fall_count // 6], (x, y))


falling_left = []
for item in falling_right:
    falling_left.append(pygame.transform.flip(item, True, False))


def fall_left(x, y):
    screen.blit(falling_left[fall_count // 6], (x, y))


attacking_right_1 = [pygame.image.load('./Individual Sprites/adventurer-attack1-00.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack1-01.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack1-02.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack1-03.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack1-04.png')]


def attack_right_1(x, y):
    screen.blit(attacking_right_1[attack_count_1 // 6], (x, y))


attacking_left_1 = []
for item in attacking_right_1:
    attacking_left_1.append(pygame.transform.flip(item, True, False))


def attack_left_1(x, y):
    screen.blit(attacking_left_1[attack_count_1 // 6], (x, y))


attacking_right_2 = [pygame.image.load('./Individual Sprites/adventurer-attack2-00.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack2-01.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack2-02.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack2-03.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack2-04.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack2-05.png')]


def attack_right_2(x, y):
    screen.blit(attacking_right_2[attack_count_2 // 6], (x, y))


attacking_left_2 = []
for item in attacking_right_2:
    attacking_left_2.append(pygame.transform.flip(item, True, False))


def attack_left_2(x, y):
    screen.blit(attacking_left_2[attack_count_2 // 6], (x, y))


attacking_right_3 = [pygame.image.load('./Individual Sprites/adventurer-attack3-00.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack3-01.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack3-02.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack3-03.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack3-04.png'),
                     pygame.image.load('./Individual Sprites/adventurer-attack3-05.png')]


def attack_right_3(x, y):
    screen.blit(attacking_right_3[attack_count_3 // 6], (x, y))


attacking_left_3 = []
for item in attacking_right_3:
    attacking_left_3.append(pygame.transform.flip(item, True, False))


def attack_left_3(x, y):
    screen.blit(attacking_left_3[attack_count_3 // 6], (x, y))


def skill_dash_right(x, y):
    screen.blit(pygame.image.load('./Individual Sprites/adventurer-attack3-02.png'), (x, y))


def skill_dash_left(x, y):
    screen.blit(pygame.transform.flip(pygame.image.load('./Individual Sprites/adventurer-attack3-02.png'), True, False),
                (x, y))


def skill_dash_charge_right(x, y):
    screen.blit(pygame.image.load('./Individual Sprites/adventurer-attack3-05.png'), (x, y))


def skill_dash_charge_left(x, y):
    screen.blit(pygame.transform.flip(pygame.image.load('./Individual Sprites/adventurer-attack3-05.png'), True, False),
                (x, y))
