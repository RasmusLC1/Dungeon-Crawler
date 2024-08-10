from scripts.traps.trap import Trap

import random
import math
import pygame

class Top_Push_Trap(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)

    def Update(self, entity):
        # Trigger trap animation and snare
        if self.rect().colliderect(entity.rect()) and self.animation < 5:
            if entity.type == 'player':
                if entity.dashing:
                    return
            entity.Push(0, self.animation*6)
            if self.animation == 0:
                self.animation += 1

    def Animation_Update(self):    
        # Resetting Trap
        if self.Cooldown > 0:
            self.Cooldown -= 1
        if self.animation > 0 and self.Cooldown == 0 :
            self.animation += 1
            self.Cooldown = 10
            if self.animation > 9:
                self.animation = 0

        



            