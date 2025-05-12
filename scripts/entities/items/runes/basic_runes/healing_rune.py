from scripts.entities.items.runes.rune import Rune

import pygame

class Healing_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, game.dictionary.Get_Healing_Rune, pos, 10, 30)
        self.animation_time_max = 30
        self.animation_size_max = 15

