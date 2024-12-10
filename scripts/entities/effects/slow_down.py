from scripts.entities.effects.effect import Effect
import random


class Slow_Down(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'slow_down', 0, 0)

    
    def Set_Effect(self, effect):
        if not effect:
            return
        try:
            self.entity.max_speed = max(0.1, self.entity.max_speed / effect)
        except ZeroDivisionError as e:
            print(f"SLOWDOWN: {e}", self.entity.max_speed, effect)