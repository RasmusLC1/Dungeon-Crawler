from scripts.entities.moving_entities.effects.effect import Effect
import random

# Immune to damage but cannot move
class Invulnerable(Effect):
    def __init__(self, entity):
        description = 'Prevents all damage\nbut snare'
        super().__init__(entity, "invulnerable", 0, 0, (30, 50), description)
        self.entity_health_holder = entity.health

    
    #set Fire effect
    def Set_Effect(self, effect_time):
        self.entity_health_holder = self.entity.health
        self.entity.effects.Set_Effect("snare", self.cooldown)
        return super().Set_Effect(effect_time)
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.Update_Cooldown():
            if self.effect <= 0:
                self.entity.effects.Set_Effect("snare", -10)

        
        if self.entity.health < self.entity_health_holder:
            self.entity.health = self.entity_health_holder
    
        self.entity_health_holder = self.entity.health
        return False