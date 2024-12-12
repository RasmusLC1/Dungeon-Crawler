from scripts.entities.effects.effect import Effect
import pygame
import random

# Make entity invisible and prevent enemy aggro
class Invisibility(Effect):
    def __init__(self, entity):
        super().__init__(entity, "invisibility", 0, 0, (130, 160))

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.entity.Set_Alpha_Value(max(0, 110 - self.effect * 10))

        return self.Update_Cooldown()
    