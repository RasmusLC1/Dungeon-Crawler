from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.assets.keys import keys

# Resistance to freeze
class Frozen_Resistance(Effect):
    def __init__(self, entity):
        description = 'Prevents freezing'
        super().__init__(entity, keys.frozen_resistance, 0, 0, (200, 250), description)

    