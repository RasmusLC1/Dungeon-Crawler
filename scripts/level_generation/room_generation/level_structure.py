import random
from scripts.level_generation.dungeon_enum_keys import *
from scripts.level_generation.decoration_spawner.torch_spawner import Torch_Spawner
from scripts.engine.assets.keys import keys


class Level_Structure():

    @staticmethod
    def Level_Structure(map, tile_size, size_x, size_y, tilemap):
        traps = [keys.spike_trap, keys.spike_poison_trap, keys.pit_trap]

        torches = []
        for j in range(size_y):
            for i in range(size_x):
                if map[i][j] == WALL: 
                    if not Level_Structure.Wall_Checker(map, i, j, size_x, size_y, tilemap.tilemap):
                        tilemap.tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_bottom, 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


                elif map[i][j] == FLOOR: # Floor
                    Level_Structure.Floor_Checker(i, j, tile_size, tilemap, torches)
                elif map[i][j] == LAVA:
                    tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Lava_env', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif map[i][j] == DOOR:
                    tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'door_basic', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif map[i][j] == TRAP:
                    trap_type = random.randint(0, 2)
                    tilemap.tilemap[str(i) + ';' + str(j)] = {'type': traps[trap_type], 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
    
    def Floor_Checker(i, j, tile_size, tilemap, torches):
        random_variant = random.randint(0, 10)
        tilemap.tilemap[str(i) + ';' + str(j)] = {'type': keys.floor, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
        Torch_Spawner.Torch_Spawner(i, j, tile_size, 20, torches, tilemap.offgrid_tiles)


    def Wall_Checker(map, i, j, size_x, size_y, tilemap):
        random_variant = random.randint(0, 3)
        # Handle Edge cases first to prevent crashes
        if i <= 1:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_left, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        elif i >= size_x - 2:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_right, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j <= 1:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_top, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j >= size_y - 2:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_top, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        


        if map[i][j + 1] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_top, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True



        if Level_Structure.Corner_Handling(map, i, j, random_variant, tilemap):
            return True
        

        if map[i + 1][j] != WALL and map[i - 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_middle, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        if map[i + 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_left, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True


        if map[i - 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_right, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        return False
    
    def Corner_Handling(map, i, j, random_variant, tilemap) -> bool:
        if not map[i][j - 1] != WALL:
            return False
        
        left_side = 0
        right_side = 1
        both_sides = 2
        if map[i + 1][j] != WALL and map[i - 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_bottom_corner, 'variant': both_sides, 'pos': (i, j), 'active': 0, 'light': 0}

        elif map[i + 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_bottom_corner, 'variant': right_side, 'pos': (i, j), 'active': 0, 'light': 0}

        elif map[i - 1][j] != WALL:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_bottom_corner, 'variant': left_side, 'pos': (i, j), 'active': 0, 'light': 0}

        else:
            tilemap[str(i) + ';' + str(j)] = {'type': keys.wall_bottom, 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
        return True