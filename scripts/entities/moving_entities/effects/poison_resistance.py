from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Resist poison
class Poison_Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "poison_resistance", 0, 0, (200, 250))

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.Update_Cooldown()
        
        return False