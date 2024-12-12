from scripts.entities.effects.effect import Effect
import random

# Increased damage to electricity but immune to fire
class Wet(Effect):
    def __init__(self, entity):
        super().__init__(entity, "wet", 2, 20, (200, 250))

    
    def Set_Effect(self, effect_time):
        if self.entity.effects.fire.effect:
            self.effects.fire.Remove_Effect()

        if self.entity.effects.frozen:
            self.entity.effects.frozen.Decrease_Effect()
            
        return super().Set_Effect(effect_time)

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.fire.effect:
            self.entity.effects.fire.Remove_Effect()
            
        self.Update_Cooldown()
        
        self.Effect_Animation_Cooldown()
        return False
    