# import pygame
# from math import sin, cos, radians

# class Arrow(pygame.sprite.Sprite):
#     def __init__(self, screen, parent, x, y, WIDTH, HEIGHT, theta, wall_rect, speed):
#         pygame.sprite.Sprite.__init__(self)
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.theta = theta
#         self.speed = speed
#         self.orig_image = pygame.image.load('kenney_tiny-town/Tiles/tile_0119.png')
#         self.image = self.orig_image
#         self.rect = self.image.get_rect()
#         self.wall_rect = wall_rect
#         self.screen_w = WIDTH
#         self.screen_h = HEIGHT

#     def check_collisions(self):
#         # New positions based on movement
#         new_x = self.x
#         new_y = self.y
#         # Check for collision with walls
#         new_rect = pygame.Rect(new_x, new_y, self.rect.width, self.rect.height)

#         # If the new position collides with any of the wall_rects, kills the sprite
#         if not any(new_rect.colliderect(wall) for wall in self.wall_rect):

#             self.kill()

#         self.rect = self.image.get_rect(center=(self.x, self.y))

#     def border(self):

#         if self.x < 10:
#             self.kill()
#         elif self.x > self.screen_w -10:
#             self.kill()

#         if self.y < 10:
#             self.kill()
#         elif self.y > self.screen_h - 10:
#             self.kill()


#         return self.x, self.y
    
#     def update(self):
#         dx = self.speed * cos(radians(self.theta))
#         dy = self.speed * sin(radians(self.theta))

#         self.x += dx
#         self.y += dy
#         self.rect.center(self.x, self.y)
#         self.border()
#         self.check_collisions()

import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, screen):
        super().__init__()
        self.image = pygame.image.load('kenney_tiny-town/Tiles/tile_0119.png')
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction  # direction of movement (angle or vector)
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
        # Check if the projectile collides with any enemy
        collided_enemies = pygame.sprite.spritecollide(self, enemy_group, True)  # Enemy will be killed if hit
        if collided_enemies:
            for enemy in collided_enemies:
                enemy.kill()  # Remove enemy from the group completely
            self.kill()  # Remove the projectile after collision

