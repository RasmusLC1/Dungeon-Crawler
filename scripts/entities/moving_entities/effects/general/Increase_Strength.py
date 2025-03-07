from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Increase entity's strength
class Increase_Strength(Effect):
    def __init__(self, entity):
        description = 'Increases\nmelee damage'

        super().__init__(entity, "increase_strength", 0, 0, (130, 160), description)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poison.effect:
            return False
        return super().Set_Effect(effect_time)


    def Update_Effect(self):

        if not self.effect or self.entity.effects.poison.effect:
            return False
        
        self.entity.strength = min(20, self.entity.strength * 2)

        return self.Update_Cooldown()
    