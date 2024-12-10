from scripts.entities.effects.effect import Effect
import random

# Increase souls from entity kills
class Hunger(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'hunger', 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.effect = effect_time
        return True
    
    