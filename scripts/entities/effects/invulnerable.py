from scripts.entities.effects.effect import Effect
import random

# Immune to damage but cannot move
class Invulnerable(Effect):
    def __init__(self, entity):
        super().__init__(entity, "invulnerable", 0, 0)
        self.entity_health_holder = entity.health

    
    #set Fire effect
    def Set_Effect(self, effect_time):        
        self.effect = min(self.effect_max, self.effect + effect_time)
        self.entity_health_holder = self.entity.health
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        
        if self.cooldown:
            self.cooldown -= 1

        else:
            self.cooldown = random.randint(50, 80)
            self.entity.effects.Set_Effect("snare", self.cooldown)
            self.effect -= 1
            if self.effect <= 0:
                self.entity.effects.Set_Effect("snare", -10)

        
        if self.entity.health < self.entity_health_holder:
            self.entity.health = self.entity_health_holder
        
        self.entity_health_holder = self.entity.health
        return False