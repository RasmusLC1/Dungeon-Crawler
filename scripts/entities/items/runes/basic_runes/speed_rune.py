from scripts.entities.items.runes.rune import Rune
from scripts.engine.assets.keys import keys

class Speed_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, keys.speed_rune, pos, 3, 25)
        self.animation_time_max = 30
        self.animation_size_max = 15
