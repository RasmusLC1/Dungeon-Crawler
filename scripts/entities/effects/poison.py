from scripts.entities.effects.effect import Effect
import random

# Long lasting damage and slowdown
class Poison(Effect):
    def __init__(self, entity):
        super().__init__(entity, "poison", 2, 30)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poison_resistance.effect:
            return False
        self.effect =  max(random.randint(2, effect_time), self.effect)
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.poison_resistance.effect:
            self.effect = 0
            self.cooldown = 0
            return False
        

        if self.cooldown:
            self.cooldown -= 1
        else:
            # Handle damage when effect updates
            self.entity.Damage_Taken(self.effect)
            self.cooldown = random.randint(50, 70)
            self.effect -= 1

        self.entity.effects.Set_Effect("slow_down", self.effect)
        self.Effect_Animation_Cooldown()
        return True
    
    