from scripts.entities.moving_entities.effects.effect import Effect
from scripts.engine.assets.keys import keys

# Don't generate sound and clatter
class Silence(Effect):
    def __init__(self, entity):
        description = 'Reduces noise'

        super().__init__(entity, keys.silence, 0, 0, (120, 160), description)

