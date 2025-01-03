from scripts.entities.items.runes.rune import Rune
import math
import pygame

class Resistance_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'resistance_rune', pos, 3, 15)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False

