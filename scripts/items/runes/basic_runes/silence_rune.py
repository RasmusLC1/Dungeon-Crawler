from scripts.items.runes.rune import Rune
import math
import pygame

class Silence_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'silence_rune', pos, 3, 40)
        self.animation_time_max = 30
        self.effect = 'silence'
        self.animation_size_max = 15

