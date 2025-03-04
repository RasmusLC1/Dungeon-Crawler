from scripts.entities.moving_entities.effects.effect import Effect
import random

# Low damage and slowdown of entity
class Frozen(Effect):
    def __init__(self, entity):
        description = 'Slows and damages\nover time'
        super().__init__(entity, "frozen", 2, 30, (160, 200), description)

    
    def Set_Effect(self, effect_time):
        if self.entity.effects.fire.effect or self.entity.effects.frozen_resistance.effect:
            return False
        
        if self.entity.effects.wet.effect:
            effect_time *= 2
            self.wet = 0

        return super().Set_Effect(effect_time)
    
    def Update_Effect(self):
        if not self.effect:
            return False
        

        if self.entity.effects.frozen_resistance.effect:
            self.effect = 0
            self.cooldown = 0
            return False
        
        if self.Update_Cooldown():
            damage = random.randint(1, 2)
            self.entity.Damage_Taken(damage)
        
        self.entity.effects.Set_Effect("slow_down", self.effect)

        self.Effect_Animation_Cooldown()

        return True