from scripts.entities.effects.effect import Effect
import random

# Don't generate sound and clatter
class Thorns(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'thorns', 0, 0)
        self.type = 'slash'

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, self.effect_max)
        return True
    
    def Set_Type(self, type):
        self.type = type
