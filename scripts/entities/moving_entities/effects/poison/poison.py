from scripts.entities.moving_entities.effects.effect import Effect
import random

# Long lasting damage and weakens the entity
class Poison(Effect):
    def __init__(self, entity):
        description = 'Damage over time, reduces strength'
        super().__init__(entity, "poison", 2, 30, (50, 70), description)
        self.strength_holder = self.entity.strength

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.poison_resistance.effect:
            return False
        
        return super().Set_Effect(effect_time)

    
    def Update_Effect(self):
        if not self.effect:
            return False
        self.entity.Set_Strength(self.strength_holder // 2)

        if self.entity.effects.poison_resistance.effect:
            self.effect = 0
            self.cooldown = 0
            return False
        

        if self.Update_Cooldown():
            self.entity.Damage_Taken(self.effect)

        self.Effect_Animation_Cooldown()
        return True
    
    