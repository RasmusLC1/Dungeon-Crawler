import random

class Noise_Map():
    def __init__(self, size_x, size_y) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.map = [[0 for _ in range(self.size_x)] for _ in range(self.size_y)]
        

    def Generate_Map(self, density):
        for y in range(self.size_y):
            for x in range(self.size_x):
                value = random.randint(0, 100)
                if value > density:
                    self.map[y][x] = 0  # Floor
                else:
                    self.map[y][x] = 1  # Wall

    

    def Create_Noise_Map(self):
        self.Generate_Map(56)
        return self.map