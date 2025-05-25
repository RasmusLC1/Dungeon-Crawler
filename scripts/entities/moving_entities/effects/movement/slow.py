from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.assets.keys import keys

# Reduce the entity speed
class Slow(Effect):
    def __init__(self, entity):
        description = 'Reduces speed'
        super().__init__(entity, keys.slow, 0, 0, (5,10), description)

    
    #set Fire effect
    def Set_Effect(self, effect_time, permanent = True):
        return super().Set_Effect(effect_time, True)

    def Update_Effect(self):

        if not self.effect:
            return False

        try:
            self.entity.max_speed = max(0.1, self.entity.max_speed / self.effect)
        except ZeroDivisionError as e:
            print(f"SLOWDOWN: {e}", self.entity.max_speed, self.effect)
        
        self.Update_Cooldown()

        return True
    
