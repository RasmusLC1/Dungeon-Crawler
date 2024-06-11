import pygame
import random

class Chest:
    def __init__(self, game, pos, size):
        i = 0
        while i < 5:
            self.version = i
            test = random.randint(0, 10)
            if test < 5:
                break
            i += 1
        self.game = game
        self.pos = pos
        self.size = size
        self.empty = False

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            loot_type = random.randint(0, 3)
            loot_amount = random.randint(1, 3)
            if loot_type == 0:
                if not self.game.player.Healing(loot_amount * self.version):
                    self.Update()
            elif loot_type == 1:
                if not self.game.player.Ammo_Change(loot_amount * self.version):
                    self.Update()
            elif loot_type == 2:
                self.game.player.Coin_Change(loot_amount * 3 * self.version)
            elif loot_type == 3:
                if not self.game.player.Healing(loot_amount * self.version):
                    self.Update()

            self.empty = True

    def Render(self, surf, offset = (0,0)):
        surf.blit(self.game.assets['Chest'][self.version], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    