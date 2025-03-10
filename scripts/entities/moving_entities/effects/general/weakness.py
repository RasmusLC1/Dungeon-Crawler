from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Increase entity's strength
class Weakness(Effect):
    def __init__(self, entity):
        description = 'Decreases\nmelee damage'

        super().__init__(entity, "weakness", 0, 0, (130, 160), description)

    
    #set Fire effect
    def Set_Effect(self, effect_time, permanent = False):
        # Double the effect if poisoned
        if self.entity.effects.poison.effect:
            effect_time *= 2
        return super().Set_Effect(effect_time, permanent)


    def Update_Effect(self):

        if not self.effect:
            return False
        
        self.entity.strength = min(20, self.entity.strength // 2)

        return self.Update_Cooldown()
    