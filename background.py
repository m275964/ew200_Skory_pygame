import pygame

def build_background(WIDTH, HEIGHT):

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
        if (x > TILE_SIZE*2) and (x < (WIDTH - TILE_SIZE*3)):
            background.blit(GRASS, (x, y))
