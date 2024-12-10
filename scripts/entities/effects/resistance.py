from scripts.entities.effects.effect import Effect

# Reduces damage that entity takes, cannot fully cancel damage though
class Resistance(Effect):
    def __init__(self, entity):
        super().__init__(entity, "resistance", 0, 0)
        self.entity_health_holder = entity.health

    
    #set Fire effect
    def Set_Effect(self, effect_time):        
        self.effect = min(self.effect_max, self.effect + effect_time)
        self.entity_health_holder = self.entity.health
        return True
    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.health < self.entity_health_holder:
            self.entity.health = min(self.entity.health + self.effect, self.entity_health_holder - 2)
        
        self.entity_health_holder = self.entity.health
        return False