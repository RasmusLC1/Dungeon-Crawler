
from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil

import random


class Passive_Loot_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {
            'lantern': Lantern,
            'echo_sigil': Echo_Sigil,
        }

        self.special_type = [
            'lantern',
            'echo_sigil',
        ]



        self.passive_types = [
            'lantern',
            'anchor_stone',
            'magnet',
            'strength_totem',
            'power_totem',
            'muffled_boots',
            'halo',
            'faith_pendant',
            'lucky_charm',
            'echo_sigil',
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


    def Spawn_Passive(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.passive_types)
        if type in self.special_type: # Handle lantern seperately as it needs light updates
            return self.Loot_Spawner(type, pos_x, pos_y, 0, data)
            
        
        passive_Loot = Passive_Loot(self.game, type, (pos_x, pos_y))

        return self.Load_Data(passive_Loot, data)







