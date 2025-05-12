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
            game.dictionary.skeleton_key: Skeleton_Key,
            game.dictionary.blood_key: Blood_Key,
            game.dictionary.soul_key: Soul_Key,
            game.dictionary.cursed_key: Cursed_Key,
            game.dictionary.lockpick: Lockpick,
        }

        self.types = [
            game.dictionary.skeleton_key,
            game.dictionary.blood_key,
            game.dictionary.soul_key,
            game.dictionary.cursed_key,
            game.dictionary.lockpick,
        ]


