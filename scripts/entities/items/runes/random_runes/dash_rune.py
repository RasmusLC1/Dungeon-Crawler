from scripts.entities.items.runes.projectile_rune import Projectile_Rune
import math
import pygame

class Dash_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'dash_rune', pos, 10, 10)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.clicked = False
        self.effect = None

    def Generate_Projectile(self):
        self.game.player.movement_handler.Dash(self.game.render_scroll)
