from scripts.entities.moving_entities.effects.effect import Effect
import random

# Reduce the cost runes
class Magnet(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'magnet', 0, 0, (200, 250))
        self.effect_max = 4


    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.effect = min(effect_time, self.effect_max)
        return True
    
    def Update_Effect(self):
        self.entity.game.item_handler.Pick_Up_All_Nearby_Items(self.effect)
    

    
    