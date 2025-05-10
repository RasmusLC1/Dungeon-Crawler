from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.keys.skeleton_key import Skeleton_Key
from scripts.entities.items.loot.keys.blood_key import Blood_Key
from scripts.entities.items.loot.keys.soul_key import Soul_Key
from scripts.entities.items.loot.keys.cursed_key import Cursed_Key
from scripts.entities.items.loot.keys.lockpick import Lockpick
from scripts.entities.items.loot.keys.key_loot_handler import Key_Loot_Handler


from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.loot.bombs.bomb_loot_handler import Bomb_Loot_Handler


from scripts.entities.items.loot.utility.echo_bell import Echo_Bell
from scripts.entities.items.loot.utility.shadow_cloak import Shadow_Cloak
from scripts.entities.items.loot.utility.faded_hourglass import Faded_Hourglass
from scripts.entities.items.loot.utility.ethereal_chains import Ethereal_Chains
from scripts.entities.items.loot.utility.recall_scroll import Recall_Scroll
from scripts.entities.items.loot.utility.utility_loot_handler import Utility_Loot_Handler


from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil
from scripts.entities.items.loot.passive.passive_loot_handler import Passive_Loot_Handler

from scripts.entities.items.loot.revive.phoenix_feather import Phoenix_Feather
from scripts.entities.items.loot.revive.light_pendant import Light_Pendant
from scripts.entities.items.loot.revive.revive_loot_handler import Revive_Loot_Handler

from scripts.entities.items.loot.potions.potion_handler import Potion_Handler
from scripts.entities.items.loot.potions.potion import Potion





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

        self.loot_types = [
            self.key_loot_handler,
            self.bomb_loot_handler,
            self.utility_loot_handler,
            self.passive_loot_handler,
            self.revive_loot_handler,
            self.potion_loot_handler,
        ]

        self.loot_types_weights = {
            "key" : 0.05,
            "bomb" : 0.2,
            "utility" : 0.1,
            "passive" : 0.05,
            "revive" : 0.02,
            "potion" : 0.3,
        }

        self.loot_types_dic = {
            'key' : self.key_loot_handler,
            'bomb' : self.bomb_loot_handler,
            'utility' : self.utility_loot_handler,
            'passive' : self.passive_loot_handler,
            'revive' : self.revive_loot_handler,
            'potion' : self.potion_loot_handler,
        }

        self.loot_map = {
            'skeleton_key': Skeleton_Key,
            'blood_key': Blood_Key,
            'soul_key': Soul_Key,
            'cursed_key': Cursed_Key,
            'lockpick': Lockpick,
            'bomb': Bomb,
            'echo_bell': Echo_Bell,
            'faded_hourglass' : Faded_Hourglass,
            'ethereal_chains' : Ethereal_Chains,
            'shadow_cloak': Shadow_Cloak,
            'recall_scroll': Recall_Scroll,
            'lantern': Lantern,
            'phoenix_feather': Phoenix_Feather,
            'light_pendant': Light_Pendant,
            'echo_sigil': Echo_Sigil,
            'potion': Potion,
        }



    # Responsible initalising loot and finding the correct type
    def Loot_Loader(self, type, pos_x, pos_y, amount, data):
        # Handle when there's no data
        if not data:
            self.Loot_Spawner(type, pos_x, pos_y, amount)
            return
        
        loot_type = data.get('loot_type')

        if not loot_type:
            return
        
        # Match statement for loot type handling
        return self.Loot_Spawner(loot_type, pos_x, pos_y, amount, data)



    # Spawn specific loot
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
    
    def Adjust_Weights(self):
        pass

    # Function for creating loot
    def Spawn_Random_Loot(self, pos):
        loot_handler = random.choice(self.loot_types)
        loot = loot_handler.Loot_Spawner(pos)
        if not loot:
            return

        self.game.item_handler.Add_Item(loot)

    def Spawn_Key(self, pos):
        return self.key_loot_handler.Loot_Spawner(pos)

    def Spawn_Loot_Type(self, type, pos, data = None):
        loot_handler = self.loot_types_dic.get(type)

        if not loot_handler:
            return None
        
        loot = loot_handler.Loot_Spawner(pos)

        return self.Load_Data(loot, data)
    

    def Spawn_Gold(self, pos_x, pos_y, amount, type = None, data = None):
        gold = Gold(self.game, (pos_x, pos_y), amount)

        return self.Load_Data(gold, data)



