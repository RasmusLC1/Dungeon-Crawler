from scripts.items.runes.rune import Rune
import math
import pygame

class Strength_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'strength_rune', pos, 3, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15
