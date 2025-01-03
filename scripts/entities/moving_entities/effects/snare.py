from scripts.entities.moving_entities.effects.effect import Effect
import random

# Set entity movement speed to zero
class Snare(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'snare', 0, 0, (50, 70))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.effect = max(0, min(effect_time + self.effect, 10))
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