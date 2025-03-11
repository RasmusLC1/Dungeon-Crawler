from scripts.entities.moving_entities.effects.effect import Effect
import random

# Don't generate sound and clatter
class Silence(Effect):
    def __init__(self, entity):
        description = 'Prevents Clatter\ngeneration'

        super().__init__(entity, 'silence', 0, 0, (120, 160), description)

