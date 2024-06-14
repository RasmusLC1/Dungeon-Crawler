from scripts.traps.trap import Trap
import random
import math
import pygame


class Bear_Trap(Trap):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)

    def Update(self):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(self.game.player.rect()) and self.Cooldown == 0 and not self.game.player.dashing:
            if not self.game.player.dashing:
                self.game.player.Damage_Taken(2)
                self.game.player.Set_Snare(100)
                self.Cooldown = 300
            
        if self.Cooldown:
            if not self.animation_cooldown:
                self.animation = min(3, self.animation + 1)
                self.animation_cooldown = 10

            self.animation_cooldown -= 1
        
        if self.Cooldown < 200:
            self.animation = 0

    def rect(self):
        return pygame.Rect(self.pos[0]+10, self.pos[1]+10, self.size[0], self.size[1])
    