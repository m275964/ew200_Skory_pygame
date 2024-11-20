import pygame
from background import build_background

TARGET_COLOR = (136, 153, 178)
class Player(pygame.sprite.Sprite):


    def __init__(self, screen, x, y, WIDTH, HEIGHT, type='human'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 1
        self.type = type
        # Character sprite
        if type == 'human':
            self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0085.png')
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
        self.background = build_background(self.screen_w, self.screen_h)


    
    def check_keys(self, collision = False):
        press = pygame.key.get_pressed()

        if press[pygame.K_w]:
            self.y -= self.speed
        if press[pygame.K_s]:
            self.y += self.speed


        if press[pygame.K_a]:
            self.x -= self.speed
        if press[pygame.K_d]:
            self.x += self.speed



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
        else:
            self.track_player()


        self.rect = self.image.get_rect(center= (self.x, self.y))
        self.border()

