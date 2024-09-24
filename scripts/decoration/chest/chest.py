import pygame
import random
from scripts.weapon_generator import Weapon_Generator
from scripts.items.item import Item
from scripts.items.potions.health_potion import Health_Potion
from scripts.items.potions.soul_potion import Soul_Potion
from scripts.items.potions.regen_potion import Regen_Potion
from scripts.items.potions.speed_potion import Speed_Potion
from scripts.items.potions.strength_potion import Strength_Potion
from scripts.items.potions.invisibility_potion import Invisibility_Potion
from scripts.items.potions.silence_potion import Silence_Potion
from scripts.items.potions.fire_resistance_potion import Fire_Resistance_Potion
from scripts.items.potions.freeze_resistance import Freeze_Resistance_Potion
from scripts.items.potions.poison_resistance import Poison_Resistance_Potion
from scripts.decoration.decoration import Decoration

from scripts.items.weapons.close_combat.sword import Sword
from scripts.items.weapons.close_combat.torch import Torch
from scripts.items.weapons.projectiles.spear import Spear
from scripts.items.weapons.ranged_weapons.bow import Bow
from scripts.items.weapons.projectiles.arrow import Arrow
from scripts.items.weapons.shields.shield import Shield


class Chest(Decoration):
    def __init__(self, game, pos, size, type, depth) -> None:
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
            # 'sword',
            # 'torch',
            'spear',
            # 'bow',
            # 'arrow',
            # 'shield'
        ]

        self.potions = [
            'health',
            'regen',
            'soul',
            'speed',
            'strength',
            'invisibility',
            'silence',
            'fire_resistance',
            'freeze_resistance',
            'poison_resistance',
        ]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Open(self):
        version_modifier = self.version * 3 + 1
        self.loot_amount = random.randint(1, 3) * version_modifier
        self.loot_type = random.randint(3, 3)

        if self.loot_type in range(0, 3):
            if not self.Potion_Spawner():
                self.Open()
                return

        elif self.loot_type == 3:
            if not self.Weapon_Spawner():
                self.Open()
                return

        # Call itself recursively if it should fail
        else:
            self.Open()
            return
        
        self.empty = True
        self.text_cooldown = 30
        self.game.item_handler.Reset_Nearby_Items_Cooldown()
        self.game.sound_handler.Play_Sound('chest_open', 0.15)

        self.game.clatter.Generate_Clatter(self.pos, 5000) # Generate clatter to alert nearby enemies

    def Potion_Spawner(self):
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        potion_index = random.randint(0, len(self.potions) - 1)
        item = None
        if self.potions[potion_index] == 'health':
            item = Health_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'regen':
            item = Regen_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'soul':
            item = Soul_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'speed':
            item = Speed_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'strength':
            item = Strength_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'invisibility':
            item = Invisibility_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'silence':
            item = Silence_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'fire_resistance':
            item = Fire_Resistance_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'freeze_resistance':
            item = Freeze_Resistance_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))
        elif self.potions[potion_index] == 'poison_resistance':
            item = Poison_Resistance_Potion(self.game, (rand_pos_x, rand_pos_y), random.randint(1,3))

        
        if item:
            self.game.item_handler.Add_Item(item)
            return True
        
        return False
    

    def Weapon_Spawner(self):
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        weapon_index = random.randint(0, len(self.weapons) - 1)
        weapon = None
        if self.weapons[weapon_index] == 'sword':
            weapon = Sword(self.game, (rand_pos_x, rand_pos_y), (16,16))
        elif self.weapons[weapon_index] == 'shield':
            weapon = Shield(self.game, (rand_pos_x, rand_pos_y), (16,16))
        elif self.weapons[weapon_index] == 'spear':
            weapon = Spear(self.game, (rand_pos_x, rand_pos_y), (16,16))
        elif self.weapons[weapon_index] == 'torch':
            weapon = Torch(self.game, (rand_pos_x, rand_pos_y), (16,16))
        elif self.weapons[weapon_index] == 'bow':
            weapon = Bow(self.game, (rand_pos_x, rand_pos_y), (16,16))
        elif self.weapons[weapon_index] == 'arrow':
            loot_amount = min(20, max(self.loot_amount // 5, 3))
            for i in range(loot_amount):
                arrow = Arrow(self.game, (rand_pos_x, rand_pos_y), (16,16))
                self.game.item_handler.Add_Item(arrow)
            return True
        if weapon:
            self.game.item_handler.Add_Item(weapon)
            return True
        
        return False

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
        if not alpha_value:
            return
        
        chest_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(chest_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        chest_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(chest_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))


    