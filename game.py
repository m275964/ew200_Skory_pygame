# Example file showing a basic pygame "game loop"
import pygame
   
# pygame setup
pygame.init()
WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

background = pygame.Surface((WIDTH, HEIGHT))
WATER = pygame.image.load('PNG/mapTile_187.png')
GRASS = pygame.image.load('PNG/mapTile_022.png')
GRASS_LEFT = pygame.image.load('PNG/mapTile_021.png')
GRASS_RIGHT = pygame.image.load('PNG/mapTile_023.png')
GRASS_BOTTOM = pygame.image.load('PNG/mapTile_037.png')
GRASS_BOTTOM_LEFT = pygame.image.load('PNG/mapTile_036.png')
GRASS_BOTTOM_RIGHT = pygame.image.load('PNG/mapTile_038.png')
GRASS_TOP = pygame.image.load('PNG/mapTile_007.png')
GRASS_TOP_LEFT = pygame.image.load('PNG/mapTile_006.png')
GRASS_TOP_RIGHT = pygame.image.load('PNG/mapTile_008.png')

TILE_SIZE = WATER.get_width()

# fill the screen with a color to wipe away anything from last frame
for x in range(0, WIDTH, TILE_SIZE):
    for y in range(0, HEIGHT, TILE_SIZE):
        background.blit(WATER, (x, y))
        




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # RENDER YOUR GAME HERE

    #blit the background to the screen
    screen.blit(background, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()