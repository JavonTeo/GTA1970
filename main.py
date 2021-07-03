import pygame
from pygame.constants import KEYDOWN

pygame.init()

screen = pygame.display.set_mode((1500, 900))
floor = pygame.image.load('desertground.jpg')
game_floor = pygame.transform.scale(floor, (1500, 150))

ground_value = 717

#character
R_character = pygame.image.load('bomb.png')
L_character = pygame.transform.flip(R_character, True, False)
characterX = 10
characterY = ground_value
characterX_change = 0
characterY_change = 0

#enemy
enemy = pygame.image.load('foot-clan.png')
enemyX = 700
enemyY = ground_value

running = True
Kspace_released = False
wentforkill = False
character = R_character
jump = False
while running:
    dist = abs(enemyX - characterX)
    screen.fill((31,187,255))
    screen.blit(game_floor, (0, 750))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character = L_character
                characterX_change = -1
            if event.key == pygame.K_RIGHT:
                character = R_character
                characterX_change = 1
            if event.key == pygame.K_SPACE:
                if jump == False:
                    jump = True
                    if character == R_character:
                        characterX_change = 1.25
                        characterY_change = -3
                    elif character == L_character:
                        characterX_change = -1.25
                        characterY_change = -3
            if event.key == pygame.K_q:
                #jump to enemy
                if characterX < enemyX:
                    characterX_change = 2
                elif characterX > enemyX:
                    characterX_change = -2
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character = L_character
                characterX_change = 0
            if event.key == pygame.K_RIGHT:
                character = R_character
                characterX_change = 0
            if event.key == pygame.K_SPACE:
                Kspace_released = True
                jump = False
                if character == R_character:
                    characterX_change = 1.25
                    characterY_change = 3
                elif character == L_character:
                    characterX_change = -1.25
                    characterY_change = 3
            if event.key == pygame.K_q:
                if characterX < enemyX:
                    characterX_change = 2
                    wentforkill = True
                elif characterX > enemyX:
                    characterX_change = -2
                    wentforkill = True
                
    characterX += characterX_change
    characterY += characterY_change

    if Kspace_released and characterY >= ground_value:
        characterX_change = 0
        Kspace_released = False

    if wentforkill == True:
        if dist <= 5:
            characterX_change = 0
            wentforkill = False

    if characterY >= ground_value:
        characterY = ground_value
    
    screen.blit(enemy, (enemyX, enemyY))     
    screen.blit(character, (characterX, characterY))
    pygame.display.update()