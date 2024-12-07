from scripts.items.runes.rune import Rune

import pygame

class Freeze_Resistance_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'freeze_resistance_rune', pos, 5, 15)
        self.animation_time_max = 20
        self.effect = 'freeze_resistance'
        self.animation_size_max = 25
