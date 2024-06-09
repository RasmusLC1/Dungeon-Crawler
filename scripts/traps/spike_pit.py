from scripts.traps.trap import Trap

import random
import math
import pygame

class Spike_Pit(Trap):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

    def Update(self):
        # Resetting Trap
        if self.Cooldown > 0:
            self.Cooldown -= 1
        
        # Trigger trap animation and snare
        if self.rect().colliderect(self.game.player.rect()) and not self.Cooldown and not self.game.player.dashing:
            if not self.game.player.dashing:
                self.game.player.Damage_Taken(5)
                self.Cooldown = 100
                if not self.animation:
                    self.animation = 1
                    self.game.player.Snare(50)
                else:
                    self.game.player.Snare(25)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0]-5, self.size[1]-5)
                    
            