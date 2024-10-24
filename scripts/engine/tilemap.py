from scripts.engine.utility.helper_functions import Helper_Functions

import json
import pygame
import math

AUTOTILE_MAP = {
    tuple(sorted([(1, 0), (0, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1), (-1, 0)])): 1,
    tuple(sorted([(-1, 0), (0, 1)])): 2, 
    tuple(sorted([(-1, 0), (0, -1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1)])): 4,
    tuple(sorted([(-1, 0), (0, -1), (1, 0)])): 5,
    tuple(sorted([(1, 0), (0, -1)])): 6,
    tuple(sorted([(1, 0), (0, -1), (0, 1)])): 7,
    tuple(sorted([(1, 0), (-1, 0), (0, 1), (0, -1)])): 8,
}

# Tiles that are checked for physics
NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'wall', 'LeftWall', 'RightWall', 'TopWall', 'BottomWall', 'DoorClosed'}
AUTOTILE_TYPES = {'floor'}
FLOOR_TTLES = {'floor'}

class Tilemap:
    def __init__(self, game, tile_size=16) -> None:
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []
        self.saved_data = {}
    
    def Save_Tile_Data(self):
        self.saved_data['tilemap'] = self.tilemap
        self.saved_data['offgrid_tiles'] = self.offgrid_tiles

    def Load_Data(self, data):
        for loaded_tile in  data['tilemap']:
            if not loaded_tile:
                continue
            for key, value in self.tilemap:
                print("KEY AND VALUE", key, value) 
                if not tile:
                    continue
                print("TILE: ", tile['pos'])
                print(tile['pos'])
                if tile['pos'] == tile['pos']:
                    tile['active'] = loaded_tile['active']
                    tile['light'] = loaded_tile['light']
                    break

        for loaded_tile in  data['offgrid_tiles']:
            for tile in self.tilemap:
                if tile['pos'] == tile['pos']:
                    tile['active'] = loaded_tile['active']
                    tile['light'] = loaded_tile['light']
                    break


            

    def extract(self, id_pairs, keep=False):
        matches = []
        for tile in self.offgrid_tiles.copy():
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile.copy())
                if not keep:
                    self.offgrid_tiles.remove(tile)
                    
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile.copy())
                matches[-1]['pos'] = matches[-1]['pos'].copy()
                matches[-1]['pos'][0] *= self.tile_size
                matches[-1]['pos'][1] *= self.tile_size
                if not keep:
                    del self.tilemap[loc]
        
        return matches
    

    # Get the position of tiles in the tilemap
    def Get_Pos(self):
        positions = []
        for tile in self.tilemap.values():
            positions.append(tile['pos'])
        return positions
    
    # Get the tile size
    def Get_Tile_Size(self):
        return self.tile_size
    
    # Get surrounding tiles
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    # Check what tile type is in a given position
    def Current_Tile_Type(self, pos):
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        check_loc = str(tile_loc[0]) + ';' + str(tile_loc[1])
        if check_loc in self.tilemap:
            return self.tilemap[check_loc]['type']
        else:
            return None
        
    # Check what tile type is in a given position
    def Current_Tile_Type_Without_Offset(self, pos):
        check_loc = str(pos[0]) + ';' + str(pos[1])
        if check_loc in self.tilemap:
            return self.tilemap[check_loc]['type']
        else:
            return None
        
    # Check what tile is in a given position and return the full tile
    def Current_Tile(self, pos):
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        check_loc = str(tile_loc[0]) + ';' + str(tile_loc[1])
        if check_loc in self.tilemap:
            return self.tilemap[check_loc]
        else:
            return None
        
    def Find_Nearby_Tiles(self, pos, max_distance):
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        normalised_max_distance = max_distance // 16
        nearby_tiles = []
        for tile_key in self.tilemap:
            tile = self.tilemap[tile_key]
            # Calculate the Euclidean distance
            distance = Helper_Functions.Abs_Distance_Float(tile_loc, tile['pos'])
            if distance < normalised_max_distance:
                nearby_tiles.append(tile)
        return nearby_tiles
    
    def Update_Tile_Type(self, pos, new_type):
        tile = self.Current_Tile(pos)
        tile['type'] = new_type


    # Check for collision on relevant tile
    def Collision_Check(self, pos):
        tile = self.Current_Tile_Type(pos)
        if not tile:
            return False
        if tile['type'] == 'Floor':
            return True
        else:
            return False

    
    def save(self, path):
        f = open(path, 'w')
        json.dump({'tilemap': self.tilemap, 'tile_size': self.tile_size, 'offgrid': self.offgrid_tiles}, f)
        f.close()
        
    def Load(self, path):
        f = open(path, 'r')
        map_data = json.load(f)
        f.close()
        
        self.tilemap = map_data['tilemap']
        self.tile_size = map_data['tile_size']
        self.offgrid_tiles = map_data['offgrid']
    
    # Check for collision with solid tiles
    def solid_check(self, pos):
        tile_loc = str(int(pos[0] // self.tile_size)) + ';' + str(int(pos[1] // self.tile_size))
        if tile_loc in self.tilemap:
            if self.tilemap[tile_loc]['type'] in PHYSICS_TILES:
                return self.tilemap[tile_loc]
    
    # Check for physics tiles
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    # Check for physics tiles
    def floor_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in FLOOR_TTLES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    # Automatically assign tiles
    def autotile(self):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            neighbors = set()
            for shift in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                check_loc = str(tile['pos'][0] + shift[0]) + ';' + str(tile['pos'][1] + shift[1])
                if check_loc in self.tilemap:
                    if self.tilemap[check_loc]['type'] == tile['type']:
                        neighbors.add(shift)
            neighbors = tuple(sorted(neighbors))
            if (tile['type'] in AUTOTILE_TYPES) and (neighbors in AUTOTILE_MAP):
                tile['variant'] = AUTOTILE_MAP[neighbors]



    # Convert screen coordinates to isometric grid coordinates
    def tile_isometric_to_grid(x, y):
        grid_x = (x // 10 + y // 5) // 2
        grid_y = (y // 5 - x // 10) // 2
        return int(grid_x), int(grid_y)
    
    def Set_Light_Level(self, tile, new_light_level):
        tile['light'] = new_light_level

    def Clear_Tilemap(self):
        self.tilemap.clear()
        self.offgrid_tiles.clear()
    
    # Render function that shows the entire screen
    def Render(self, surf, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, (offset[0] + surf.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                

                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))

        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

    # Render function that only renders the tiles in the tiles array
    def render_tiles(self, tiles, surf, offset=(0, 0)):
        for tile in tiles:
            if not tile:
                continue
            # Get the tile surface from the assets
            tile_surface = self.game.assets[tile['type']][tile['variant']].copy()
            
            # Adjust the tile activeness calculation
            tile_activeness = max(0, min(255, 700 - tile['active']))
            
            # Apply a non-linear scaling for a smoother transition
            tile_darken_factor = min(255, (255 * (1 - math.exp(-tile_activeness / 255)) + 150))

            if tile['light'] > 0:
                light_level = min(255, tile['light'] * 25)
            else:
                light_level = 1
            tile_darken_factor = max(0, min(220, tile_darken_factor - light_level))

            # Create a darkening surface with an alpha channel
            darkening_surface = pygame.Surface(tile_surface.get_size(), flags=pygame.SRCALPHA)
            darkening_surface.fill((0, 0, 0, int(tile_darken_factor)))
            
            # Blit the darkening surface onto the tile surface
            tile_surface.blit(darkening_surface, (0, 0))
            
            # Blit the darkened tile surface onto the main surface
            surf.blit(tile_surface, (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))


