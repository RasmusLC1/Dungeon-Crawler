from scripts.level_generation.dungeon_enum_keys import *
from scripts.engine.assets.keys import keys

import random
class Vase_Spawner():


    @staticmethod
    def Spawn_Vase(map, level, size_x, size_y, tile_size, offgrid_tiles, A_Star_Search):
        loot_amount = random.randint(10 + level * 3, 20 + level * 3)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, size_x - 2)
            spawner_y = random.randint(1, size_y - 2)
            if map[spawner_x][spawner_y] != FLOOR:
                continue
            path = A_Star_Search(spawner_x, spawner_y)
            
            if path:
                offgrid_tiles.append({keys.type: keys.vase, keys.variant: 0, keys.pos: (spawner_x * tile_size, spawner_y * tile_size)})
                loot += 1