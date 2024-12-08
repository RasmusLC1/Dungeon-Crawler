from scripts.entities.effects.effect import Effect
import pygame
import random


class Speed(Effect):
    def __init__(self, entity):
        super().__init__(entity, "speed", 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects_frozen.effect:
            return False
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):

        if not self.effect or self.entity.effects.frozen.effect:
            return False
        
        if self.cooldown:
            self.cooldown -= 1

        self.entity.max_speed = min(14, self.entity.max_speed * 2)
            
        if not self.cooldown:
            self.effect -= 1
            self.cooldown = random.randint(130, 160)
            return True
        
        return False