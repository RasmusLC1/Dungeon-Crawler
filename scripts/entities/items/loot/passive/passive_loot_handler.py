
from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil
from scripts.entities.items.loot.passive.recipe_scroll import Recipe_Scroll
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random
from scripts.engine.assets.keys import keys


class Passive_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)

        self.loot_map = {
            keys.lantern: Lantern,
            keys.echo_sigil: Echo_Sigil,
            keys.recipe_scroll: Recipe_Scroll,
        }

        self.special_type = [
            keys.lantern,
            keys.echo_sigil,
            keys.recipe_scroll,
        ]


        self.types = [
            keys.lantern,
            keys.anchor_stone,
            keys.magnet,
            keys.strength_totem,
            keys.power_totem,
            keys.muffled_boots,
            keys.halo,
            keys.faith_pendant,
            keys.lucky_charm,
            keys.echo_sigil,
            keys.recipe_scroll,
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
            loot = Passive_Loot(self.game, type, pos)


        return loot




