import pygame
from Tile import Tile
from Functions import *


class A_Star():

    def __init__(self, screen, source_tile, destination_tile):
        self.half = 48 / 2
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

        self.loop()

        return_tiles = []
        parent = source_tile

        while True:
            return_tiles.append(parent)
            parent = parent.parent  # parent's parent

            if parent == None:
                break

            if parent.tile_id == destination_tile.tile_id:
                break

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

    def get_LFT(self):  # get Lowest F Value
        F_Values = []
        for tile in self.open_list:
            F_Values.append(tile.F)

        o = self.open_list[::-1]  # reversed list

        for tile in o:
            if tile.F == min(F_Values):
                return tile

    def move_to_G_cost(self, LFT, tile):
        GVal = 0
        direction = ((tile.grid_x - LFT.grid_x), (tile.grid_y - LFT.grid_y))

        if direction in (self.north, self.south, self.east, self.west):
            GVal = LFT.G + 10
        elif direction in (self.north_east, self.north_west, self.south_west, self.south_east):
            GVal = LFT.G + 14

        return GVal

    def loop(self):
        # Get lowest F tile
        LFT = self.get_LFT()
        self.swap(LFT)
        # get all the surrounding tiles
        surrounding_nodes = Tile.get_surrounding_tiles(LFT)

        for node in surrounding_nodes:
            if node:
                if node not in self.open_list:
                    self.open_list.append(node)
                    node.parent = LFT
                elif node in self.open_list:
                    # G check
                    calculated_G = self.move_to_G_cost(LFT, node)
                    if calculated_G < node.G:
                        node.parent = LFT
                        self.G(node)
                        self.F(node)

        if self.open_list == [] or self.destination_tile in self.closed_list:
            return

        for node2 in self.open_list:
            self.G(node2)
            self.F(node2)

        self.loop()
