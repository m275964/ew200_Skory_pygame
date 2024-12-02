import pygame
from math import sin, cos, radians

class Ax(pygame.sprite.Sprite):
    def __init__(self, screen, parent, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.parent = parent
        self.x = x
        self.y = y
        self.orig_image = pygame.image.load('kenney_tiny-town/Tiles/tile_0127.png')