from scripts.traps.trap import Trap

import random
import math
import pygame

class Ice(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 1)

    def Update(self, entity):
        if self.rect().colliderect(entity.rect()):

            if self.type == 'shallow_ice_env':
                entity.On_Ice(20)
            elif self.type == 'medium_ice_env':
                entity.On_Ice(20)
            elif self.type == 'deep_ice_env':
                entity.On_Ice(20)


    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets[self.type][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))