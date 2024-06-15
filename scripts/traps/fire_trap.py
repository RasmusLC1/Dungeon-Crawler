from scripts.traps.trap import Trap

import random
import math
import pygame

class Fire_Trap(Trap):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        self.animation = random.randint(0, 13)

    def Update(self):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(self.game.player.rect()) and self.Cooldown == 0 and self.animation > 7 and self.animation < 11 and not self.game.player.dashing:
            if not self.game.player.dashing:
                self.game.player.Set_On_Fire(3)
                self.Cooldown = 100

        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 13:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(10, 20)