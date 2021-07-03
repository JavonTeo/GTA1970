import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1200,900))

pygame.display.set_caption("GTA 1970")
# background = pygame.image.load("background.jpg")

# projectile
bomb_icon = pygame.image.load('bomb.png')
bombX = 3
bombY = 800
bombX_change = 0.2
#bombY_change = 0.5 *  math.pow(bombX, 2)

def bomb(x,y):
    screen.blit(bomb_icon, (x,y))

running = True
while running:
    # screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    playerY = 600
    bombX += bombX_change
    bombY = (0.005 * math.pow(bombX-200, 2)) + playerY
    bomb(bombX, bombY)
    pygame.display.update()