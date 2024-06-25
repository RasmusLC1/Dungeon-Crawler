import pygame
import random
from scripts.weapon_generator import Weapon_Generator
from scripts.inventory.items.item import Item
from scripts.inventory.items.health_potion import Health_Potion


class Chest:
    def __init__(self, game, pos, size, depth):
        i = 0
        while i < 9:
            self.version = i
            if random.randint(depth, max(depth + 5, 10)) < max(depth + 2, 5):
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
        self.text_color = (255, 255, 255)
        self.weapon_type = ''

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            self.loot_type = random.randint(0, 0)
            version_modifier = self.version * 3 + 1
            self.loot_amount = random.randint(1, 3) * version_modifier
            if self.loot_type == 0:
                print("HEALTH")
                # if not self.game.player.Healing(self.loot_amount):
                #     self.Update()
                # else:
                #     self.text_color  = (255, 0, 0)
                for i in range(3):
                    self.game.items.append(Health_Potion(self.game, (self.pos[0] + random.randint(-100, 100)/10 , self.pos[1] + random.randint(-100, 100)/10), random.randint(1,3)))
            elif self.loot_type == 1:
                print("AMMO")
                if not self.game.player.Ammo_Change(self.loot_amount):
                    self.Update()
                else:
                    self.text_color  = (129, 133, 137)    
            elif self.loot_type == 2:
                print("COIN")
                self.loot_amount *= 3
                self.game.player.Coin_Change(self.loot_amount)
                self.text_color  = (255,223,0)  
            elif self.loot_type == 3:
                print("WEAPON")
                if self.version <= 2:
                    self.Update()
                else:
                    self.weapon_type = Weapon_Generator.Generate_Weapon(self, self.loot_amount)
                    self.text_color  = (255, 255, 255)

            self.empty = True
            self.text_cooldown = 30

    def Render_text(self, surf, offset = (0,0)):
        try:
            font = pygame.font.Font('freesansbold.ttf', 10)
        except Exception as e:
            print(f"Font load error: {e}")
        if self.loot_type == 3 and self.version > 2:
            text = font.render(self.weapon_type, True, self.text_color)
        else:
            text = font.render(str(self.loot_amount), True, self.text_color)
        surf.blit(text, (self.pos[0] - offset[0], self.pos[1] - offset[1] - self.text_animation))
        self.text_animation += 1
        self.text_cooldown -= 1




    def Render(self, surf, offset = (0,0)):

        surf.blit(self.game.assets['Chest'][self.version], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    