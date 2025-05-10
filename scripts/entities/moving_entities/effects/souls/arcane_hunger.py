from scripts.entities.moving_entities.effects.effect import Effect
import random

# Increase souls from entity kills
class Arcane_Hunger(Effect):
    def __init__(self, entity):
        description = 'Gain souls\nfrom kills'
        super().__init__(entity, 'arcane_hunger', 0, 0, (200, 250), description)

