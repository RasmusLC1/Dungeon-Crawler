from scripts.entities.moving_entities.effects.effect import Effect
import random

# Return damage dealth to entity
class Thorns(Effect):
    def __init__(self, entity):
        description = 'Reflects damage back to attackers'
        super().__init__(entity, 'thorns', 0, 0, (150, 200), description)
        self.type = 'slash'


    def Set_Type(self, type):
        self.type = type
