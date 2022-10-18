import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Runner Pablo')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/unlearne.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = test_font.render('Tiny Runner Pablo', False, 'Black')
snail_surface = pygame.image.load('graphics/enemy/enemy1.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 280))
    screen.blit(text_surface, (200, 50))
    screen.blit(snail_surface, (600, 240))

    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)  # limits the while loop to 60 loops a second
