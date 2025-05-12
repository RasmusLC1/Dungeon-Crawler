from scripts.entities.items.runes.rune import Rune
import math
import pygame

class Speed_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.dictionary.Get_Speed_Rune, pos, 3, 25)
        self.animation_time_max = 30
        self.animation_size_max = 15
