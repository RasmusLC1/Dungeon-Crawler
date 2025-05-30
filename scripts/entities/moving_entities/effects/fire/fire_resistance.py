from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.assets.keys import keys

# Reduce fire damage
class Fire_Resistance(Effect):
    def __init__(self, entity):
        description = 'Prevents fire damage'
        super().__init__(entity, keys.fire_resistance, 0, 0, (200, 250), description)

