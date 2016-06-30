import pygame
from Tile import Tile
from Functions import *


class A_Star():

    def __init__(self, screen, source_tile, destination_tile):
        #self.half = Tile.width / 2
        self.open_list = []  # tiles to check
        self.closed_list = []  # tiles already checked
        self.source_tile = source_tile
        self.destination_tile = destination_tile
        self.open_list.append(source_tile)
        self.screen = screen

        self.north = (0, -1)
        self.south = (0, 1)
        self.east = (1, 0)
        self.west = (-1, 0)
        self.north_west = (-1, -1)
        self.north_east = (1, -1)
        self.south_west = (-1, 1)
        self.south_east = (1, 1)

        # get all the surrounding tiles
        self.surrounding_nodes = Tile.get_surrounding_tiles(source_tile)

        for node in self.surrounding_nodes:
            if node:
                node.parent = source_tile
                self.open_list.append(node)

        self.H()

        for node in self.surrounding_nodes:
            if node:
                self.G(node)
                self.F(node)

    def H(self):
        for tile in Tile.List:
            tile.H = 10 * (abs(tile.x - self.destination_tile.x) + abs(tile.y - self.destination_tile.y)) / tile.height
            text_to_screen(self.screen, 'H: ' + str(tile.H), tile.x, tile.y + 12,
                           12, (255, 255, 255), 'monospace')

    def G(self, tile):
        direction = ((tile.parent.grid_x - tile.grid_x), (tile.parent.grid_y - tile.grid_y))

        if direction in (self.north, self.south, self.east, self.west):
            # 10
            tile.G = tile.parent.G + 10
        elif direction in (self.north_east, self.north_west, self.south_west, self.south_east):
            # 14
            tile.G = tile.parent.G + 14

        text_to_screen(self.screen, 'G: ' + str(tile.H), tile.x, tile.y + 24,
                       12, (255, 255, 255), 'monospace')

    def F(self, tile):
        # F = G + H
        tile.F = tile.G + tile.H
        text_to_screen(self.screen, 'F: ' + str(tile.H), tile.x, tile.y + 36,
                       12, (255, 255, 255), 'monospace')

    def swap(self, tile):
        self.open_list.remove(tile)
        self.closed_list.append(tile)
