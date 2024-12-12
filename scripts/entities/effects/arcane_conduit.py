from scripts.entities.effects.effect import Effect
import random

# Reduce the cost runes
class Arcane_Conduit(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'arcane_conduit', 0, 0, (200, 250))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.effect = effect_time
        return True
    
    