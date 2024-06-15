import random
import math
import pygame

class Trap:
    def __init__(self, game, pos, size, type):
        self.game = game
        self.pos = pos
        self.size = size
        self.Cooldown = 0
        self.animation = 0
        self.animation_cooldown = 0
        self.type = type

    def Update(self):
        pass

    def Animation_Update(self):
        pass

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets[self.type][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))