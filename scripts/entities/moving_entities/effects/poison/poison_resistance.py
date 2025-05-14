from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.assets.keys import keys

# Resist poison
class Poison_Resistance(Effect):
    def __init__(self, entity):
        description = 'Prevents poison'
        super().__init__(entity, "poison_resistance", 0, 0, (200, 250), description)

