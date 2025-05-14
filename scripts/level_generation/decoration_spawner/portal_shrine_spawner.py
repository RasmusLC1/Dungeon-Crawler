import random
from scripts.engine.assets.keys import keys

class Portal_Shrine_Spawner():

    @staticmethod
    def Spawn_Portal_Shrine(size_x, size_y, A_Star_Search, offgrid_tiles):
        spawner_x = random.randint(1, size_x - 2)
        spawner_y = random.randint(1, size_y - 2)
        path = A_Star_Search(spawner_x, spawner_y)

        if not path:
            Portal_Shrine_Spawner.Spawn_Portal_Shrine(size_x, size_y, A_Star_Search, offgrid_tiles)
            return
        offgrid_tiles.append({"type": "portal_shrine", "variant": 0, "pos": [spawner_x, spawner_y]})


