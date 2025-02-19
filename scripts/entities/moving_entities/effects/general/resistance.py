from scripts.entities.moving_entities.effects.effect import Effect

# Reduces damage that entity takes, cannot fully cancel damage though
class Resistance(Effect):
    def __init__(self, entity):
        description = 'General damage\nresistance'
        super().__init__(entity, "resistance", 0, 0, (200, 250), description)
        self.entity_health_holder = entity.health

    
    def Update_Effect(self):
        if not self.effect:
            return False
        
        self.Update_Cooldown()
        
        if self.entity.health < self.entity_health_holder:
            self.entity.health = min(self.entity.health + self.effect, self.entity_health_holder - 2)
        
        self.entity_health_holder = self.entity.health
        return False