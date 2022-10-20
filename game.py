import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(midtop=(400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Runner Pablo')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/unlearne.ttf', 50)
game_active = True
start_time = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/Ground.png').convert()

# score_surf = test_font.render('Tiny Runner Pablo', False, (64, 64, 64))
# score_rect = score_surf.get_rect(midtop=(400, 50))

enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(bottomleft=(600, 310))

player_surf = pygame.image.load(
    'graphics/player/player_walk1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(80, 310))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 310:
                    player_gravity = -20
                    print('jump')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 310:
                    player_gravity = -20
                    print('jump')
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rect.left = 600
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 280))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        display_score()

        enemy_rect.left -= 4
        if enemy_rect.left < -35:
            enemy_rect.left = 835

        screen.blit(enemy_surf, enemy_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 310:
            player_rect.bottom = 310
        screen.blit(player_surf, player_rect)

        # Collision
        if enemy_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill('Yellow')

    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)  # limits the while loop to 60 loops a second
