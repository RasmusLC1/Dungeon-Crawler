import pygame

class Item:
    def __init__(self, pos, type, quality):
        self.type = type
        self.quality = quality
        self.pos = pos
        self.active = False
        self.animation = 0
        self.animation_cooldown = 0

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            print("TEST")

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def Render(self, surf, offset=(0, 0)):
        surf.blit(self.game.assets[self.type][self.animation], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        