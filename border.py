import pygame


pygame.init()
screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("GTA 1970")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if characterX <= 0:
        characterX = 0
    elif characterX >= 1440:
        characterX = 1440
