from scripts.traps.trap import Trap

import random
import math
import pygame

class Lava(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 2)

    def Update(self, entity):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(entity.rect()):
            entity.Slow_Down(3)
            if self.Cooldown == 0:
                if entity.type == 'player':
                    if entity.dashing:
                        return
                entity.Set_On_Fire(5)
                entity.Damage_Taken(5)
                self.Cooldown = 20

    def Animation_Update(self):
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 2:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)