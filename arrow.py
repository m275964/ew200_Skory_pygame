

import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, screen):
        super().__init__()
        self.image = pygame.image.load('kenney_tiny-town/Tiles/tile_0119.png')
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction  
        self.speed = speed
        self.screen = screen

    def update(self):
        # Move the projectile
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

        # Remove the projectile if it goes off screen
        if self.rect.x < 0 or self.rect.x > self.screen.get_width() or self.rect.y < 0 or self.rect.y > self.screen.get_height():
            self.kill()



    def check_collision(self, enemy_group):
        score_increase = 0
        for enemy in enemy_group:
            if pygame.sprite.collide_rect(self, enemy):  # Check if the arrow collides with the enemy
                enemy.kill()  # Remove the enemy from the game
                self.kill() #removes arrow from the game
                score_increase += 100  # Increase the score by 1 for each enemy hit
                break  # Avoid double-counting the same collision (if the arrow hits multiple enemies at once)
        return score_increase
