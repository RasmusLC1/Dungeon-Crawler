from scripts.traps.trap import Trap
import random
import math
import pygame


class Bear_Trap(Trap):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.animation_max = 3

    def Update(self, entity):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(entity.rect()) and self.Cooldown == 0:
            if entity.effects.invulnerable.effect:
                return
                
            entity.Damage_Taken(2)
            entity.Set_Effect('snare', 100)
            self.Cooldown = 300
            
        if self.Cooldown:
            if not self.animation_cooldown:
                self.animation = min(self.animation_max, self.animation + 1)
                self.animation_cooldown = 10

            self.animation_cooldown -= 1
        
        if self.Cooldown < 200:
            self.animation = 0

    def rect(self):
        return pygame.Rect(self.pos[0]+10, self.pos[1]+10, self.size[0], self.size[1])
    