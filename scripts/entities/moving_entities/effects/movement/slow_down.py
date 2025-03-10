from scripts.entities.moving_entities.effects.effect import Effect
import random

# Reduce the entity speed
class Slow_Down(Effect):
    def __init__(self, entity):
        description = 'Reduces speed'
        super().__init__(entity, 'slow_down', 0, 0, (0,0), description)

    
    def Set_Effect(self, effect_time, permanent = False):
        if not effect_time:
            return
        try:
            self.entity.max_speed = max(0.1, self.entity.max_speed / effect_time)
        except ZeroDivisionError as e:
            print(f"SLOWDOWN: {e}", self.entity.max_speed, effect_time)