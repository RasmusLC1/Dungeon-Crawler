from scripts.level_generation.noise_map import Noise_Map
import random

class Cellular_Automata():
    def __init__(self) -> None:
        self.size_x = 0 
        self.size_y = 0
        
        
    def Create_Map(self):
        self.map = self.Create_Level()
        # self.Save_Map_To_File('test_map_1.txt', self.map)
        floor = 0
        wall = 1
        self.Refine_Level(floor, wall, self.size_x, self.size_y, 5, self.map)
        self.Close_Borders(0, 0, self.size_x, self.size_y)
        self.Save_Map_To_File('test_map.txt', self.map)


    def Create_Level(self) -> None:
        self.size_x = 70 + random.randint(-20, 20)
        self.size_y = 70 + random.randint(-20, 20)
        noise_map = Noise_Map()
        return noise_map.Create_Noise_Map(self.size_x, self.size_y)    
    
    def Within_Map_Bounds(self, x, y, size_x, size_y) -> bool:
        return 0 <= x < size_x and 0 <= y < size_y

    def Refine_Level(self, value_1, value_2, size_x, size_y, iterations, map):
        for i in range(iterations):
            temp_map = [row.copy() for row in map]

            for j in range(size_y):
                for i in range(size_x):
                    neighbour_wall_count = 0
                    for y in range(j-1, j+2):
                        for x in range(i-1, i+2):
                            if self.Within_Map_Bounds(x, y, size_x, size_y):
                                if y != j or x != i:
                                    if temp_map[x][y] == value_2:
                                        neighbour_wall_count += 1
                            else:
                                neighbour_wall_count += 1

                    if neighbour_wall_count > 4:
                        map[i][j] = value_2
                    else:
                        map[i][j] = value_1

                
    def Generate_Treasure_Rooms(self):
        for i in range(5):
            max_size = 15
            start_x = random.randint(0, self.size_x - max_size - 5)
            start_y = random.randint(0, self.size_y - max_size - 5)
            width = start_x + random.randint(7, max_size)
            height = start_y + random.randint(7, max_size)

            for j in range(start_x, height -1):
                for i in range(start_y, width -1):
                    self.map[i][j] = 0

            
            self.Close_Borders(start_x, start_y, width, height)

            center_x = width // 2
            center_y = height // 2

            self.map[center_x][center_y] = 2

            # Create door
            for i in range(3):
                self.map[center_x + i][0] = 0
                self.map[center_x + i][height - 1] = 0
                self.map[0][center_y + i] = 0
                self.map[width - 1][center_y + i] = 0


        


    def Close_Borders(self, start_x, start_y, width, height):
        
        for j in range(height):
            self.map[start_x][j] = 1
        
        for j in range(height):
            self.map[width - 1][j] = 1

        for i in range(width):
            self.map[i][start_y] = 1
        
        for i in range(width):
            self.map[i][height - 1] = 1
                    

    def Save_Map_To_File(self, file_path, map):
        with open(file_path, 'w') as file:
            for y in range(self.size_y):
                for x in range(self.size_x):
                    file.write(str(map[x][y]) + ' ')
                file.write('\n')  # New line after each row
