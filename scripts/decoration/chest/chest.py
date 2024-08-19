import pygame
import random
from scripts.weapon_generator import Weapon_Generator
from scripts.entities.items.item import Item
from scripts.entities.items.potions.health_potion import Health_Potion
from scripts.entities.items.potions.mana_potion import Mana_Potion
from scripts.decoration.decoration import Decoration

from scripts.entities.items.weapons.sword import Sword
from scripts.entities.items.weapons.torch import Torch
from scripts.entities.items.weapons.spear import Spear


class Chest(Decoration):
    def __init__(self, game, pos, size, type, depth):
        super().__init__(game, pos, size, type)
        i = 0
        while i < 9:
            self.version = i
            if random.randint(depth, max(depth + 5, 10)) < max(depth + 2, 5):
                break
            i += 1
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.text_color = (255, 255, 255)
        self.weapon_type = ''
        self.active = 0
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
        self.weapons = [
            'sword',
            'torch',
            'spear'
        ]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Update(self):
        if self.rect().colliderect(self.game.player.rect()):
            version_modifier = self.version * 3 + 1
            self.loot_amount = random.randint(1, 3) * version_modifier
            self.loot_type = random.randint(0, 3)
            if self.loot_type == 0:
                    item = Health_Potion(self.game, (self.pos[0] + random.randint(-100, 100)/10 , self.pos[1] + random.randint(-100, 100)/10), random.randint(1,3))
                    self.game.item_handler.Add_Item(item)
            elif self.loot_type == 1:
                    item = Mana_Potion(self.game, (self.pos[0] + random.randint(-100, 100)/10 , self.pos[1] + random.randint(-100, 100)/10), random.randint(1,3))
                    self.game.item_handler.Add_Item(item)


            elif self.loot_type == 2:
                print("COIN")
                self.loot_amount *= 3
                self.game.player.Coin_Change(self.loot_amount)
                self.text_color  = (255,223,0)  
            elif self.loot_type == 3:
                rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
                rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
                weapon_index = random.randint(0, len(self.weapons) - 1)
                if self.weapons[weapon_index] == 'sword':
                    sword = Sword(self.game, (rand_pos_x, rand_pos_y), (16,16), 'sword')
                    self.game.item_handler.Add_Item(sword)
                elif self.weapons[weapon_index] == 'spear':
                    spear = Spear(self.game, (rand_pos_x, rand_pos_y), (16,16), 'spear')
                    self.game.item_handler.Add_Item(spear)
                elif self.weapons[weapon_index] == 'torch':
                    torch = Torch(self.game, (rand_pos_x, rand_pos_y), (16,16), 'torch')
                    self.game.item_handler.Add_Item(torch)


                    

                # if self.version <= 2:
                #     self.Update()
                # else:
                #     self.weapon_type = Weapon_Generator.Generate_Weapon(self, self.loot_amount)
                #     self.text_color  = (255, 255, 255)

            self.empty = True
            self.text_cooldown = 30

    def Set_Active(self, duration):
        self.active = duration
    
    def Reduce_Active(self):
        self.active -= 1

    def render_text(self, surf, offset = (0,0)):
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
        if self.empty:
            return
        
        if self.text_cooldown:
            self.Render_text(surf, offset)
            return
        

        if not self.Update_Light_Level():
            return
        # Set image
        chest_image = self.game.assets['Chest'][self.version].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))  # Adjust the factor as needed
        chest_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(chest_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        chest_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(chest_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


    