from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.engine.tilemap import Tilemap
import random


class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.cellular_automata = Cellular_Automata()
        self.tilemap = Tilemap(self, tile_size=16)




    def Generate_Map(self):
        self.cellular_automata.Create_Map()
        # for row in self.cellular_automata.map:
        #      print(row)
        for i in range(self.cellular_automata.size_x):
            for j in range(self.cellular_automata.size_y):
                if self.cellular_automata.map[j][i] == 1:
                    self.tilemap.tilemap[str(j) + ';' + str(i)] = {'type': 'TopWall', 'variant': 0, 'pos': (j, i), 'active': 0, 'light': 0}
                else:
                    self.tilemap.tilemap[str(j) + ';' + str(i)] = {'type': 'Floor', 'variant': 0, 'pos': (j, i), 'active': 0, 'light': 0}
        
        self.Player_Spawn()

        self.tilemap.save('data/maps/0.json')

    def Player_Spawn(self):
        player_spawn = (20, 20)
        for x in range(player_spawn[0] - 5, player_spawn[0] + 5):
            for y in range(player_spawn[1] - 5, player_spawn[1] + 5):
                self.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y), 'active': 0, 'light': 0}
        
        self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (player_spawn[0] * 16, player_spawn[1] * 16)})

        self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [player_spawn[0] * 16, player_spawn[1] * 16]})
        