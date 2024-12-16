from scripts.entities.effects.effect import Effect
import pygame
import random

# Reduce fire damage
class Electric_Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "electrioc_resistance", 0, 0, (200, 250))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.effect_max:
            return False
        
        return super().Set_Effect(effect_time)

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.Update_Cooldown()
        
        return True