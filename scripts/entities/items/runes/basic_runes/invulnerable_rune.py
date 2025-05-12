from scripts.entities.items.runes.rune import Rune

class Invulnerable_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.dictionary.Get_Invulnerable_Rune, pos, 4, 60)
        self.animation_time_max = 30
        self.animation_size_max = 15

