from scripts.entities.effects.effect import Effect
import random


class Frozen(Effect):
    def __init__(self, entity):
        super().__init__(entity, "frozen", 2, 30)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.fire.effect or self.entity.effects.freeze_resistance.effect:
            return False
        
        if self.entity.effects.wet.effect:
            effect_time *= 2
            self.wet = 0
        self.effect = max(3, effect_time)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.freeze_resistance.effect:
            self.effect = 0
            self.cooldown = 0
            return False
        
        if self.cooldown:
            self.cooldown -= 1

        else:
            self.cooldown = random.randint(160, 200)
            self.effect -= 1
        
        self.entity.effects.Set_Effect("slow_down", self.effect)

        self.Effect_Animation_Cooldown()
        return False