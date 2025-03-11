from scripts.entities.moving_entities.effects.effect import Effect
import random

# Heal entity when dealing damage
class Vampiric(Effect):
    def __init__(self, entity):
        description = 'Heals when\ndealing damage'
        super().__init__(entity, "vampiric", 0, 0, (150, 200), description)

