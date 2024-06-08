import random
import math
import pygame

class Spike:
    def __init__(self, game, pos, size, speed):
        self.game = game
        self.pos = pos
        self.speed = speed
        self.size = size
        self.Cooldown = 0
        self.animation = random.randint(0, 5)
        self.animation_cooldown = 0

    def Update(self):
        if self.Cooldown > 0:
            self.Cooldown -= 1

        if self.rect().colliderect(self.game.player.rect()) and self.Cooldown == 0 and self.animation > 3:
            if not self.game.player.dashing:
                self.game.player.Damage_Taken(2)
                self.Cooldown = 100

        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1

        if self.animation_cooldown == 0:
            if self.animation >= 5:
                self.animation = 0
            else:
                self.animation += 1
            
            self.animation_cooldown = random.randint(20, 30)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets['spike'][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))