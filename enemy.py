#Basic imports
import pygame
import math
#Entities imports
from player import Player


class Enemy(Player):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, wall_rect, type='wizard'):
        # Initializes all previous attributes from the Player class
        super().__init__(screen, x, y, WIDTH, HEIGHT, wall_rect, type)
        self.player = player
        self.speed = 1

    def track_player(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y

        distance = math.hypot(dx, dy)

        if distance > 0:
            # Calculate the new potential position of the enemy
            new_x = self.x + self.speed * (dx / distance)
            new_y = self.y + self.speed * (dy / distance)

            # Check if the new position would collide with any walls or tracks
            new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

            # Only update position if there's no collision
            if not any(new_rect.colliderect(wall) for wall in self.wall_rect):
                self.x = new_x
                self.y = new_y

        # Update the enemy's rectangle
        self.rect = self.image.get_rect(center=(self.x, self.y))