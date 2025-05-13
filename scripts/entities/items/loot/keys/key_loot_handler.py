from scripts.entities.items.loot.keys.skeleton_key import Skeleton_Key
from scripts.entities.items.loot.keys.blood_key import Blood_Key
from scripts.entities.items.loot.keys.soul_key import Soul_Key
from scripts.entities.items.loot.keys.cursed_key import Cursed_Key
from scripts.entities.items.loot.keys.lockpick import Lockpick
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Key_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)


        self.loot_map = {
            game.keys.skeleton_key: Skeleton_Key,
            game.keys.blood_key: Blood_Key,
            game.keys.soul_key: Soul_Key,
            game.keys.cursed_key: Cursed_Key,
            game.keys.lockpick: Lockpick,
        }

        self.types = [
            game.keys.skeleton_key,
            game.keys.blood_key,
            game.keys.soul_key,
            game.keys.cursed_key,
            game.keys.lockpick,
        ]


