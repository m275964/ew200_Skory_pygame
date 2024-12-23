#basic imports
import pygame
import random

#background imports
from background import build_background
from Title import display_title_screen

#enities imports
from player import Player
from enemy import Enemy
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

#screen set up
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#get background
background, wall_rect = build_background(WIDTH, HEIGHT)

#Title screen
display_title_screen(screen, WIDTH, HEIGHT)

# Now start the actual game loop

#make a group
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
all_sprite_group = pygame.sprite.Group()

#make a character
player_1 = Player(screen, 400, 256, WIDTH, HEIGHT, wall_rect)
enemy = Enemy(player_1, screen, random.randint(0, 100), random.randint(0, 312), WIDTH, HEIGHT, wall_rect, 'wizard')
enemy_2 = Enemy(player_1, screen, random.randint(0, 100), random.randint(0, 312), WIDTH, HEIGHT, wall_rect, 'wizard')


#add player to group
player_group.add(player_1)
enemy_group.add(enemy)
enemy_group.add(enemy_2)

#Text for Scores
Score = 0
start_time = pygame.time.get_ticks()
enemy_spawn_time = pygame.time.get_ticks()
font = pygame.font.SysFont('Verdana', 20, bold = True)
Score_text = font.render(f"Score: {Score}", True, (0, 0, 0)) 

#status of player
player_alive = True

####################################################### Actual Game #######################################################
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #update enetities 
    if player_alive:
        player_1.check_keys(player_alive)  # Allow movement and shooting
    player_group.update(player_alive)
    enemy_group.update(player_alive)

    #tracks player
    for enemy in enemy_group:
        enemy.track_player(target_x=player_1.x, target_y=player_1.y)

    #blit the background to the screen
    screen.blit(background, (0,0))

    #Scoring system
    current_time = pygame.time.get_ticks()
    if player_alive:
        if (current_time - start_time) >= 100:  # 1000 milliseconds = 1 second
            Score += 1
            start_time = current_time
        Score_text = font.render(f"Score: {Score}", True, (0, 0, 0))
        screen.blit(Score_text, (0, 0))
  
    #Arrow abilities 
    player_1.update(player_alive)
    for arrow in player_1.arrow_group:
        score_increase = arrow.check_collision(enemy_group) #Checks if arrow hit enemy
        Score += score_increase #increases score
    player_1.arrow_group.draw(screen)


    #draw character
    player_group.draw(screen)
    enemy_group.draw(screen)

    #Death code
    for enemy in enemy_group:
        if pygame.sprite.collide_rect(player_1, enemy):
            player_alive = False
            player_1.kill() #kills player
            Score_text = font.render(f"YOU HAVE DIED, YOUR FINAL SCORE: {Score}", True, (0, 0, 0))
            screen.blit(Score_text, (WIDTH // 2 - Score_text.get_width() // 2, HEIGHT // 3))
            break

    #Enemy Spawner
    if current_time - enemy_spawn_time >= 1000 and player_alive:  # 1000 milliseconds = 1 seconds
        # Spawn a new enemy at a random position
        new_enemy = Enemy(player_1, screen, random.randint(0, 100), random.randint(0, 312), WIDTH, HEIGHT, wall_rect, 'wizard')
        enemy_group.add(new_enemy)  # Add the new enemy to the enemy group
        enemy_spawn_time = current_time  # Reset the spawn timer

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()