from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.keys.skeleton_key import Skeleton_Key
from scripts.entities.items.loot.keys.blood_key import Blood_Key
from scripts.entities.items.loot.keys.soul_key import Soul_Key
from scripts.entities.items.loot.keys.cursed_key import Cursed_Key
from scripts.entities.items.loot.keys.lockpick import Lockpick
from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.loot.utility.echo_bell import Echo_Bell
from scripts.entities.items.loot.utility.shadow_cloak import Shadow_Cloak
from scripts.entities.items.loot.utility.faded_hourglass import Faded_Hourglass
from scripts.entities.items.loot.utility.ethereal_chains import Ethereal_Chains
from scripts.entities.items.loot.utility.recall_parchment import Recall_Parchment

from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil

from scripts.entities.items.loot.revive.phoenix_feather import Phoenix_Feather
from scripts.entities.items.loot.revive.light_pendant import Light_Pendant

import random


class Loot_Handler():
    def __init__(self, game):
        self.game = game    

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
            'recall_parchment': Recall_Parchment,
            'lantern': Lantern,
            'phoenix_feather': Phoenix_Feather,
            'light_pendant': Light_Pendant,
            'echo_sigil': Echo_Sigil,
        }

        self.key_types = [
            'skeleton_key',
            'blood_key',
            'soul_key',
            'cursed_key',
            'lockpick',
        ]

        self.bomb_types = [
            'fire_bomb',
            'frozen_bomb',
            'electric_bomb',
            'poison_bomb',
            'vampiric_bomb',
        ]

        self.utility_types = [
            'echo_bell',
            'shadow_cloak',
            'faded_hourglass',
            'ethereal_chains',
            'recall_parchment'
        ]

        self.passive_types = [
            # 'lantern',
            # 'anchor_stone',
            # 'magnet',
            # 'strength_totem',
            # 'power_totem',
            # 'muffled_boots',
            # 'halo',
            # 'faith_pendant',
            # 'lucky_charm',
            'echo_sigil',
        ]

        self.revive_items = [
            'phoenix_feather',
            'light_pendant',
        ]

        self.cursed_items = [
            'demonic_bargain',
            'blood_tomb',
            'temptress_embrace',
        ]


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
        match loot_type:
            case 'gold':
                return self.Spawn_Gold(pos_x, pos_y, amount, data)
            case 'key':
                return self.Spawn_Key(pos_x, pos_y, type, data)
            case 'bomb':
                return self.Spawn_Bomb(pos_x, pos_y, type, data)
            case 'utility':
                return self.Spawn_Utility(pos_x, pos_y, type, data)
            case 'passive':
                return self.Spawn_Passive(pos_x, pos_y, type, data)
            case 'cursed':
                return self.Spawn_Cursed(pos_x, pos_y, type, data)
            case _:
                return self.Loot_Spawner(type, pos_x, pos_y, amount, data)




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
    

    def Spawn_Key(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.key_types)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)

    def Spawn_Bomb(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.bomb_types)

        bomb = Bomb(self.game, type, (pos_x, pos_y))
        
        return self.Load_Data(bomb, data)

    def Spawn_Gold(self, pos_x, pos_y, amount, type = None, data = None):
        gold = Gold(self.game, (pos_x, pos_y), amount)

        return self.Load_Data(gold, data)



    def Spawn_Utility(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.utility_types)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)

    def Spawn_Passive(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.passive_types)
        if type == 'lantern' or type == 'echo_sigil': # Handle lantern seperately as it needs light updates
            return self.Loot_Spawner(type, pos_x, pos_y, 0, data)
            
        
        passive_Loot = Passive_Loot(self.game, type, (pos_x, pos_y))

        return self.Load_Data(passive_Loot, data)


    def Spawn_Cursed(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.cursed_items)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)


    def Spawn_Revive(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.revive_items)

        return self.Loot_Spawner(type, pos_x, pos_y, 0, data)







