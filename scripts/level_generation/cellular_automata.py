from scripts.level_generation.noise_map import Noise_Map
import random

class Cellular_Automata():
    def __init__(self) -> None:
        self.size_x = 0 
        self.size_y = 0
        
        
    def Create_Map(self):
        self.size_x = 70 + random.randint(-20, 20)
        self.size_y = 70 + random.randint(-20, 20)
        self.map = self.Create_Level()
        self.Save_Map_To_File('test_map_1.txt', self.map)
        self.Refine_Level(5)
        self.Close_Borders()
        self.Save_Map_To_File('test_map.txt', self.map)


    def Create_Level(self) -> None:
        noise_map = Noise_Map(self.size_x, self.size_y)
        return noise_map.Create_Noise_Map()    
    
    def Within_Map_Bounds(self, x, y) -> bool:
        return 0 <= x < self.size_x and 0 <= y < self.size_y

    def Refine_Level(self, iterations):
        for i in range(iterations):
            temp_map = [row.copy() for row in self.map]

            for j in range(self.size_y):
                for i in range(self.size_x):
                    neighbour_wall_count = 0
                    for y in range(j-1, j+2):
                        for x in range(i-1, i+2):
                            if self.Within_Map_Bounds(x, y):
                                if y != j or x != i:
                                    if temp_map[y][x] == 1:
                                        neighbour_wall_count += 1
                            else:
                                neighbour_wall_count += 1

                    if neighbour_wall_count > 4:
                        self.map[j][i] = 1
                    else:
                        self.map[j][i] = 0
                
    
    def Close_Borders(self):
        
        for j in range(self.size_y):
            self.map[j][0] = 1
        
        for j in range(self.size_y):
            self.map[j][self.size_x - 1] = 1

        for i in range(self.size_x):
            self.map[0][i] = 1
        
        for i in range(self.size_x):
            self.map[self.size_y - 1][i] = 1


                    

    def Save_Map_To_File(self, file_path, map):
        with open(file_path, 'w') as file:
            for y in range(self.size_y):
                for x in range(self.size_x):
                    file.write(str(map[y][x]) + ' ')
                file.write('\n')  # New line after each row

