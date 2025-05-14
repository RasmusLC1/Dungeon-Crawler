import random
from scripts.engine.assets.keys import keys

class Spawn_Player():

    @staticmethod
    def Player_Spawn(tile_size, tilemap):
        player_spawn = (20, 20)
        for y in range(player_spawn[1] - 5, player_spawn[1] + 5):
            for x in range(player_spawn[0] - 5, player_spawn[0] + 5):
                random_variant = random.randint(0, 10)

                tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'floor', 'variant': random_variant, 'pos': (x, y), 'active': 0, 'light': 0}
        
        tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (player_spawn[0] * tile_size, player_spawn[1] * tile_size)})

        # tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [player_spawn[0] * tile_size - 50, player_spawn[1] * tile_size]})
        tilemap.offgrid_tiles.append({"type": "chest", "variant": 0, "pos": [player_spawn[0] * tile_size, player_spawn[1] * tile_size]})


        return player_spawn