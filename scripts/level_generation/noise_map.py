import random

class Noise_Map():
    def __init__(self) -> None:
        pass

    def Generate_Map(self, density, map, size_x, size_y):
        for y in range(size_y):
            for x in range(size_x):
                value = random.randint(0, 100)
                if value > density:
                    map[x][y] = 0  # Floor
                else:
                    map[x][y] = 1  # Wall

    

    def Create_Noise_Map(self, size_x, size_y):
        self.map = [[0 for _ in range(size_y)] for _ in range(size_x)]
        self.Generate_Map(56, self.map, size_x, size_y)
        return self.map