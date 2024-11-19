# Example file showing a basic pygame "game loop"
import pygame
from background import build_background
from player import Player
from enemy import Enemy
import random
   
# pygame setup
pygame.init()
WIDTH = 800
HEIGHT = 512

# 50 pixels tall, 32 pixels wide

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#get background
background = build_background(WIDTH, HEIGHT)

#make a group
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

#make a chacrter
player_1 = Player(screen, 400, 256, WIDTH, HEIGHT)
enemy = Enemy(player_1, screen, random.randint(0, WIDTH), random.randint(0, HEIGHT), WIDTH, HEIGHT)


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
    player_1.update()

    #blit the background to the screen
    screen.blit(background, (0,0))

    r,g,b,_ = screen.get_at(player_1.rect.center)
    print(r, g, b)
    if (r in range(185,195)) and (g in range(195,205)) and (b in range(210, 225)):
        player_1.speed = 0
    else:
        player_1.speed =1

    #draw character
    player_group.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()