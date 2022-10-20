import pygame
from sys import exit

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Runner Pablo')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/unlearne.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/Ground.png').convert()

score_surf = test_font.render('Tiny Runner Pablo', False, 'Black')
score_rect = score_surf.get_rect(midtop=(400, 50))

enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(bottomleft=(600, 310))

player_surf = pygame.image.load(
    'graphics/player/player_walk1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(80, 310))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 280))
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)
    screen.blit(score_surf, score_rect)

    enemy_rect.left -= 4
    if enemy_rect.left < -35:
        enemy_rect.left = 835

    screen.blit(enemy_surf, enemy_rect)
    screen.blit(player_surf, player_rect)

    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)  # limits the while loop to 60 loops a second
