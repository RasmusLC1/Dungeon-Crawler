from scripts.entities.effects.effect import Effect
import random

# Take fire damage
class Fire(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'fire', 7, 20, (30, 50))

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        if self.entity.effects.wet.effect or self.entity.effects.fire_resistance.effect:
            return False
        if self.entity.effects.frozen.effect:
            self.entity.effects.frozen.Remove_Effect()
            
        return super().Set_Effect(effect_time)
    
    def Update_Effect(self):
        if not self.effect:
            return False
        

        if self.entity.effects.fire_resistance.effect or self.entity.effects.wet.effect:
            self.effect = 0
            self.cooldown = 0
            if self.entity.effects.wet.effect:
                self.entity.effects.wet.Decrease_Effect()
            return False
        
        if self.Update_Cooldown():
            damage = random.randint(1, 3)
            self.entity.Damage_Taken(damage)


        self.Effect_Animation_Cooldown()
        return True
   
    