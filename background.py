import pygame
from random import randint


def build_background(WIDTH, HEIGHT):
    wall_rects = [] # contains all my wall rectangle

    background = pygame.Surface((WIDTH, HEIGHT))
    DIRT = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0049.png') # tile_49
    GRASS = pygame.image.load('kenney_tiny-town/Tiles/tile_0001.png')

    #Castle tiles
    STAIRS = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0037.png')
    FRONT_WALL = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0040.png')
    TOP_WALL = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0002.png')
    BACK_WALL = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0026.png')
    ROOF = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0000.png')

    #Castle sides
    LEFT_FRONT_CORNER = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0016.png')
    LEFT_WALL = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0015.png')
    LEFT_BACK_CORNER = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0004.png')

    RIGHT_FRONT_CORNER = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0017.png')
    RIGHT_WALL = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0013.png')
    RIGHT_BACK_CORNER = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0005.png')

    #train tracks
    HOR_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0094.png')
    VER_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0083.png')
    LEFT_TOP_CORNER_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0069.png')
    RIGHT_TOP_CORNER_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0071.png')
    LEFT_BOTTOM_CORNER_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0093.png')
    RIGHT_BOTTOM_CORNER_TRACK = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0095.png')

    #Images
    CROSS = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0064.png')
    GRAVE = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0065.png')
    TREE = pygame.image.load('kenney_tiny-town/Tiles/tile_0016.png')
    CHEST = pygame.image.load('kenney_tiny-dungeon/Tiles/tile_0089.png')

    TILE_SIZE = DIRT.get_width()
    print(TILE_SIZE)

# fill the screen with a color to wipe away anything from last frame
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            #Default Background
            background.blit(DIRT, (x, y))



            #Back of Castles
            if ((x == (8*TILE_SIZE)) or (x == (24*TILE_SIZE))) and y == 0:
                background.blit(LEFT_BACK_CORNER, (x, y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif ((x > (8*TILE_SIZE) and x < (16*TILE_SIZE)) or (x > (24*TILE_SIZE) and x < (32*TILE_SIZE))) and y == 0:
                background.blit(BACK_WALL, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif ((x == (16*TILE_SIZE)) or (x == (32*TILE_SIZE))) and y == 0:
                background.blit(RIGHT_BACK_CORNER, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

            #Side of Castles
            elif ((x == (8*TILE_SIZE)) or (x == (24*TILE_SIZE))) and (y > 0 and y < (8*TILE_SIZE)):
                background.blit(LEFT_WALL, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif ((x > (8*TILE_SIZE) and x < (16*TILE_SIZE)) or (x > (24*TILE_SIZE) and x < (32*TILE_SIZE))) and (y > 0 and y < (8*TILE_SIZE)):
                background.blit(ROOF, (x,y))

            elif ((x == (16*TILE_SIZE)) or (x == (32*TILE_SIZE))) and (y > 0 and y < (8*TILE_SIZE)):
                background.blit(RIGHT_WALL, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

            #Front of castles
            elif ((x == (8*TILE_SIZE)) or (x == (24*TILE_SIZE))) and y == (8*TILE_SIZE):
                background.blit(LEFT_FRONT_CORNER, (x, y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            elif ((x >= (8*TILE_SIZE) and x <= (10*TILE_SIZE)) or (x >= (14*TILE_SIZE) and x <= (16*TILE_SIZE)) or (x >= (24*TILE_SIZE) and x <= (26*TILE_SIZE)) or (x >= (30*TILE_SIZE) and x <= (32*TILE_SIZE))) and y == (8*TILE_SIZE):

                background.blit(TOP_WALL, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

            elif ((x == (16*TILE_SIZE)) or (x == (32*TILE_SIZE))) and y == (8*TILE_SIZE):
                background.blit(RIGHT_FRONT_CORNER, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            
            elif ((x >= (8*TILE_SIZE) and x <= (10*TILE_SIZE)) or (x >= (14*TILE_SIZE) and x <= (16*TILE_SIZE)) or (x >= (24*TILE_SIZE) and x <= (26*TILE_SIZE)) or (x >= (30*TILE_SIZE) and x <= (32*TILE_SIZE))) and (y > (8*TILE_SIZE) and  y < (11*TILE_SIZE)):
                background.blit(FRONT_WALL, (x,y))
                wall_rects.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))

            #Stairs
            elif ((x > (10*TILE_SIZE) and x < (14*TILE_SIZE)) or (x > (26*TILE_SIZE) and x < (30*TILE_SIZE))) and (y >= (8*TILE_SIZE) and  y <= (11*TILE_SIZE)):
                background.blit(STAIRS, (x,y))

            #TRAIN TRACKS
            if ((x >= 0) and (x < 24*TILE_SIZE)) and (y== 24*TILE_SIZE):
                background.blit(HOR_TRACK, (x,y))

            elif ((x == 24*TILE_SIZE) and (y==24*TILE_SIZE)):
                background.blit(RIGHT_TOP_CORNER_TRACK, (x,y))

            elif ((x == 24*TILE_SIZE) and (y>24*TILE_SIZE)):
                background.blit(VER_TRACK, (x,y))

            #Forest
            if (x > 28 * TILE_SIZE and x < 46 *TILE_SIZE) and (y > 22*TILE_SIZE):
                background.blit(GRASS, (x,y))
            if (x == 30*TILE_SIZE or x == 32*TILE_SIZE or x == 34 *TILE_SIZE or x== 36*TILE_SIZE or x == 38*TILE_SIZE or x == 40 * TILE_SIZE or x == 42*TILE_SIZE or x ==44 *TILE_SIZE) and (y == 24* TILE_SIZE or y == 27* TILE_SIZE or y == 30* TILE_SIZE):
                background.blit(TREE, (x,y))

            #Graveyard
            if (x== 36*TILE_SIZE or x == 40 * TILE_SIZE or x ==44 *TILE_SIZE) and (y == 8* TILE_SIZE or y == 6* TILE_SIZE or y == 4* TILE_SIZE):
                background.blit(GRAVE, (x,y))
            if (x == 38*TILE_SIZE or x == 42*TILE_SIZE or x == 47 * TILE_SIZE) and (y == 9* TILE_SIZE or y == 1* TILE_SIZE or y == 5* TILE_SIZE):
                background.blit(CROSS, (x,y))

            #Chest
            if (x == 10 *TILE_SIZE or x == 14*TILE_SIZE or x == 26*TILE_SIZE or x == 30 *TILE_SIZE) and (y == 3 *TILE_SIZE):
                background.blit(CHEST, (x,y))

  
            
            

    return background, wall_rects





