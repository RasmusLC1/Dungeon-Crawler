from scripts.entities.moving_entities.effects.effect import Effect
import random

# Long lasting damage and weakens the entity
class Poison(Effect):
    def __init__(self, entity):
        description = 'poison Damage over time,\nreduces increase_strength'
        super().__init__(entity, "poison", 2, 30, (50, 70), description)
        self.strength_holder = self.entity.strength

    
    #set Fire effect
    def Set_Effect(self, effect_time, permanent = False):
        if self.entity.effects.poison_resistance.effect:
            return False
        
        if not super().Set_Effect(effect_time, permanent):
            return False
        
        self.entity.Set_Healing_Enabled(False)
        return True

    
    def Remove_Effect(self, reduce_permanent=0):
        if not super().Remove_Effect(reduce_permanent):
            return False
        
        self.entity.Set_Healing_Enabled(True)
        return True
        

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
    
    