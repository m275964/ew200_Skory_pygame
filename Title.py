#Basic imports
import pygame

#Background imports
from background import build_background

clock = pygame.time.Clock()

#title screen function
def display_title_screen(screen, WIDTH, HEIGHT):

    # set variables and instructions
    font = pygame.font.SysFont('Verdana', 50, bold = True)
    instructions_font = pygame.font.SysFont('Verdana', 30, italic= True)
    
    title_text = font.render("Wizard Wars", True, (0, 0, 0))  # White color for title
    instructions_text = instructions_font.render("Press SPACE to Start", True, (73,75,75))
    controls_text = instructions_font.render("Use WASD to Move", True, (73,75,75))
    controls_text_2 = instructions_font.render("Pres Space to Shoot arrows", True, (73,75,75))

    character_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0096.png')
    enemy_image = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0111.png')
    
    running_title_screen = True
    while running_title_screen:
        # Green background for title screen
        screen.fill((14,81,53))  
        
        
        # Position of the texts
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
        screen.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2))
        screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 1.5))
        screen.blit(controls_text_2, (WIDTH // 2 - controls_text_2.get_width() // 2, HEIGHT // 1))

        screen.blit(character_image, (200, HEIGHT/ 2))
        screen.blit(enemy_image, (600, HEIGHT/2))

    
        #Runs title screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # If spacebar is pressed, start the game
                    running_title_screen = False
        
        pygame.display.flip()
        clock.tick(60)