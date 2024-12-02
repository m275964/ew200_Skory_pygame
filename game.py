# Example file showing a basic pygame "game loop"
import pygame


from background import build_background
from player import Player
from enemy import Enemy
import random
from Title import display_title_screen

from arrow import Arrow


# pygame setup
pygame.init()
pygame.mixer.init()

#audio 
music = pygame.mixer.Sound('audio/echoofsadness.mp3')
music.set_volume(0.5)
music.play(-1)

#border of the screen
WIDTH = 800
HEIGHT = 512

# 50 pixels tall, 32 pixels wide

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#get background
background, wall_rect = build_background(WIDTH, HEIGHT)


display_title_screen(screen, WIDTH, HEIGHT)

# Now start the actual game loop

#make a group
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprite_group = pygame.sprite.Group()

#make a chacrter
player_1 = Player(screen, 400, 256, WIDTH, HEIGHT, wall_rect)
enemy = Enemy(player_1, screen, random.randint(0, WIDTH), random.randint(0, HEIGHT), WIDTH, HEIGHT, wall_rect, 'wizard')
enemy_2 = Enemy(player_1, screen, random.randint(0, WIDTH), random.randint(0, HEIGHT), WIDTH, HEIGHT, wall_rect, 'wizard')
enemy_3 = Enemy(player_1, screen, random.randint(0, WIDTH), random.randint(0, HEIGHT), WIDTH, HEIGHT, wall_rect, 'wizard')


#add player to group
player_group.add(player_1)
enemy_group.add(enemy)
enemy_group.add(enemy_2)

#Text for Scoress
Score = 0000
start_time = pygame.time.get_ticks()
font = pygame.font.SysFont('Verdana', 20, bold = True)
Score_text = font.render(f"Score: {Score}", True, (0, 0, 0)) 

#status of player
player_alive = True

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
    enemy_2.track_player(target_x = player_1.x, target_y= player_1.y)

    #blit the background to the screen
    screen.blit(background, (0,0))


    current_time = pygame.time.get_ticks()
    if player_alive:
        if (current_time - start_time) >= 100:  # 1000 milliseconds = 1 second
            Score += 1
            start_time = current_time
        Score_text = font.render(f"Score: {Score}", True, (0, 0, 0))
        screen.blit(Score_text, (0, 0))
  
    player_1.update()
    for arrow in player_1.arrow_group:
        arrow.check_collision(enemy_group)

    player_1.arrow_group.draw(screen)
    #draw character
    player_group.draw(screen)

    enemy_group.draw(screen)

    if pygame.sprite.collide_rect(player_1, enemy) or pygame.sprite.collide_rect(player_1, enemy_2):
        player_alive = False
        player_1.kill()
        Score_text = font.render(f"YOU HAVE DIED, YOUR FINAL SCORE: {Score}", True, (0, 0, 0))
        screen.blit(Score_text, (WIDTH // 2 - Score_text.get_width() // 2, HEIGHT // 3))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()