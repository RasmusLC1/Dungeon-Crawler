from scripts.entities.items.runes.rune import Rune

import pygame

class Frozen_Resistance_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'frozen_resistance_rune', pos, 5, 15)
        self.animation_time_max = 20
        self.animation_size_max = 25