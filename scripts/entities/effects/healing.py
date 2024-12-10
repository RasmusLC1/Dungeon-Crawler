from scripts.entities.effects.effect import Effect
import random

# Heal entity
class Healing(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'healing', 0, 0)

    
    def Set_Effect(self, effect_time):
        if self.entity.health >= self.entity.max_health:
            return False     
        self.entity.health = min(self.entity.max_health, self.entity.health + effect_time)
        return True
