

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

    def check_collision(self, enemy_group, Score):
        #score_increment = 0
        score_increment = Score
        # Check if the projectile collides with any enemy
        collided_enemies = pygame.sprite.spritecollide(self, enemy_group, True)  
        if collided_enemies:
            for enemy in collided_enemies:
                enemy.kill() 
            self.kill()  
            score_increment += 100  
        return score_increment

