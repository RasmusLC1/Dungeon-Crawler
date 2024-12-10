from scripts.entities.effects.effect import Effect
import random

# Resistance to freeze
class Frozen_Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "frozen_resistance", 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        if self.cooldown:
            self.cooldown -= 1
        else:
            self.effect -= 1
            self.cooldown = random.randint(200, 250)
            return True
        
        return False
    