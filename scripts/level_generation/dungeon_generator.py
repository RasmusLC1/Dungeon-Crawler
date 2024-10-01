from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.level_generation.noise_map import Noise_Map
from scripts.engine.tilemap import Tilemap
from scripts.engine.a_star import A_Star
import random
import os


class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.player_spawn = (0, 0)
        self.cellular_automata = Cellular_Automata()
        self.tilemap = Tilemap(self, tile_size=16)
        self.a_star = A_Star()
        self.traps = ['spike_trap', 'spike_poison_trap', 'Pit_trap', 'Pit_trap', 'Pit_trap']
        self.noise_map = Noise_Map




    def Generate_Map(self):
        self.Delete_Map_File('data/maps/0.json')
        self.tilemap.Clear_Tilemap()
        self.cellular_automata.Create_Map()
        # for row in self.cellular_automata.map:
        #      print(row)
        self.Level_Structure()
        
        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

        self.Player_Spawn()

        # Call itself recursively and generate a new map if it fails to spawn enemies
        if not self.Enemy_Spawner():
            self.Generate_Map()

            return
        
        self.Spawn_Loot(2)
        

        self.tilemap.save('data/maps/0.json')

    def Level_Structure(self):
        for j in range(self.cellular_automata.size_y):
            for i in range(self.cellular_automata.size_x):
                if self.cellular_automata.map[i][j] == 1: # Wall 
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'TopWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif self.cellular_automata.map[i][j] == 0: # Floor
                    value = random.randint(0, 100)
                    if value < 3:
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': self.traps[value], 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                    else:
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Floor', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif self.cellular_automata.map[i][j] == 2:
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Lava_env', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                    

    def Generate_Lava(self):
        spawners = 0
        fails = 0
        while spawners < 3:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == 1:
                fails += 1
                if fails > 10:
                    return
                continue
            self.Generate_Lava_Lake()
            spawners += 1
        
        return


    
    def Generate_Lava_Lake(self):
        size = 20
        density = random.randint(40, 60)
        lava_map = [[0 for _ in range(self.size_y)] for _ in range(self.size_x)]
        self.noi

    
    def Player_Spawn(self):
        self.player_spawn = (20, 20)
        for y in range(self.player_spawn[1] - 5, self.player_spawn[1] + 5):
            for x in range(self.player_spawn[0] - 5, self.player_spawn[0] + 5):
                self.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y), 'active': 0, 'light': 0}
        
        self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (self.player_spawn[0] * 16, self.player_spawn[1] * 16)})

        self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [self.player_spawn[0] * 16, self.player_spawn[1] * 16]})
    
    def Enemy_Spawner(self):
        spawners = 0
        fails = 0
        path = []
        self.a_star.Set_Map('custom')
        while spawners < 10:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == 1:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 1, 'pos': (spawner_x * 16, spawner_y * 16)})
                spawners += 1
            else:
                fails += 1

            if fails > 20:
                return False
        
        return True

    def Spawn_Loot(self, level):
        loot_amount = random.randint(10 + level, 20 + level)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == 1:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (spawner_x * 16, spawner_y * 16)})
                loot += 1


    def Delete_Map_File(self, file_path):

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
            



    # TODO: Enemy spawning, loot, shrines, entrance and exit, keys 