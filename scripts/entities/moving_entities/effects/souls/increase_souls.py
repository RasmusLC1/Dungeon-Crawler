from scripts.entities.moving_entities.effects.effect import Effect
import random

# Heal entity
class Increase_Souls(Effect):
    def __init__(self, entity):
        description = 'Increase Souls once'
        super().__init__(entity, 'increase_souls', 0, 0, (0,0), description)

    
    def Set_Effect(self, effect_time, permanent = False):

        self.game.player.Increase_Souls(effect_time)
        return True
