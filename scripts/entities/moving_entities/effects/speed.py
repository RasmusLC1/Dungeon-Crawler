from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Increase entity speed
class Speed(Effect):
    def __init__(self, entity):
        super().__init__(entity, "speed", 0, 0, (130, 160))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.frozen.effect:
            return False
        return super().Set_Effect(effect_time)

    def Update_Effect(self):

        if not self.effect or self.entity.effects.frozen.effect:
            return False

        self.entity.max_speed = min(14, self.entity.max_speed * 2)
        
        return self.Update_Cooldown()