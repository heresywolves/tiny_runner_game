from cgitb import small
import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 100) - start_time
    score_surf = small_font.render(f'{current_time} ft', False, ('#C4C4BF'))
    score_rect = score_surf.get_rect(midtop=(80, 360))
    screen.blit(score_surf, score_rect)
    return current_time

def display_butterfly_caught(count):
    butterfly_score_surf = small_font.render(f'{count}', False, ('#C4C4BF'))
    screen.blit(butterfly_icon_surf, butterfly_icon_rect)
    screen.blit(butterfly_score_surf, butterfly_score_rect)
    return

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 310:
                screen.blit(enemy_surf, obstacle_rect)
            else:
                screen.blit(enemy2_surf, obstacle_rect)
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def butterfly_movement(butterfly_list):
    global butterflies_caught
    if butterfly_list:
        for butterfly_rect in butterfly_list:
            butterfly_rect.x -= 5
            screen.blit(butterfly_surf, butterfly_rect)
            if butterfly_collisions(player_rect, butterfly_list):
                butterfly_list.remove(butterfly_rect)
                butterflies_caught += 1
        butterfly_list = [butterfly for butterfly in butterfly_list if butterfly.x > -100]
            
        return butterfly_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
    
def butterfly_collisions(player, butterflies):
    if butterflies:
        for butterfly_rect in butterflies:
            if player.colliderect(butterfly_rect):
                return 1
    else: return 0
    
        
def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tiny Butterfly Catcher')
clock = pygame.time.Clock()

# Fonts
test_font = pygame.font.Font('font/Undertale-Font.ttf', 35)
small_font = pygame.font.Font('font/Undertale-Font.ttf', 20)

game_active = False
start_time = 0
score = 0
butterflies_caught = 0
health = 3

sky_surf = pygame.image.load('graphics/Sky.png').convert()
sky_rect = sky_surf.get_rect(topleft=(0,0))
sky2_surf = pygame.image.load('graphics/Sky2.png').convert()
sky2_rect = sky2_surf.get_rect(topleft=(800,0))
ground_surf = pygame.image.load('graphics/Ground.png').convert()

# Butterflies
butterfly_surf = pygame.image.load('graphics/butterfly/butterfly1.png')
butterfly_rect_list = []
butterfly_icon_surf = pygame.image.load('graphics/butterfly/butterfly_icon.png')
butterfly_icon_rect = butterfly_icon_surf.get_rect(midtop=(715, 365))

# Butterfly scoring
butterfly_score_surf = small_font.render(f'{butterflies_caught}', False, ('#C4C4BF'))
butterfly_score_rect = butterfly_score_surf.get_rect(midtop=(750, 360))

# Health
health_1 = pygame.image.load('graphics/health/1health.png').convert_alpha()
health_2 = pygame.image.load('graphics/health/2health.png').convert_alpha()
health_3 = pygame.image.load('graphics/health/3health.png').convert_alpha()
health_rect = health_3.get_rect(midtop=(400, 363))

# Obstacles
enemy_surf = pygame.image.load('graphics/enemy/enemy1.png').convert_alpha()
enemy2_surf = pygame.image.load('graphics/enemy/enemy2.png').convert_alpha()
obstacle_rect_list = []

player_walk_1 = pygame.image.load('graphics/player/player_walk1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/player/player_walk2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/player/player_jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(bottomleft=(80, 310))
player_gravity = 0

# Intro screen
player_sit_surf = pygame.image.load('graphics/player/player_sit.png').convert_alpha()
player_sit_rect = player_sit_surf.get_rect(center=(400, 200))

instructions_surf = small_font.render('Press SPACE to start the game', False, ('#C4C4BF'))
instructions_rect = instructions_surf.get_rect(center=(400, 345))

title_surf = test_font.render('Tiny Butterfly Catcher', False, ('#C4C4BF'))
title_rect = title_surf.get_rect(center=(400, 50))

# Timer
obstacle_timer = pygame.USEREVENT + 1
butterfly_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1700)
pygame.time.set_timer(butterfly_timer, 1700)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 310:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 310:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 100)
                butterflies_caught = 0

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(enemy_surf.get_rect(bottomleft=(randint(900, 1100), 310)))
            else:
                obstacle_rect_list.append(enemy2_surf.get_rect(bottomleft=(randint(900, 1100), 130)))

        if event.type == butterfly_timer and game_active:
            butterfly_rect_list.append(butterfly_surf.get_rect(bottomleft=(randint(900, 1300), randint(50, 250))))
            

    if game_active:
        # BG movement
        screen.blit(sky_surf, sky_rect)
        sky_rect.x -= 3
        screen.blit(sky2_surf, sky2_rect)
        sky2_rect.x -= 3
        if sky_rect.x <= -800:
            sky_rect.x = 800
        if sky2_rect.x <= -800:
            sky2_rect.x = 800
        
        # Ground
        screen.blit(ground_surf, (0, 280))

        # Score
        score = display_score()
        display_butterfly_caught(butterflies_caught)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 310: player_rect.bottom = 310
        player_animation()
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        butterfly_rect_list = butterfly_movement(butterfly_rect_list)

        # Enemy Collision
        game_active = collisions(player_rect, obstacle_rect_list)

        # Health
        if health == 3:
            screen.blit(health_3, health_rect)
            

    else:
        screen.fill('#1F211F')
        screen.blit(player_sit_surf, player_sit_rect)
        obstacle_rect_list.clear()
        player_rect.bottomleft = (80, 310)
        player_gravity = 0

        score_message = small_font.render(
            f'Distance: {score} ft             Butterflies Caught: {butterflies_caught}', False, ('#C4C4BF'))
        score_message_rect = score_message.get_rect(center=(400, 60))
        screen.blit(instructions_surf, instructions_rect)

        if score == 0:
            screen.blit(title_surf, title_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # draw all elements
    # update everything
    pygame.display.update()
    clock.tick(60)  # limits the while loop to 60 loops a second
