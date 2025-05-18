

from scripts.entities.items.loot.curse.cursed_loot import Cursed_Loot
from scripts.entities.items.loot.curse.black_coin import Black_Coin
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random
from scripts.engine.assets.keys import keys


class Cursed_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)

        self.loot_map = {
            keys.black_coin: Black_Coin,
        }

        # Needs special spawning conditions
        self.special_type = [
            keys.black_coin,
        ]


        self.types = [
            # keys.temptress_embrace,
            # keys.demonic_bargain,
            # keys.blood_tomb,
            keys.black_coin,
        ]


    def Loot_Spawner(self, pos, type = None):
        if not type:
            type = random.choice(self.types)
        loot = None
        if type in self.special_type: # Handle lantern seperately as it needs light updates
            loot_class = self.loot_map.get(type)
            if not loot_class:
                return None
            

            loot = loot_class(self.game, pos)
        else:
            loot = Cursed_Loot(self.game, type, pos)


        return loot




