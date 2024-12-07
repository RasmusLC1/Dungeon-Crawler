from scripts.items.runes.rune import Rune

import pygame

class Fire_Resistance_Rune(Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'fire_resistance_rune', pos, 5, 15)
        self.animation_time_max = 20
        self.effect = 'fire_resistance'
        self.animation_size_max = 25


        

    