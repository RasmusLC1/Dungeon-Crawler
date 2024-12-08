from scripts.entities.effects.effect import Effect
import random


class Wet(Effect):
    def __init__(self, entity):
        super().__init__(entity, "wet", 2, 20)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.fire:
            self.fire = 0
        if self.entity.effects.frozen:
            self.entity.effects.frozen.Decrease_Effect()
        self.effect = max(2, effect_time)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.fire.effect:
            self.entity.effects.fire.Remove_Effect()
            
        elif self.cooldown:
            self.cooldown -= 1

        else:
            self.cooldown = random.randint(160, 200)
            self.effect -= 1
            return True
        
        self.Effect_Animation_Cooldown()
        return False
    