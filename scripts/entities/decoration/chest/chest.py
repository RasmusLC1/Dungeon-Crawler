import pygame
import random
from scripts.entities.decoration.decoration import Decoration
from scripts.engine.assets.keys import keys


class Chest(Decoration):
    def __init__(self, game, pos, version) -> None:
        super().__init__(game, keys.chest, pos, (32, 32), True, 5)
        self.version = version
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.text_color = (255, 255, 255)


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
        
        self.Drop_Loot()
        
        # self.empty = True
        self.game.decoration_handler.Remove_Decoration(self)

        self.text_cooldown = 30
        self.game.item_handler.Reset_Nearby_Items_Cooldown()
        self.game.sound_handler.Play_Sound('chest_open', 0.1)

        self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies

    def Drop_Loot(self):
        version_modifier = self.version * 3 + 1
        self.loot_amount = random.randint(1, 3) * version_modifier
        self.loot_type = random.randint(5, 6) # Spawn normal
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        self.game.item_handler.loot_handler.Spawn_Random_Loot((rand_pos_x, rand_pos_y))


    def Destroyed(self):
        if self.health > 0:
            return
        self.game.clatter.Generate_Clatter(self.pos, 1000) # Generate clatter to alert nearby enemies
        self.game.decoration_handler.Remove_Decoration(self)
        self.game.sound_handler.Play_Sound('chest_break', 0.2)

        self.Drop_Loot()


    def Reduce_Active(self):
        self.active -= 1
