
from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Passive_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)

        self.loot_map = {
            game.dictionary.lantern: Lantern,
            game.dictionary.echo_sigil: Echo_Sigil,
        }

        self.special_type = [
            game.dictionary.lantern,
            game.dictionary.echo_sigil,
        ]



        self.types = [
            game.dictionary.lantern,
            game.dictionary.anchor_stone,
            game.dictionary.magnet,
            game.dictionary.strength_totem,
            game.dictionary.power_totem,
            game.dictionary.muffled_boots,
            game.dictionary.halo,
            game.dictionary.faith_pendant,
            game.dictionary.lucky_charm,
            game.dictionary.echo_sigil,
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




