from scripts.entities.moving_entities.effects.effect import Effect
import random

# Heal entity
class Healing(Effect):
    def __init__(self, entity):
        description = 'One time healing.\nBlocked by poison'
        super().__init__(entity, 'healing', 0, 0, (0,0), description)

    
    def Set_Effect(self, effect_time, permanent = False):
        if self.entity.effects.poison.effect:
            return False
        
        if self.entity.health >= self.entity.max_health:
            return False     
        self.entity.health = min(self.entity.max_health, self.entity.health + effect_time)
        return True
