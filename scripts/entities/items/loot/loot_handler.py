from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.keys.skeleton_key import Skeleton_Key
from scripts.entities.items.loot.keys.blood_key import Blood_Key
from scripts.entities.items.loot.keys.soul_key import Soul_Key
from scripts.entities.items.loot.keys.cursed_key import Cursed_Key
from scripts.entities.items.loot.keys.lockpick import Lockpick

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
            'gold': Gold,
        }

        self.key_types = [
            'skeleton_key',
            'blood_key',
            'soul_key',
            'cursed_key',
            'lockpick',
        ]

    def Loot_Spawner(self, type, pos_x, pos_y, amount = 0, data = None):
        loot_class = self.loot_map.get(type)
        if amount > 1:
            loot = loot_class(self.game, (pos_x, pos_y), amount)
        else:
            loot = loot_class(self.game, (pos_x, pos_y))
        if not loot:
            return None
        
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return loot
    

    def Spawn_Key(self, pos_x, pos_y, data = None):
        type = random.choice(self.key_types)

        self.Loot_Spawner(type, pos_x, pos_y, 0, data)

