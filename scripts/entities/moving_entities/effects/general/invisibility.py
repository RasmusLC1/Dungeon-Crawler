from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Make entity invisible and prevent enemy aggro
class Invisibility(Effect):
    def __init__(self, entity):
        description = 'Invisible to\nother entities'
        super().__init__(entity, "invisibility", 0, 0, (130, 160), description)

    # TODO: NOT WORKING, FUNCTIONAL BUILD AT 10th february 2025
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.entity.Set_Active(max(0, 110 - self.effect * 10))

        return self.Update_Cooldown()
    