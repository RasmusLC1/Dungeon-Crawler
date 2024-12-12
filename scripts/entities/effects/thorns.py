from scripts.entities.effects.effect import Effect
import random

# Don't generate sound and clatter
class Thorns(Effect):
    def __init__(self, entity):
        super().__init__(entity, 'thorns', 0, 0, (150, 200))
        self.type = 'slash'


    def Set_Type(self, type):
        self.type = type
