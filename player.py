import pygame
from background import build_background

TARGET_COLOR = (136, 153, 178)
class Player(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, WIDTH, HEIGHT, wall_rect, type='human'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 1
        self.type = type
        # Character sprite
        if type == 'human':
            self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0096.png')
        elif type == 'wizard':
            self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0111.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.length = self.rect.height
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.max_speed = 3
        self.reverse_time = pygame.time.get_ticks()
        self.screen = screen
        self.wall_rect = wall_rect


    
    def check_keys(self):
        press = pygame.key.get_pressed()

    # New positions based on movement
        new_x = self.x
        new_y = self.y

        if press[pygame.K_w]:
            new_y -= self.speed
        if press[pygame.K_s]:
            new_y += self.speed
        if press[pygame.K_a]:
            new_x -= self.speed
        if press[pygame.K_d]:
            new_x += self.speed

    # Check for collision with walls
        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

    # If the new position collides with any of the wall_rects, don't move
        if not any(new_rect.colliderect(wall) for wall in self.wall_rect):
            self.x = new_x
            self.y = new_y

        self.rect = self.image.get_rect(center=(self.x, self.y))


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
    
    def track_player(self):
        pass

    def update(self):
        if self.type == 'human':
            self.check_keys()



        self.rect = self.image.get_rect(center= (self.x, self.y))
        self.border()