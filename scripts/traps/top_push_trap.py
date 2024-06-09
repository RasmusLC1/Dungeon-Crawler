from scripts.traps.trap import Trap

import random
import math
import pygame

class Top_Push_Trap(Trap):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

    def Update(self):
        # Resetting Trap
        if self.Cooldown > 0:
            self.Cooldown -= 1
        
        if self.animation > 0 and self.Cooldown == 0 :
            self.animation += 1
            self.Cooldown = 10
            if self.animation > 9:
                self.animation = 0

        # Trigger trap animation and snare
        if self.rect().colliderect(self.game.player.rect()) and self.animation < 5 and not self.game.player.dashing:
                self.game.player.Push(0, self.animation*6)
                if self.animation == 0:
                    self.animation += 1



            