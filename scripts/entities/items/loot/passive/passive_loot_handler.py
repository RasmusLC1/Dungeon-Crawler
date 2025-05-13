
from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Passive_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)

        self.loot_map = {
            game.keys.lantern: Lantern,
            game.keys.echo_sigil: Echo_Sigil,
        }

        self.special_type = [
            game.keys.lantern,
            game.keys.echo_sigil,
        ]



        self.types = [
            game.keys.lantern,
            game.keys.anchor_stone,
            game.keys.magnet,
            game.keys.strength_totem,
            game.keys.power_totem,
            game.keys.muffled_boots,
            game.keys.halo,
            game.keys.faith_pendant,
            game.keys.lucky_charm,
            game.keys.echo_sigil,
        ]


    def Loot_Spawner(self, pos):
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




