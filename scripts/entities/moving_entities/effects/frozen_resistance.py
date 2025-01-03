from scripts.entities.moving_entities.effects.effect import Effect
import random

# Resistance to freeze
class Frozen_Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "frozen_resistance", 0, 0, (200, 250))

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        
        return self.Update_Cooldown()
    