import math
import pygame

class Helper_Functions():
    def __init__(self) -> None:
        pass


    def Abs_Distance_Float(origin, destination):
        return abs(math.sqrt((destination[0] - origin[0]) ** 2 + (destination[1] - origin[1]) ** 2))
    
    def Abs_Distance_Tuple(origin, destination):
        dx = abs(destination[0] - origin[0])
        dy = abs(destination[1] - origin[1])
        return dx, dy
    
    def Direction_Vector(direction):
        return pygame.math.Vector2(direction[0], direction[1])
    
    def Set_Direction_Vector(origin, target):
        return pygame.math.Vector2(target[0] - origin[0], target[1] - origin[1])