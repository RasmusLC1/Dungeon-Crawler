from scripts.entities.moving_entities.effects.effect import Effect
import random

# Heal entity when dealing damage
class Vampiric(Effect):
    def __init__(self, entity):
        super().__init__(entity, "vampiric", 0, 0, (150, 200))

    

    def Update_Effect(self):
        if not self.effect:
            return False

        self.Update_Cooldown()

        return False