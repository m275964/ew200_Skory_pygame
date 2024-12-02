import pygame
from math import sin, cos, radians

class Arrow(pygame.sprite.Sprite):
    def __init__(self, screen, parent, x, y, WIDTH, HEIGHT, theta, wall_rect, speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.x = x
        self.y = y
        self.theta = theta
        self.speed = speed
        self.orig_image = pygame.image.load('kenney_tiny-town/Tiles/tile_0119.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.wall_rect = wall_rect
        self.screen_w = WIDTH
        self.screen_h = HEIGHT

    def check_collisions(self):
        # New positions based on movement
        new_x = self.x
        new_y = self.y
        # Check for collision with walls
        new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

        # If the new position collides with any of the wall_rects, kills the sprite
        if not any(new_rect.colliderect(wall) for wall in self.wall_rect):

            self.kill()

        self.rect = self.image.get_rect(center=(self.x, self.y))

    def border(self):

        if self.x < 10:
            self.kill()
        elif self.x > self.screen_w -10:
            self.kill()

        if self.y < 10:
            self.kill()
        elif self.y > self.screen_h - 10:
            self.kill()


        return self.x, self.y
    
    def update(self):
        dx = self.speed * cos(radians(self.theta))
        dy = self.speed * sin(radians(self.theta))

        self.x += dx
        self.y += dy
        self.rect.center(self.x, self.y)
        self.border()
        self.check_collisions()