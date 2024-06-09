import random
import math
import pygame

class Bear_Trap:
    def __init__(self, game, pos, size, speed):
        self.game = game
        self.pos = pos
        self.speed = speed
        self.size = size
        self.Cooldown = 0
        self.animation = 0
        self.animation_cooldown = 0

    def Update(self):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(self.game.player.rect()) and self.Cooldown == 0:
            if not self.game.player.dashing:
                self.game.player.Damage_Taken(2)
                self.game.player.Snare(100)
                self.Cooldown = 400
            
        if self.Cooldown:
            if not self.animation_cooldown:
                self.animation = min(3, self.animation + 1)
                self.animation_cooldown = 10

            self.animation_cooldown -= 1
            self.Cooldown -= 1
        
        if self.Cooldown < 200:
            self.animation = 0

    def rect(self):
        return pygame.Rect(self.pos[0]+5, self.pos[1], self.size[0]/2, self.size[1]/2)
    
    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets['BearTrap'][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))