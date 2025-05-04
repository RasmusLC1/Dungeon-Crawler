import pygame
import random
from scripts.entities.decoration.decoration import Decoration
from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.keys.key import Key
from scripts.entities.entities import PhysicsEntity


from scripts.entities.items.weapons.weapon_handler import Weapon_Handler
from scripts.entities.items.potions.potion_handler import Potion_Handler



class Chest(Decoration):
    def __init__(self, game, pos, version) -> None:
        super().__init__(game, 'chest', pos, (32, 32))
        self.version = version
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.text_color = (255, 255, 255)
        self.weapon_handler = Weapon_Handler(self.game)
        self.potion_handler = Potion_Handler(self.game)

        self.potions = [
            'health',
            'regen',
            'soul',
            'speed',
            'strength',
            'invisibility',
            'silence',
            'fire_resistance',
            'frozen_resistance',
            'poison_resistance',
            'vampiric'
        ]


    

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['version'] = self.version
        self.saved_data['empty'] = self.empty
        

    def Load_Data(self, data):
        super().Load_Data(data)
        self.version = data['version']
        self.empty = data['empty']



    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Open(self):
        if self.empty:
            return
        
        version_modifier = self.version * 3 + 1
        self.loot_amount = random.randint(1, 3) * version_modifier
        self.loot_type = random.randint(5, 6) # Spawn normal
        if self.loot_type in range(0, 3):
            if not self.Potion_Spawner():
                self.Open()
                return

        elif self.loot_type in range(4, 6):
            rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
            rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
            # loot = Gold(self.game, (rand_pos_x, rand_pos_y), random.randint(60,60))
            random_val = random.randint(1, 2)
            if random_val == 1:
                self.game.item_handler.loot_handler.Spawn_Passive(rand_pos_x, rand_pos_y)
            else:
                self.game.item_handler.loot_handler.Spawn_Utility(rand_pos_x, rand_pos_y)

        # Call itself redcursively if it should fail
        else:
            self.Open()
            return
        
        # self.empty = True
        self.game.decoration_handler.Remove_Decoration(self)

        self.text_cooldown = 30
        self.game.item_handler.Reset_Nearby_Items_Cooldown()
        self.game.sound_handler.Play_Sound('chest_open', 0.15)

        self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies

    def Potion_Spawner(self):
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        potion_index = random.randint(0, len(self.potions) - 1)
        potion_amount = random.randint(1,3)
        return self.potion_handler.Spawn_Potions(self.potions[potion_index], rand_pos_x, rand_pos_y, potion_amount)
        
    

    def Weapon_Spawner(self):
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        weapon_index = random.randint(0, len(self.weapons) - 1)
        loot_amount = min(20, max(self.loot_amount // 5, 3))
        return self.weapon_handler.Weapon_Spawner(self.weapons[weapon_index], rand_pos_x, rand_pos_y, loot_amount)


    def Reduce_Active(self):
        self.active -= 1
