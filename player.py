import pygame
from math import cos, sin, pi, radians


class Player(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, WIDTH, HEIGHT, theta = 270):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = 0
        self.theta = theta
        # Character sprite
        self.orig_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0085.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.length = self.rect.height
        self.rect.center = (self.x, self.y)
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.max_speed = 3
        self.reverse_time = pygame.time.get_ticks()
        self.screen = screen

    def radians(self, deg):
        rad = (deg/180) *pi
        return rad
    
    def check_keys(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_w]:
            self.speed += 0.1
        if press[pygame.K_s]:
            self.speed -= 0.1
        if (not press[pygame.K_w]) and (not press[pygame.K_s]):
            self.speed = 0

        if press[pygame.K_a]:
            self.theta += 1
        if press[pygame.K_d]:
            self.theta -= 1

    def border(self):
        
        border_rect = pygame.rect.Rect(0,0, self.screen_w, self.screen_h)
        if not border_rect.contains(self.rect):
            if pygame.time.get_ticks() - self.reverse_time > 500:
                self.speed = -0.2 *self.speed
                self.reverse_time = pygame.time.get_ticks()

    def update(self):

        self.border()
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        elif self.speed < -self.max_speed:
            self.speed = -self.max_speed
        
        rad = self.radians(self.theta)
        x_dot = cos(rad) * self.speed
        y_dot = sin(rad) * self.speed

        self.x += x_dot
        self.y -= y_dot

        self.image = pygame.transform.rotozoom(self.orig_image, self.theta - 270, 1.2)
        self.rect = self.image.get_rect(center= (self.x, self.y))

        