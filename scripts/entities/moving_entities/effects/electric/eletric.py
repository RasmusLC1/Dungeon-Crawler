from scripts.entities.moving_entities.effects.effect import Effect
import random

# 
class Electric(Effect):
    def __init__(self, entity):
        description = 'Damage and snare,\nspreads to nearby\nenemy, increased\nby wet'
        super().__init__(entity, 'electric', 5, 10, (70, 100), description)

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.electric_resistance.effect:
            return False
        
        if self.entity.effects.wet.effect:
            effect_time *= 2

        self.entity.Damage_Taken(effect_time)
            
        return super().Set_Effect(effect_time)
    
    def Update_Effect(self):
        if not self.effect:
            return False
        

        if self.entity.effects.electric_resistance.effect:
            self.Remove_Effect()
            return False
        
        if self.Update_Cooldown():
            effect = max(self.effect - 1, 0)
            if not effect:
                return False
            for enemy in self.entity.nearby_enemies:
                if enemy.Set_Effect(self.effect_type, effect):
                    self.entity.Set_Effect('electric_resistance', 0)
                    return True
                


        self.entity.frame_movement = (0, 0)
        self.Effect_Animation_Cooldown()
        return True
   
    