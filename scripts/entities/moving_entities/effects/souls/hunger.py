from scripts.entities.moving_entities.effects.effect import Effect
import random

# Increase souls from entity kills
class Hunger(Effect):
    def __init__(self, entity):
        description = 'Increased souls\nfrom kills'
        super().__init__(entity, 'hunger', 0, 0, (200, 250), description)

