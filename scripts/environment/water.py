from scripts.traps.trap import Trap

import random
import math
import pygame

class Water(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size)
        self.animation = random.randint(0, 2)
        self.type = type

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            if self.type == 'shallow_water':
                self.game.player.Slow_Down(2)
            elif self.type == 'medium_water':
                self.game.player.Slow_Down(4)
            elif self.type == 'deep_water':
                self.game.player.Slow_Down(8)


        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 2:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)

    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets[self.type][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))