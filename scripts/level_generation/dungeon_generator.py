from scripts.level_generation.cellular_automata import Cellular_Automata
from scripts.level_generation.noise_map import Noise_Map
from scripts.engine.tilemap.tilemap import Tilemap
from scripts.engine.a_star import A_Star
import random
import os

import math
# TODO:  shrines, entrance and exit, keys 

# ENUMS for different tile types
floor = 0
wall = 1
lava = 2
door = 3
trap = 4
boss_room = 5

class Dungeon_Generator():
    def __init__(self, game) -> None:
        self.game = game
        self.player_spawn = (0, 0)
        self.cellular_automata = Cellular_Automata()
        self.tile_size = 32
        self.tilemap = Tilemap(self, tile_size=self.tile_size)
        self.a_star = A_Star()
        # TODO: IMPLEMENT MORE TRAPS AND ADD THEM HERE
        self.traps = ['spike_trap', 'spike_poison_trap', 'Pit_trap']
        self.noise_map = Noise_Map()
        
        self.torches = []



    # Customise the internal map structure
    def Generate_Map(self):
        self.Update_Load_Menu(1)

        self.tilemap.Clear_Tilemap()
        self.cellular_automata.Create_Map()
        self.Update_Load_Menu(2)

        self.Spawn_Lakes(7, floor, lava)

        
        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

        self.Player_Spawn()
        self.a_star.Set_Map('custom')
        self.Spawn_Traps(1)
        self.Update_Load_Menu(3)

        # Spawn more loot rooms in lower levels of dungeon
        # TODO: PROPER LEVEL SYSTEM
        temp_level = 5
        if not self.Spawn_Loot_Room(temp_level):
            self.Generate_Map()
            return        
        self.Update_Load_Menu(4)

        self.Spawn_Boss_Room()

        self.a_star.Setup_Custom_Map(self.cellular_automata.map, self.cellular_automata.size_x, self.cellular_automata.size_y)

        self.a_star.Set_Map('custom')

        # Call itself recursively and generate a new map if it fails to spawn enemies
        if not self.Enemy_Spawner():
            self.Generate_Map()
            return
        self.Update_Load_Menu(5)
        
        self.Spawn_Chest(2)

        self.Level_Structure()
    

        self.Update_Load_Menu(6)
        self.tilemap.save('data/maps/0.json')

    def Update_Load_Menu(self, value):
        self.game.menu_handler.Loading_Menu_Update(value)



    # Spawn trap if density is greater than spawn trap, goes from 0 to 100
    def Spawn_Traps(self, density):
        for y in range(1, self.cellular_automata.size_y - 1):
            for x in range(1, self.cellular_automata.size_x - 1):
                if self.cellular_automata.map[x][y] != floor:
                    continue
                spawn_trap = random.randint(0, 100)
                if spawn_trap < density:
                    self.cellular_automata.map[x][y] = trap

    
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
                    if self.cellular_automata.map[x][y] == floor:
                        spawn_loot = random.randint(0, 3)
                        if spawn_loot == 1:
                            self.tilemap.offgrid_tiles.append({"type": 'gold', "variant": 0, "pos": [x * self.tile_size, y * self.tile_size]})

                    i += 1
                j += 1

    def Level_Structure(self):
        for j in range(self.cellular_automata.size_y):
            for i in range(self.cellular_automata.size_x):
                if self.cellular_automata.map[i][j] == wall: 
                    if not self.Wall_Checker(i, j):
                        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_bottom', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}


                elif self.cellular_automata.map[i][j] == floor: # Floor
                    self.Floor_Checker(i, j)
                elif self.cellular_automata.map[i][j] == lava:
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Lava_env', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif self.cellular_automata.map[i][j] == door:
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'Door_Basic', 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                elif self.cellular_automata.map[i][j] == trap:
                    trap_type = random.randint(0, 2)
                    self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': self.traps[trap_type], 'variant': 0, 'pos': (i, j), 'active': 0, 'light': 0}
                    

    # Spawns torches based on density, it then checks distance to nearest torch to prevent overlap
    # Higher density = More torches
    def Torch_Spawner(self, i, j, density):
        spawn_torch = random.randint(0, density)
        if spawn_torch == 1:
            for torch in self.torches:
                distance = math.sqrt((i - torch[0]) ** 2 + (j - torch[1]) ** 2)
                if distance < 8:
                    return
            self.torches.append((i, j))
            self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [i * self.tile_size, j * self.tile_size]})

    def Floor_Checker(self, i, j):
        random_variant = random.randint(0, 10)
        self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'floor', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
        self.Torch_Spawner(i, j, 20)


    def Spawn_Boss_Room(self):
        fail = 0
        start_x = 0
        start_y = 0
        radius = 0

        while fail < 10:
            radius = random.randint(6, 8)
            start_x = random.randint(radius * 2, self.cellular_automata.size_x - radius * 2)
            start_y = random.randint(radius * 2, self.cellular_automata.size_y - radius * 2)
            
            path = []
            self.a_star.a_star_search(path, [start_x, start_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            if  path:
                break

            fail += 1


        self.Room_Structure_Circle(start_x, start_y, radius)
        # self.tilemap.offgrid_tiles.append({"type": 'Shrine', "variant": 0, "pos": [start_x * self.tile_size, start_y * self.tile_size]})
        self.tilemap.offgrid_tiles.append({"type": 'Boss_Room', "variant": 0, "pos": [start_x * self.tile_size, start_y * self.tile_size], "radius": radius})

        trap_number = random.randint(1, 5)
        i = 0
        while i < trap_number:
            pos_x = random.randint(start_x - radius + 1, start_x + radius - 2)
            pos_y = random.randint(start_y - radius + 1, start_y + radius - 2)
            
            distance_from_center = math.sqrt((pos_x - start_x) ** 2 + (pos_y - start_y) ** 2)
            if distance_from_center <= 2:
                continue
            self.cellular_automata.map[pos_x][pos_y] = trap
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

            
            self.Room_Structure_Rectangle(start_x, start_y, size_x, size_y)
            if not self.Generate_Doors_Room_Rectangle(start_x, start_y, size_x, size_y):
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
            if not self.cellular_automata.map[pos_x][pos_y] == floor:
                continue
            self.tilemap.offgrid_tiles.append({"type": item, "variant": 0, "pos": [pos_x * self.tile_size, pos_y * self.tile_size]})
            loot += 1

    


    def Generate_Doors_Room_Rectangle(self, start_x, start_y, size_x, size_y):
        door_array = [1, 2, 3, 4]
        # Randomize the array
        random.shuffle(door_array)

        path = []

        # Check if left side connects to player
        y_mid = start_y + size_y // 2
        x_mid = start_x + size_x // 2

        for i in range(4):
            if door_array[i] == 1: # Left wall
                self.a_star.a_star_search(path, [start_x - 1, y_mid], [self.player_spawn[0], self.player_spawn[1]], 'test')
                if not path:
                    continue
                
                self.cellular_automata.map[start_x][y_mid] = door
                return True

            elif door_array[i] == 2: # Right wall
                self.a_star.a_star_search(path, [start_x + size_x, y_mid], [self.player_spawn[0], self.player_spawn[1]], 'test')
                if not path:
                    continue
                self.cellular_automata.map[start_x + size_x - 1][y_mid] = door
                return True

            elif door_array[i] == door: # Top
                self.a_star.a_star_search(path, [x_mid, start_y - 1], [self.player_spawn[0], self.player_spawn[1]], 'test')
                if not path:
                    continue
                self.cellular_automata.map[x_mid][start_y] = door
                return True

            elif door_array[i] == 4: # Bottom
                self.a_star.a_star_search(path, [x_mid, start_y + size_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
                if not path:
                    continue
                self.cellular_automata.map[x_mid][start_y + size_y - 1] = door
                return True

        return False
        


    # Flatten the loot room and add walls to outside
    # 1 = Wall, 0 = Floor
    def Room_Structure_Rectangle(self, start_x, start_y, size_x, size_y):
        for y in range(start_y, start_y + size_y):
            for x in range(start_x, start_x + size_x):
                if y == start_y:
                    self.cellular_automata.map[x][y] = wall
                elif y == start_y + size_y - 1:
                    self.cellular_automata.map[x][y] = wall
                elif x == start_x:
                    self.cellular_automata.map[x][y] = wall
                elif x == start_x + size_x - 1:
                    self.cellular_automata.map[x][y] = wall
                else:
                    self.cellular_automata.map[x][y] = floor



    def Room_Structure_Circle(self, center_x, center_y, radius):
        door_array = [1, 2, 3, 4]
        # Randomize the array
        random.shuffle(door_array)

        for y in range(center_y - radius, center_y + radius + 1):
            for x in range(center_x - radius, center_x + radius + 1):
                # Calculate the distance from the center
                distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                if distance == radius:
                    self.Spawn_Door_Circle_Room(door_array[0], center_x, x, center_y, y)
                        

                elif distance <= radius:
                    # Floor inside the circle
                    self.cellular_automata.map[x][y] = floor
                elif distance <= radius + 1:
                    # Walls around the circular floor
                    self.cellular_automata.map[x][y] = wall
        



    def Spawn_Door_Circle_Room(self, spawn_door, center_x, x, center_y, y):
        # Check if door is being spawned on x or y axis
        
        if y == center_y: # x axis
            self.cellular_automata.map[x][y] = door
            
        elif x == center_x: # y axis
            self.cellular_automata.map[x][y] = door
            self.cellular_automata.map[x][y] = wall

        return

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



    def Wall_Checker(self, i, j):
        random_variant = random.randint(0, 3)
        # Handle Edge cases first to prevent crashes
        if i <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_left', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        elif i >= self.cellular_automata.size_x - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_right', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j <= 1:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_top', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        
        elif j >= self.cellular_automata.size_y - 2:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_top', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True
        


        if self.cellular_automata.map[i][j + 1] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_top', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True



        if self.Corner_Handling(i, j, random_variant):
            return True
        

        if self.cellular_automata.map[i + 1][j] != wall and self.cellular_automata.map[i - 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_middle', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True

        if self.cellular_automata.map[i + 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_left', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True


        if self.cellular_automata.map[i - 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_right', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
            return True




            
        return False
        
    def Corner_Handling(self, i, j, random_variant) -> bool:
        if not self.cellular_automata.map[i][j - 1] != wall:
            return False
        
        left_side = 0
        right_side = 1
        both_sides = 2
        if self.cellular_automata.map[i + 1][j] != wall and self.cellular_automata.map[i - 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_bottom_corner', 'variant': both_sides, 'pos': (i, j), 'active': 0, 'light': 0}

        elif self.cellular_automata.map[i + 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_bottom_corner', 'variant': right_side, 'pos': (i, j), 'active': 0, 'light': 0}

        elif self.cellular_automata.map[i - 1][j] != wall:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_bottom_corner', 'variant': left_side, 'pos': (i, j), 'active': 0, 'light': 0}

        else:
            self.tilemap.tilemap[str(i) + ';' + str(j)] = {'type': 'wall_bottom', 'variant': random_variant, 'pos': (i, j), 'active': 0, 'light': 0}
        return True
        
    
    def Player_Spawn(self):
        self.player_spawn = (20, 20)
        for y in range(self.player_spawn[1] - 5, self.player_spawn[1] + 5):
            for x in range(self.player_spawn[0] - 5, self.player_spawn[0] + 5):
                random_variant = random.randint(0, 10)

                self.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'floor', 'variant': random_variant, 'pos': (x, y), 'active': 0, 'light': 0}
        
        self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 0, 'pos': (self.player_spawn[0] * self.tile_size, self.player_spawn[1] * self.tile_size)})

        # self.tilemap.offgrid_tiles.append({"type": "torch", "variant": 0, "pos": [self.player_spawn[0] * self.tile_size - 50, self.player_spawn[1] * self.tile_size]})
        self.tilemap.offgrid_tiles.append({"type": "Chest", "variant": 0, "pos": [self.player_spawn[0] * self.tile_size, self.player_spawn[1] * self.tile_size]})



    def Enemy_Spawner(self):
        spawners = 0
        fails = 0
        path = []
        while spawners < 20:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] == wall:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'spawners', 'variant': 1, 'pos': (spawner_x * self.tile_size, spawner_y * self.tile_size)})
                spawners += 1
            else:
                fails += 1

            if fails > 20:
                return False
        
        return True

    def Spawn_Chest(self, level):
        loot_amount = random.randint(10 + level, 20 + level)
        loot = 0 
        path = []
        while loot < loot_amount:
            spawner_x = random.randint(1, self.cellular_automata.size_x - 2)
            spawner_y = random.randint(1, self.cellular_automata.size_y - 2)
            if self.cellular_automata.map[spawner_x][spawner_y] != floor:
                continue
            self.a_star.a_star_search(path, [spawner_x, spawner_y], [self.player_spawn[0], self.player_spawn[1]], 'test')
            
            if path:
                self.tilemap.offgrid_tiles.append({'type': 'Chest', 'variant': 0, 'pos': (spawner_x * self.tile_size, spawner_y * self.tile_size)})
                loot += 1


    def Delete_Map_File(self, file_path):

        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
  