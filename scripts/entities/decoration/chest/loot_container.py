import pygame
import random
from scripts.entities.decoration.decoration import Decoration
from scripts.engine.assets.keys import keys


class Loot_Container(Decoration):
    def __init__(self, game, type, pos, destructable, health) -> None:
        super().__init__(game, type, pos, (32, 32), destructable, health)
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.loot_types = []
        self.loot_weights = {}
        self.Set_Loot_Types()
        self.sub_category = keys.loot_container

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['version'] = self.version
        self.saved_data['empty'] = self.empty
        

    def Load_Data(self, data):
        super().Load_Data(data)
        self.version = data['version']
        self.empty = data['empty']

    def Open(self):
        if self.empty:
            return False
        
        self.Drop_Loot()
        self.empty = True
        self.game.item_handler.Reset_Nearby_Items_Cooldown()
        
        return True

    def Drop_Loot(self):
        rand_pos_x = self.pos[0] + random.randint(-100, 100)/10
        rand_pos_y = self.pos[1] + random.randint(-100, 100)/10
        self.game.item_handler.loot_handler.Spawn_Loot_From_Table((rand_pos_x, rand_pos_y), self.loot_types, self.loot_weights)

    def Set_Loot_Types(self):
        pass


    def Destroyed(self):
        if not super().Destroyed():
            return False

        self.Drop_Loot()
        return True

