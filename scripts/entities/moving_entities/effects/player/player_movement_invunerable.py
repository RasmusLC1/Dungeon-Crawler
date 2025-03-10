from scripts.entities.moving_entities.effects.effect import Effect
import random

# Immune to damage but cannot move
class Player_Movement_Invunerable(Effect):
    def __init__(self, entity):
        super().__init__(entity, "invulnerable", 0, 0, (30, 50), '')
        self.entity_health_holder = entity.health

    
    #set Fire effect
    def Set_Effect(self, effect_time, permanent = False):
        if self.effect:
            return
        self.entity_health_holder = self.entity.health
        self.effect = effect_time
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.Update_Cooldown()

        
        if self.entity.health < self.entity_health_holder:
            self.entity.health = self.entity_health_holder
    
        self.entity_health_holder = self.entity.health
        return False