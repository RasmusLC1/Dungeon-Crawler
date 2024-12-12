from scripts.entities.effects.effect import Effect
import random

# Long lasting damage and slowdown
class Poison(Effect):
    def __init__(self, entity):
        super().__init__(entity, "poison", 2, 30, (50, 70))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poison_resistance.effect:
            return False
        
        return super().Set_Effect(effect_time)

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.poison_resistance.effect:
            self.effect = 0
            self.cooldown = 0
            return False
        

        if self.Update_Cooldown():
            self.entity.Damage_Taken(self.effect)

        self.entity.effects.Set_Effect("slow_down", self.effect)
        self.Effect_Animation_Cooldown()
        return True
    
    