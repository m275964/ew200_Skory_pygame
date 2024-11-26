import pygame
import math
from player import Player


class Enemy(Player):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, type='wizard'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, type)
        self.player = player
        self.speed = 1

    def track_player(self, target_x, target_y):
        
        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.hypot(dx, dy)

        if distance > 0:
            self.x += self.speed * (dx/distance)
            self.y += self.speed * (dy / distance)