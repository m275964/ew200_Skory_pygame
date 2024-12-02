import pygame
from background import build_background
import random


clock = pygame.time.Clock()


def display_title_screen(screen, WIDTH, HEIGHT):
    font = pygame.font.SysFont('Verdana', 50, bold = True)
    instructions_font = pygame.font.SysFont('Verdana', 30, italic= True)
    
    title_text = font.render("Wizard Wars", True, (0, 0, 0))  # White color for title
    instructions_text = instructions_font.render("Press SPACE to Start", True, (73,75,75))
    controls_text = instructions_font.render("Use WASD to Move", True, (73,75,75))
    
    running_title_screen = True
    while running_title_screen:
        # Green background for title screen
        screen.fill((14,81,53))  
        
        
        # Position of the texts
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
        screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 1.5))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # If spacebar is pressed, start the game
                    running_title_screen = False
        
        pygame.display.flip()
        clock.tick(60)