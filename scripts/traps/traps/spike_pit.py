from scripts.traps.trap import Trap

import random
import math
import pygame

class Spike_Pit(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)

    def Update(self, entity):
        # Resetting Trap
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if entity.category == 'item':
            return

        # Trigger trap animation and snare
        if self.rect().colliderect(entity.rect()) and not self.Cooldown:
            if entity.invincible:
                return
            entity.Damage_Taken(5)
            self.Cooldown = 100
            if not self.animation:
                self.animation = 1
                entity.Set_Effect('snare', 5)
            else:
                entity.Set_Effect('slow_down', 4)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0]-5, self.size[1]-5)
                    
