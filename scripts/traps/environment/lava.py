from scripts.traps.trap import Trap

import random
import math
import pygame

class Lava(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation = random.randint(0, 2)
        self.light_level = 10
        self.light_source = self.game.light_handler.Add_Light(self.pos, self.light_level, self.tile)
        

    def Update(self, entity):
        if entity.category == 'item':
            return
        if self.rect().colliderect(entity.rect()):
            self.Cooldown = 20
            entity.Set_Effect('slow_down', 4)
            if entity.effects.invulnerable.effect:
                return
            if entity.effects.wet.effect:
                entity.effects.wet.Decrease_Effect()
            if not entity.Set_Effect('fire', 5):
                return
            entity.Damage_Taken(5)

    def Animation_Update(self):
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 2:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)