from scripts.entities.effects.effect import Effect
import random


class Vampiric(Effect):
    def __init__(self, entity):
        super().__init__(entity, "vampiric", 0, 0)

    
    def Set_Effect(self, effect_time):
        self.effect = max(self.effect, max(10, effect_time))
        return True
    
    
    def Update_Effect(self):
        if not self.effect:
            return False

        if self.cooldown:
            self.cooldown -= 1

        else:
            self.cooldown = random.randint(150, 200)
            self.effect -= 1

        return False