from scripts.entities.effects.effect import Effect
import pygame
import random


class Fire_Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "fire_resistance", 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.effect_max:
            return False
        
        self.fire = 0
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        if self.cooldown:
            self.cooldown -= 1
        else:
            self.effect -= 1
            self.cooldown = random.randint(200, 250)
            return True
        
        return False