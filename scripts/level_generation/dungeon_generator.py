from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.level_generation.noise_map import Noise_Map
from scripts.engine.tilemap.tilemap import Tilemap
from scripts.engine.a_star import A_Star
from scripts.level_generation.room_generation.circle_room import Circle_Room
from scripts.level_generation.room_generation.rectangle_room import Rectangle_Room
from scripts.level_generation.room_generation.level_structure import Level_Structure
from scripts.level_generation.dungeon_enum_keys import *
import random
import os

import math
# TODO:  shrines, entrance and exit, keys 



class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.player_spawn = (0, 0)
        self.cellular_automata = Cellular_Automata()
        self.tile_size = 32
        self.tilemap = Tilemap(self, tile_size=self.tile_size)
        self.a_star = A_Star()
        # TODO: IMPLEMENT MORE TRAPS AND ADD THEM HERE
        self.noise_map = Noise_Map()
        
        self.torches = []



    # Customise the internal map structure
    def Generate_Map(self, map_id):
        self.Update_Load_Menu(1)

        self.tilemap.Clear_Tilemap()
        self.cellular_automata.Create_Map()
        self.Update_Load_Menu(2)

        self.Spawn_Lakes(7, FLOOR, LAVA)

        
        self.Update_A_Star_Map()

        self.Player_Spawn()
        self.a_star.Set_Map('custom')
        self.Spawn_Traps(1)
        self.Update_Load_Menu(3)

        # Spawn more loot rooms in lower levels of dungeon
        # TODO: PROPER LEVEL SYSTEM
        if not self.Spawn_Loot_Room(map_id):
            self.Generate_Map(map_id)
            return
        
        self.Update_A_Star_Map()

        self.Update_Load_Menu(4)

        self.Spawn_Boss_Room()

        self.Update_A_Star_Map()

        # Call itself recursively and generate a new map if it fails to spawn enemies
        if not self.Enemy_Spawner():
            self.Generate_Map(map_id)
            return
        self.Update_Load_Menu(5)
        
        self.Spawn_Chest(2)

        self.Spawn_Portal_Shrine()

        self.Update_A_Star_Map()


        self.Spawn_Weapons(2)

        Level_Structure.Level_Structure(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y, self.tilemap)

    

        self.Update_Load_Menu(6)
        self.tilemap.save(f'data/maps/{map_id}.json')

    def Update_Load_Menu(self, value):
        self.game.menu_handler.Loading_Menu_Update(value)

    def Update_A_Star_Map(self):
        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

    def A_Star_Search(self, start_x, start_y):
        return self.a_star.a_star_search_no_diagonals([start_x, start_y], [self.player_spawn[0], self.player_spawn[1]], 'custom')
        

    # Spawn trap if density is greater than spawn trap, goes from 0 to 100
    def Spawn_Traps(self, density):
        for y in range(1, self.cellular_automata.size_y - 1):
            for x in range(1, self.cellular_automata.size_x - 1):
                if self.cellular_automata.map[x][y] != FLOOR:
                    continue
                spawn_trap = random.randint(0, 100)
                if spawn_trap < density:
                    self.cellular_automata.map[x][y] = TRAP

    
    def Spawn_Lakes(self, iterations, value_1, value_2):
        for i in range(iterations):

            density = random.randint(30, 40)
            size_x = random.randint(3, 5)
            size_y = random.randint(3, 5)
            start_x = random.randint(2, self.cellular_automata.size_x - size_x)
            start_y = random.randint(2, self.cellular_automata.size_y - size_y)
            lake_map = [[0 for _ in range(size_y)] for _ in range(size_x)]

            self.noise_map.Generate_Map(density, lake_map, value_1, value_2, size_x, size_y)
            self.cellular_automata.Refine_Level(value_1, value_2, size_x, size_y, 1, lake_map)
            i = 0
            j = 0
            for y in range(start_y, start_y + size_y):
                i = 0
                for x in range(start_x, start_x + size_x):
                    if x >= self.cellular_automata.size_x- 2 or y >= self.cellular_automata.size_y - 2:
                        break

                    self.cellular_automata.map[x][y] = lake_map[i][j]
                    if self.cellular_automata.map[x][y] == FLOOR:
                        spawn_loot = random.randint(0, 3)
                        if spawn_loot == 1:
                            self.tilemap.offgrid_tiles.append({"type": 'gold', "variant": 0, "pos": [x * self.tile_size, y * self.tile_size]})

                    i += 1
                j += 1

    

    def Spawn_Boss_Room(self):
        map_copy = self.cellular_automata.map.copy()
        fail = 0
        start_x = 0
        start_y = 0
        radius = 0

        while fail < 10:
            radius = random.randint(6, 8)
            start_x = random.randint(radius * 2, self.cellular_automata.size_x - radius * 2)
            start_y = random.randint(radius * 2, self.cellular_automata.size_y - radius * 2)
            
            path = []
            path = self.A_Star_Search(start_x, start_y)
            if path:
                break

            fail += 1

        # Create backup of map

        Circle_Room.Room_Structure_Circle(self.cellular_automata.map, start_x, start_y, radius)

        # Ensure there's a valid path to get into the boss room
        path = self.A_Star_Search(start_x, start_y)
        if not path:
            self.cellular_automata.map = map_copy
            self.Spawn_Boss_Room()
            
            return

        # self.tilemap.offgrid_tiles.append({"type": 'Shrine', "variant": 0, "pos": [start_x * self.tile_size, start_y * self.tile_size]})
        self.tilemap.offgrid_tiles.append({"type": 'Boss_Room', "variant": 0, "pos": [start_x * self.tile_size, start_y * self.tile_size], "radius": radius})
        self.Spawn_Traps_In_Boss_Room(start_x, start_y, radius)
        

    def Spawn_Traps_In_Boss_Room(self, start_x, start_y, radius):
        trap_number = random.randint(1, 5)
        i = 0
        while i < trap_number:
            pos_x = random.randint(start_x - radius + 1, start_x + radius - 2)
            pos_y = random.randint(start_y - radius + 1, start_y + radius - 2)
            
            distance_from_center = math.sqrt((pos_x - start_x) ** 2 + (pos_y - start_y) ** 2)
            if distance_from_center <= 2:
                continue
            self.cellular_automata.map[pos_x][pos_y] = TRAP
            i += 1



    def Spawn_Loot_Room(self, level):

        success = 0
        fail = 0

        rooms = random.randint(level, level + 4)

        while success <= rooms:
            size_x = random.randint(4, 6)
            size_y = random.randint(4, 6)
            start_x = random.randint(size_x + 4, self.cellular_automata.size_x - size_x)
            start_y = random.randint(size_y + 4, self.cellular_automata.size_y - size_y)

            # Ensure that the room is far enough away from the player
            distance = math.sqrt((self.player_spawn[0] - start_x) ** 2 + (self.player_spawn[1] - start_y) ** 2)
            if distance < 20:
                continue

            
            
            if not Rectangle_Room.Room_Structure_Rectangle(self.cellular_automata.map, start_x, start_y, size_x, size_y, self.A_Star_Search):
                fail += 1
                if fail >= 10 + level:
                    return False
                continue


            self.Spawn_Loot_In_Loot_Room(start_x, start_y, size_x, size_y)
            success += 1
        
        self.Spawn_Loot(rooms, 'key')
        
        return True
    
    def Spawn_Loot(self, amount, item):
        loot = 0
        while loot <= amount:
            pos_x = random.randint(2, self.cellular_automata.size_x - 3)
            pos_y = random.randint(2, self.cellular_automata.size_y - 3)
            if not self.cellular_automata.map[pos_x][pos_y] == FLOOR:
                continue
            self.tilemap.offgrid_tiles.append({"type": item, "variant": 0, "pos": [pos_x * self.tile_size, pos_y * self.tile_size]})
            loot += 1

    


    def Spawn_Loot_In_Loot_Room(self, start_x, start_y, size_x, size_y):
        loot_count = 0
        for y in range(start_y + 1, start_y + size_y - 1):
            for x in range(start_x + 1, start_x + size_x -1):
                spawn_loot = random.randint(0, 3 + loot_count)
                if spawn_loot == 0:
                    loot_count += 1
                    self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (x * self.tile_size, y * self.tile_size)})
                elif spawn_loot == 1:
                    loot_count += 1
                    self.tilemap.offgrid_tiles.append({"type": 'gold', "variant": 0, "pos": [x * self.tile_size, y * self.tile_size]})

        
        # Spawn a chest in case nothing else spawns as a backup
        if not loot_count:
            self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (start_x + size_x // 2 * self.tile_size, start_y + size_y // 2 * self.tile_size)})



    
    def Player_Spawn(self):
        self.player_spawn = (20, 20)
        for y in range(self.player_spawn[1] - 5, self.player_spawn[1] + 5):
            for x in range(self.player_spawn[0] - 5, self.player_spawn[0] + 5):
                random_variant = random.randint(0, 10)

                self.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'floor', 'variant': random_variant, 'pos': (x, y), 'active': 0, 'light': 0}
        
        self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (self.player_spawn[0] * self.tile_size, self.player_spawn[1] * self.tile_size)})

        # self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [self.player_spawn[0] * self.tile_size - 50, self.player_spawn[1] * self.tile_size]})
        self.tilemap.offgrid_tiles.append({"type": "Chest", "variant": 0, "pos": [self.player_spawn[0] * self.tile_size, self.player_spawn[1] * self.tile_size]})

    def Spawn_Portal_Shrine(self):
        spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
        spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
        path = self.A_Star_Search(spawner_x, spawner_y)

        if not path:
            self.Spawn_Portal_Shrine()
            return
        self.tilemap.offgrid_tiles.append({"type": "portal_shrine", "variant": 0, "pos": [spawner_x, spawner_y]})



    def Enemy_Spawner(self):
        spawners = 0
        fails = 0
        path = []
        while spawners < 80:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == WALL:
                continue
            path = self.A_Star_Search(spawner_x, spawner_y)
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 1, 'pos': (spawner_x * self.tile_size, spawner_y * self.tile_size)})
                spawners += 1
            else:
                fails += 1

            if fails > 20:
                return False
        
        return True
    
    def Spawn_Weapons(self, level):
        loot_amount = random.randint(10 + level * 2, 20 + level * 2)
        loot = 0 
        while loot < loot_amount:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] != FLOOR:
                continue
            
            self.tilemap.offgrid_tiles.append({'type': 'Weapon', 'variant': 0, 'pos': (spawner_x * self.tile_size, spawner_y * self.tile_size)})
            loot += 1


    def Spawn_Chest(self, level):
        loot_amount = random.randint(10 + level * 3, 20 + level * 3)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] != FLOOR:
                continue
            path = self.A_Star_Search(spawner_x, spawner_y)
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (spawner_x * self.tile_size, spawner_y * self.tile_size)})
                loot += 1


    def Delete_Map_File(self, file_path):

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
  