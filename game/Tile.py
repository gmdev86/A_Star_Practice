import pygame


class Tile(pygame.Rect):
    # Hold list of Tiles
    List = []

    # Assign Tile a number
    total_tile = 0

    def __init__(self, x, y, grid_x, grid_y, width, height, color, tile_type='empty'):
        self.x = x
        self.y = y
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.width = width
        self.height = height
        self.color = color
        self.tile_type = tile_type
        self.tile_id = Tile.total_tile
        self.parent = None
        self.H, self.G, self.F = 0, 0, 0

        # check type
        if tile_type == 'solid':
            self.walkable = False
        else:
            self.walkable = True

        # Add 1 to total tiles
        Tile.total_tile += 1

        # Initialize the base
        pygame.Rect.__init__(self, (x, y), (self.width, self.height))

        # Add tile to master list
        Tile.List.append(self)

    def __str__(self):
        return str(self.tile_id)

    @staticmethod
    def get_tile_by_id(tile_id):
        for tile in Tile.List:
            if tile.tile_id == tile_id:
                return tile

    @staticmethod
    def get_tile_by_grid_pos(pos_x, pos_y):
        for tile in Tile.List:
            if tile.grid_x == pos_x:
                if tile.grid_y == pos_y:
                    return tile

    @staticmethod
    def get_surrounding_tiles(tile):
        surrounding_tile = []
        N_x = tile.grid_x
        N_y = tile.grid_y - 1
        S_x = tile.grid_x
        S_y = tile.grid_y + 1
        E_x = tile.grid_x + 1
        E_y = tile.grid_y
        W_x = tile.grid_x - 1
        W_y = tile.grid_y

        NW_x = tile.grid_x - 1
        NW_y = tile.grid_y - 1
        NE_x = tile.grid_x + 1
        NE_y = tile.grid_y - 1
        SW_x = tile.grid_x - 1
        SW_y = tile.grid_y + 1
        SE_x = tile.grid_x + 1
        SE_y = tile.grid_y + 1

        s_tile = Tile.get_tile_by_grid_pos(N_x, N_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(S_x, S_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(E_x, E_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(W_x, W_y)
        surrounding_tile.append(s_tile)

        s_tile = Tile.get_tile_by_grid_pos(NW_x, NW_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(NE_x, NE_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(SW_x, SW_y)
        surrounding_tile.append(s_tile)
        s_tile = Tile.get_tile_by_grid_pos(SE_x, SE_y)
        surrounding_tile.append(s_tile)

        return surrounding_tile
