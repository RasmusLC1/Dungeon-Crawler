import pygame
import random

class Chest:
    def __init__(self, game, pos, size):
        i = 0
        while i < 5:
            self.version = i
            if random.randint(0, 10) < 5:
                break
            i += 1
        self.game = game
        self.pos = pos
        self.size = size
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            self.loot_type = random.randint(0, 3)
            version_modifier = self.version * 3 + 1
            self.loot_amount = random.randint(1, 3) * version_modifier
            if self.loot_type == 0:
                if not self.game.player.Healing(self.loot_amount):
                    self.Update()
            elif self.loot_type == 1:
                if not self.game.player.Ammo_Change(self.loot_amount):
                    self.Update()
            elif self.loot_type == 2:
                self.loot_amount *= 3
                self.game.player.Coin_Change(self.loot_amount)
            elif self.loot_type == 3:
                if not self.game.player.Healing(self.loot_amount):
                    self.Update()
            self.empty = True
            self.text_cooldown = 30

    def Render_text(self, surf, offset = (0,0)):
        color = (255, 255, 255)
        if self.loot_type == 0:
            color = (255, 0, 0)
        elif self.loot_type == 1:
            color = (129, 133, 137)   
        elif self.loot_type == 2:
            color = (255,223,0)  
        elif self.loot_type == 3:
            color = (255, 0, 0)
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
        text = font.render(str(self.loot_amount), True, color)
        surf.blit(text, (self.pos[0] - offset[0], self.pos[1] - offset[1] - self.text_animation))
        self.text_animation += 1
        self.text_cooldown -= 1




    def Render(self, surf, offset = (0,0)):

        surf.blit(self.game.assets['Chest'][self.version], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    