from scripts.entities.items.runes.rune import Rune


class Invisibility_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.keys.invisibility_rune, pos, 4, 60)
        self.animation_time_max = 30
        self.animation_size_max = 15

