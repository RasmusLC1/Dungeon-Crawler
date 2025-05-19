import random
from scripts.level_generation.dungeon_enum_keys import *
from scripts.engine.assets.keys import keys

class Portal_Shrine_Spawner():

    @staticmethod
    def Spawn_Portal_Shrine(map, size_x, size_y, A_Star_Search, offgrid_tiles):
        loot_amount = random.randint(2, 3)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, size_x - 2)
            spawner_y = random.randint(1, size_y - 2)
            if map[spawner_x][spawner_y] != FLOOR:
                continue
            path = A_Star_Search(spawner_x, spawner_y)
            
            if path:
                offgrid_tiles.append({"type": "portal_shrine", "variant": 0, "pos": [spawner_x, spawner_y]})

                loot += 1