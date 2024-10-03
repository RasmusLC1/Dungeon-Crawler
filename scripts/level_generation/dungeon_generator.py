from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.level_generation.noise_map import Noise_Map
from scripts.engine.tilemap import Tilemap
from scripts.engine.a_star import A_Star
import random
import os

import math
# TODO:  shrines, entrance and exit, keys 

class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.player_spawn = (0, 0)
        self.cellular_automata = Cellular_Automata()
        self.tilemap = Tilemap(self, tile_size=16)
        self.a_star = A_Star()
        self.traps = ['spike_trap', 'spike_poison_trap', 'Pit_trap', 'Pit_trap', 'Pit_trap']
        self.noise_map = Noise_Map
        self.torches = []




    def Generate_Map(self):
        self.Delete_Map_File('data/maps/0.json')
        self.tilemap.Clear_Tilemap()
        self.cellular_automata.Create_Map()

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
                    if not self.Wall_Checker(i, j):
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


                elif self.cellular_automata.map[i][j] == 0: # Floor
                    self.Floor_Checker(i, j)
                elif self.cellular_automata.map[i][j] == 2:
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Lava_env', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


    # Spawns torches based on density, it then checks 
    def Torch_Spawner(self, i, j, density):
        spawn_torch = random.randint(0, density)
        if spawn_torch == 1:
            for torch in self.torches:
                distance = math.sqrt((i - torch[0]) ** 2 + (j - torch[1]) ** 2)
                if distance < 8:
                    return
            self.torches.append((i, j))
            self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [i * 16, j * 16]})

    def Floor_Checker(self, i, j):
        value = random.randint(0, 100)
        if value < 3:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': self.traps[value], 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
        else:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Floor', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            self.Torch_Spawner(i, j, 5)

    def Wall_Checker(self, i, j):

        # Handle Edge cases first to prevent crashes
        if i <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'LeftWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        elif i >= self.cellular_automata.size_x - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'RightWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'TopWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j >= self.cellular_automata.size_y - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        wall_found = False

        if self.cellular_automata.map[i + 1][j] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'LeftWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True

        elif self.cellular_automata.map[i - 1][j] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'RightWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True


        if self.cellular_automata.map[i][j - 1] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'TopWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True

        elif self.cellular_automata.map[i][j + 1] != 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'BottomWall', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
            wall_found = True
            
        return wall_found
        
 

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
            


