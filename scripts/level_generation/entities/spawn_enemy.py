from scripts.level_generation.dungeon_enum_keys import *
import random
from scripts.engine.assets.keys import keys

class Spawn_Enemy():

    @staticmethod
    def Enemy_Spawner(map, tile_size, size_x, size_y, A_Star_Search, offgrid_tiles):
        spawners = 0
        fails = 0
        path = []
        while spawners < 80:
            spawner_x = random.randint(1, size_x - 2)
            spawner_y = random.randint(1, size_y - 2)
            if map[spawner_x][spawner_y] == WALL:
                continue
            path = A_Star_Search(spawner_x, spawner_y)
            
            if path:
                offgrid_tiles.append({'type': 'spawners', 'variant': 1, 'pos': (spawner_x * tile_size, spawner_y * tile_size)})
                spawners += 1
            else:
                fails += 1

            if fails > 20:
                return False
        
        return True