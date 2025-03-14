from scripts.entities.moving_entities.effects.effect import Effect
import random

# Increases damage when health when low
class Temptress_Embrace(Effect):
    def __init__(self, entity):
        description = 'Damage scales\nwith health lost'
        super().__init__(entity, 'temptress_embrace', 0, 0, (120, 160), description)

    def Update_Effect(self):
        if not self.effect:
            return False
        
        if self.entity.effects.poison.effect:
            return True
        
        self.Calculate_Strength()
        self.Update_Cooldown()
        return True


    # Scale the player's strength with health lost
    def Calculate_Strength(self):
        normalised_health = self.Normalise_Health()
        self.entity.strength = min(20, self.entity.strength + normalised_health)



    def Normalise_Health(self):
        entity = self.entity

        # Invert scaling: 10 (worst) → 1 (best), subtract 2 to start scaling slower
        normalised_health = min(12, round(12 * (1 - (entity.health - 1) / (entity.max_health - 1)))) - 2

        return normalised_health