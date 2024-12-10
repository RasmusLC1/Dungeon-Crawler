from scripts.entities.effects.effect import Effect
import pygame
import random

# Increase entity's strength
class Strength(Effect):
    def __init__(self, entity):
        super().__init__(entity, "strength", 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects_poisoned.effect:
            return False
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if self.cooldown:
            self.cooldown -= 1

        if not self.effect or self.entity.effects_poisoned.effect:
            return False
        
        self.entity.strength = min(20, self.entity.strength * 2)

        if not self.cooldown:
            self.effect -= 1
            self.cooldown = random.randint(130, 160)
            return True
        
        return False
    