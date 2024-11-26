# Example file showing a basic pygame "game loop"
import pygame
from background import build_background
from player import Player
from enemy import Enemy
import random
   
# pygame setup
pygame.init()

#border of the screen
WIDTH = 800
HEIGHT = 512

# 50 pixels tall, 32 pixels wide

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#get background
background, wall_rect = build_background(WIDTH, HEIGHT)

#make a group
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprite_group = pygame.sprite.Group()

#make a chacrter
player_1 = Player(screen, 400, 256, WIDTH, HEIGHT, wall_rect)
enemy = Enemy(player_1, screen, random.randint(0, WIDTH), random.randint(0, HEIGHT), WIDTH, HEIGHT, wall_rect, 'wizard')


#add player to group
player_group.add(player_1)
enemy_group.add(enemy)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # RENDER YOUR GAME HERE

    #update character
    player_1.check_keys()
    player_group.update()
    enemy_group.update()

    enemy.track_player(target_x = player_1.x, target_y= player_1.y)

    #blit the background to the screen
    screen.blit(background, (0,0))

  
       



    #draw character
    player_group.draw(screen)
    enemy_group.draw(screen)

    if pygame.sprite.collide_rect(player_1, enemy):
        player_1.kill()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()