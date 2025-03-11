from scripts.entities.moving_entities.effects.effect import Effect
import random

# Resistance to freeze
class Frozen_Resistance(Effect):
    def __init__(self, entity):
        description = 'Prevents freezing'
        super().__init__(entity, "frozen_resistance", 0, 0, (200, 250), description)

    