import random

class Noise_Map():
    def __init__(self) -> None:
        pass
    
    # Takes from starting x/y to the given size and inserts 2 values into the table
    def Generate_Map(self, floor_density, map, floor_val, wall_val, size_x, size_y):
        for y in range(size_y):
            for x in range(size_x):
                value = random.randint(0, 100)
                if value > floor_density:
                    map[x][y] = floor_val  # Floor
                else:
                    map[x][y] = wall_val  # Wall

    

    def Create_Noise_Map(self, size_x, size_y):
        self.map = [[0 for _ in range(size_y)] for _ in range(size_x)]
        floor = 0
        wall = 1
        density = 57
        self.Generate_Map(density, self.map, floor, wall, size_x, size_y)
        return self.map