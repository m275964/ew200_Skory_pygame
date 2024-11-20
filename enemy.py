import pygame
import math
from player import Player


class Enemy(Player):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, type='wizard'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, type)
        self.player = player
        self.speed = 1.5

    def track_player(self):
        
        dx = self.player.x - self.x
        dy = self.player.y - self.y

        distance = math.hypot(dx, dy)

        if distance != 0:

            dx /= distance
            dy /= distance

        self.rect.x += dx + self.speed
        self.rect.y += dy + self.speed

