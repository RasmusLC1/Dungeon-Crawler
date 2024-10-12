from scripts.items.runes.rune import Rune

import pygame

class Healing_Rune(Rune):
    def __init__(self, game, pos, strength, soul_cost):
        super().__init__(game, 'healing_rune', pos, strength, soul_cost)
        self.animation_time_max = 30

        

    def Render_Animation(self, surf, offset=(0, 0)):
        pygame.draw.circle(self.game, (255, 0, 0), self.game.player.pos, 20)


