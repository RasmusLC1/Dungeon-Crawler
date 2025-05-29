from scripts.entities.items.loot.keys.key_loot_handler import Key_Loot_Handler
from scripts.entities.items.loot.valueable.valueable_loot_handler import Valuable_Loot_Handler

from scripts.entities.items.loot.bombs.bomb_loot_handler import Bomb_Loot_Handler
from scripts.entities.items.loot.utility.utility_loot_handler import Utility_Loot_Handler
from scripts.entities.items.loot.passive.passive_loot_handler import Passive_Loot_Handler
from scripts.entities.items.loot.revive.revive_loot_handler import Revive_Loot_Handler
from scripts.entities.items.loot.curse.cursed_loot_handler import Cursed_Loot_Handler


from scripts.entities.items.loot.potions.potion_handler import Potion_Handler
from scripts.engine.assets.keys import keys





import random


class Loot_Handler():
    def __init__(self, game):
        self.game = game

        self.key_loot_handler = Key_Loot_Handler(game) 
        self.bomb_loot_handler = Bomb_Loot_Handler(game) 
        self.utility_loot_handler = Utility_Loot_Handler(game) 
        self.passive_loot_handler = Passive_Loot_Handler(game) 
        self.revive_loot_handler = Revive_Loot_Handler(game) 
        self.potion_loot_handler = Potion_Handler(game) 
        self.cursed_loot_handler = Cursed_Loot_Handler(game) 
        self.valueable_loot_handler = Valuable_Loot_Handler(game) 

        self.loot_types = [
            self.key_loot_handler,
            self.bomb_loot_handler,
            self.utility_loot_handler,
            self.passive_loot_handler,
            self.revive_loot_handler,
            self.potion_loot_handler,
            self.valueable_loot_handler,
        ]

        self.loot_types_dic = {
            keys.key : self.key_loot_handler,
            keys.bomb : self.bomb_loot_handler,
            keys.utility : self.utility_loot_handler,
            keys.passive : self.passive_loot_handler,
            keys.revive : self.revive_loot_handler,
            keys.potion : self.potion_loot_handler,
            keys.curse : self.cursed_loot_handler,
            keys.valuable : self.valueable_loot_handler,
        }

        self.loot_types_weights = {
            keys.key : 0.05,
            keys.bomb : 0.2,
            keys.utility : 0.1,
            keys.passive : 0.05,
            keys.revive : 0.02,
            keys.potion : 0.3,
            keys.curse : 0.1,
        }

        self.loot_types_keys = [
            keys.key,
            keys.bomb,
            keys.utility,
            keys.passive,
            keys.revive,
            keys.potion,
            keys.curse,
            keys.valuable,
        ]

    
    # Responsible for loading the data and adding the item to the itemhandler
    def Load_Data(self, loot, data = None):
        if not loot:
            return None
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return loot
    
    # Adjust the weights based on events to control the inventory state closer
    def Adjust_Weights(self):
        weights = self.loot_types_weights.copy()
        items_in_inventory = self.game.inventory.item_inventory.Find_Loot()
        
        key_amount = 0 
        revive_amount = 0 
        for item in items_in_inventory:
            if not hasattr(item, 'loot_type'):
                continue

            if item.loot_type == keys.key:
                key_amount += 1
            elif item.loot_type == keys.revive:
                revive_amount += 1
        
        if revive_amount > 0:
            weights[keys.revive] /= 10
        if key_amount == 0:
            weights[keys.key] = 0.5

        return weights

 
    # Function for creating loot
    def Spawn_Random_Loot(self, pos):
        weights_dict = self.Adjust_Weights()
        weight_values = [weights_dict[loot_types_keys] for loot_types_keys in self.loot_types_keys]
        loot_handler = random.choices(self.loot_types, weight_values, k=1)[0]
        loot = loot_handler.Loot_Spawner(pos)
        if not loot:
            return

        self.game.item_handler.Add_Item(loot)


    def Spawn_Key(self, pos):
        return self.key_loot_handler.Loot_Spawner(pos)

    def Spawn_Gold(self, pos, amount):
        return self.valueable_loot_handler.Spawn_Gold(pos, amount)

    def Spawn_Loot_Type(self, loot_type, pos, data = None):
        loot_handler = self.loot_types_dic.get(loot_type)
        if not loot_handler:
            return None
        
        type = None
        if data:
            type = data[keys.type]

        loot = loot_handler.Loot_Spawner(pos, type)

        return self.Load_Data(loot, data)
    



