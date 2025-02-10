import random
from scripts.level_generation.dungeon_enum_keys import *


class Rectangle_Room():
    @staticmethod
    # Flatten the loot room and add walls to outside
    # 1 = Wall, 0 = Floor
    def Room_Structure_Rectangle(map, start_x, start_y, size_x, size_y, a_star):
        for y in range(start_y, start_y + size_y):
            for x in range(start_x, start_x + size_x):
                if y == start_y:
                    map[x][y] = WALL
                elif y == start_y + size_y - 1:
                    map[x][y] = WALL
                elif x == start_x:
                    map[x][y] = WALL
                elif x == start_x + size_x - 1:
                    map[x][y] = WALL
                else:
                    map[x][y] = FLOOR

        return Rectangle_Room.Generate_Doors_Room_Rectangle(map, start_x, start_y, size_x, size_y, a_star)
    
    @staticmethod
    def Generate_Doors_Room_Rectangle(map, start_x, start_y, size_x, size_y, a_star):
        door_array = [1, 2, 3, 4]
        # Randomize the array
        random.shuffle(door_array)

        path = []

        # Check if left side connects to player
        y_mid = start_y + size_y // 2
        x_mid = start_x + size_x // 2

        for i in range(4):
            if door_array[i] == 1: # Left wall
                path = a_star(start_x - 1, y_mid)
                if not path:
                    continue
                
                map[start_x][y_mid] = DOOR
                return True

            elif door_array[i] == 2: # Right wall
                path = a_star(start_x + size_x, y_mid)
                if not path:
                    continue
                map[start_x + size_x - 1][y_mid] = DOOR
                return True

            elif door_array[i] == DOOR: # Top
                path = a_star(x_mid, start_y - 1)
                if not path:
                    continue
                map[x_mid][start_y] = DOOR
                return True

            elif door_array[i] == 4: # Bottom
                path = a_star(x_mid, start_y + size_y)
                if not path:
                    continue
                map[x_mid][start_y + size_y - 1] = DOOR
                return True

        return False