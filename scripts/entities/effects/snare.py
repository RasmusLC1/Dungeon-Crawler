from scripts.entities.effects.effect import Effect
import random


class Snare(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'snare', 0, 0)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.snared = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.cooldown:
            self.cooldown -= 1
        else:
            self.effect -= 1
            self.cooldown = random.randint(50, 70)
        
        self.entity.frame_movement = (0, 0)
        return True