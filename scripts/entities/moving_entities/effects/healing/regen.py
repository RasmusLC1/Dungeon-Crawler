from scripts.entities.moving_entities.effects.effect import Effect
import random
from scripts.engine.assets.keys import keys

# Regen health over time each time effect is triggered
class Regen(Effect):
    def __init__(self, entity):
        description = 'Heals over time.\nBlocked by poison'
        super().__init__(entity, "regen", 5, 30, (80, 100), description)

    
    #set Fire effect
    def Set_Effect(self, effect_time, permanent = False):
        if not self.entity.healing_enabled:
            return False
        
        return super().Set_Effect(effect_time, permanent)

    
    def Update_Effect(self):
        if not super().Update_Effect():
            return False
                  
        if self.entity.effects.poison.effect:
            return False
        
        self.entity.effects.Set_Effect("healing", random.randint(3, 5))
        self.Effect_Animation_Cooldown()
        return True
