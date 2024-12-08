from scripts.entities.effects.effect import Effect
import pygame
import random


class Invisibility(Effect):
    def __init__(self, entity):
        super().__init__(entity, "invisibility", 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.invisibility_max:
            return False
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.entity.Set_Alpha_Value(max(0, 110 - self.effect * 10))

        if self.cooldown:
            self.cooldown -= 1
        else:
            self.effect -= 1
            self.cooldown = random.randint(130, 160)
            return True
        return False
    