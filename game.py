import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Runner Pablo')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/unlearne.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
text_surface = test_font.render('Tiny Runner Pablo', False, 'Black')

snail_surface = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load(
    'graphics/player/player_walk1.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 280))
    screen.blit(text_surface, (200, 50))
    screen

    snail_x_pos -= 4
    if snail_x_pos < -35:
        snail_x_pos = 835

    screen.blit(snail_surface, (snail_x_pos, 240))
    screen.blilt(player_surf, (80, 240))

    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)  # limits the while loop to 60 loops a second
