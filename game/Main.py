import pygame
import sys
from Tile import Tile
from A_Star import A_Star
from Functions import *

pygame.init()
pygame.font.init()
screen_size = (480, 480)
tile_width = 48
tile_height = 48
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
FPS = 25

# Create Tilemap
pos_y = 0
pos_x = 0
for y in range(0, 480, 48):
    for x in range(0, 480, 48):
        Tile(x, y, pos_x, pos_y, 48, 48, (255, 0, 0), 'empty')
        pos_x += 1

    pos_y += 1
    pos_x = 0

lead_x = 0
lead_y = 0
lead_x_change = 0
lead_y_change = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -1
            if event.key == pygame.K_RIGHT:
                lead_x_change = 1
            if event.key == pygame.K_UP:
                lead_y_change = -1
            if event.key == pygame.K_DOWN:
                lead_y_change = +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                lead_y_change = 0

    screen.fill((0, 0, 0))
    lead_x += lead_x_change
    lead_y += lead_y_change

    if lead_x < 0:
        lead_x = 0
    if lead_y < 0:
        lead_y = 0
    if lead_x > 9:
        lead_x = 9
    if lead_y > 9:
        lead_y = 9

    #print '(' + str(lead_x) + ',' + str(lead_y) + ')'
    start_tile = Tile.get_tile_by_grid_pos(lead_x, lead_y)
    destination_tile = Tile.get_tile_by_grid_pos(9, 9)
    pygame.draw.rect(screen, (0, 0, 255), start_tile)
    pygame.draw.rect(screen, (155, 155, 155), destination_tile)

    surrounding_tiles = Tile.get_surrounding_tiles(start_tile)

    for s_tile in surrounding_tiles:
        if s_tile:
            pygame.draw.rect(screen, (0, 108, 0), s_tile)

    A_Star(screen, start_tile, destination_tile)

    for tile in Tile.List:
        pygame.draw.rect(screen, (255, 0, 0), tile, 1)
        text_to_screen(screen, '(' + str(tile.grid_x) + ',' + str(tile.grid_y) + ')', tile.x, tile.y,
                       12, (255, 255, 255), 'monospace')

    clock.tick(FPS)
    pygame.display.update()
