from scripts.entities.effects.effect import Effect
import random


class Regen(Effect):
    def __init__(self, entity):
        super().__init__(entity, "regen", 5, 30)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poisoned.effect:
            return False
        if self.effect >= self.effect_max:
            return False
        self.effect = min(effect_time + self.effect, 10)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.cooldown:
            self.cooldown -= 1
            return False
          
        if self.entity.effects.poisoned.effect:
            return False
        
        self.entity.effects.Set_Effect("healing", random.randint(3, 5))
        self.effect -= 1
        self.cooldown = random.randint(80, 100)
        self.Effect_Animation_Cooldown()
        return True
