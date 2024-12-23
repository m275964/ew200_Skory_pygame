#Basic imports
import pygame
#Background imports
from background import build_background
#Entities imports
from arrow import Arrow

#player class
class Player(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, WIDTH, HEIGHT, wall_rect, type='human'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 1
        self.type = type
        self.max_speed = 3
        self.direction = (1, 0)
        # Character sprite
        if type == 'human':
            self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0096.png')
        elif type == 'wizard':
            self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0111.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.length = self.rect.height
        self.rect.center = (self.x, self.y)
        #screen attributes
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.reverse_time = pygame.time.get_ticks()
        self.screen = screen
        self.wall_rect = wall_rect
        #arrow attributes
        self.arrow_group = pygame.sprite.Group()
        self.last_shot_time = pygame.time.get_ticks()

    #allows for player movement
    def check_keys(self, player_alive):
        if not player_alive:
            return
        press = pygame.key.get_pressed() # Press function

        # New positions based on movement
        new_x = self.x
        new_y = self.y

        #movement arguements
        if press[pygame.K_w]:
            new_y -= self.speed
            self.direction = (0, -1)  # Up
        if press[pygame.K_s]:
            new_y += self.speed
            self.direction = (0, 1)  # Down
        if press[pygame.K_a]:
            new_x -= self.speed
            self.direction = (-1, 0)  # Left
        if press[pygame.K_d]:
            new_x += self.speed
            self.direction = (1, 0)  # Right
        if press[pygame.K_SPACE]:
            self.shoot(player_alive)

        # Check for collision with walls
        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

        # If the new position collides with any of the wall_rects, don't move
        if not any(new_rect.colliderect(wall) for wall in self.wall_rect):
            self.x = new_x
            self.y = new_y

        self.rect = self.image.get_rect(center=(self.x, self.y))


    #border functions
    def border(self):
        if self.type != 'human':
            return

        if self.x < 10:
            self.x = 10
        elif self.x > self.screen_w -10:
            self.x = self.screen_w - 10

        if self.y < 10:
            self.y = 10
        elif self.y > self.screen_h - 10:
            self.y = self.screen_h - 10


        return self.x, self.y
    
    # Only applies to the enemy class
    def track_player(self):
        pass

    # Spawn the arrow at the player's position
    def shoot(self, player_alive):
        if not player_alive:
            return
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 500: # 500 miliseconds, .5 seconds. Gives a delay between every shot
            arrow = Arrow(self.x, self.y, self.direction, 5, self.screen)
            self.arrow_group.add(arrow)
            self.last_shot_time = current_time



    def update(self, player_alive):
        if self.type == 'human':
            self.check_keys(player_alive)


        self.arrow_group.update()
        self.rect = self.image.get_rect(center= (self.x, self.y))
        self.border()