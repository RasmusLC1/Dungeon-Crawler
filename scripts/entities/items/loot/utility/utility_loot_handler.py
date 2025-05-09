from scripts.entities.items.loot.utility.echo_bell import Echo_Bell
from scripts.entities.items.loot.utility.shadow_cloak import Shadow_Cloak
from scripts.entities.items.loot.utility.faded_hourglass import Faded_Hourglass
from scripts.entities.items.loot.utility.ethereal_chains import Ethereal_Chains
from scripts.entities.items.loot.utility.recall_scroll import Recall_Scroll


import random


class Utility_Loot_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {
            'echo_bell': Echo_Bell,
            'faded_hourglass' : Faded_Hourglass,
            'ethereal_chains' : Ethereal_Chains,
            'shadow_cloak': Shadow_Cloak,
            'recall_scroll': Recall_Scroll,
        }

        self.utility_types = [
            'echo_bell',
            'shadow_cloak',
            'faded_hourglass',
            'ethereal_chains',
            'recall_scroll'
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


    def Spawn_Utility(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.utility_types)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)





