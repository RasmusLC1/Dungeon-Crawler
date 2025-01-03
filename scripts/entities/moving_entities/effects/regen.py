from scripts.entities.moving_entities.effects.effect import Effect
import random

# Regen health over time each time effect is triggered
class Regen(Effect):
    def __init__(self, entity):
        super().__init__(entity, "regen", 5, 30, (80, 100))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poison.effect:
            return False
        
        return super().Set_Effect(effect_time)

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if not self.Update_Cooldown():
            return False
                  
        if self.entity.effects.poison.effect:
            return False
        
        self.entity.effects.Set_Effect("healing", random.randint(3, 5))
        self.Effect_Animation_Cooldown()
        return True
