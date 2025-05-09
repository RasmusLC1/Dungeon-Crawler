from scripts.entities.items.loot.revive.phoenix_feather import Phoenix_Feather
from scripts.entities.items.loot.revive.light_pendant import Light_Pendant

import random


class Revive_Loot_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {
            'phoenix_feather': Phoenix_Feather,
            'light_pendant': Light_Pendant,
        }

 

        self.revive_items = [
            'phoenix_feather',
            'light_pendant',
        ]


    def Loot_Spawner(self, type, pos_x, pos_y, amount = 0, data = None):
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        

        loot = loot_class(self.game, (pos_x, pos_y))

        return self.Load_Data(loot, data)
    
    # Responsible for loading the data and adding the item to the itemhandler
    def Load_Data(self, loot, data = None):
        if not loot:
            return None
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return loot
    
    def Spawn_Revive(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.revive_items)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)







