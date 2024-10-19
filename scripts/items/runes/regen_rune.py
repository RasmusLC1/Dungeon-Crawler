from scripts.items.runes.passive_rune import Passive_Rune

import pygame

class Regen_Rune(Passive_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'regen_rune', pos, 2, 1000, 30)
        self.effect = 'regen'

    