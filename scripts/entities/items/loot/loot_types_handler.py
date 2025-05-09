
from scripts.entities.items.loot.passive.lantern import Lantern
from scripts.entities.items.loot.passive.passive_loot import Passive_Loot
from scripts.entities.items.loot.passive.echo_sigil import Echo_Sigil

import random


class Loot_Types_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {}

        self.types = []


    def Loot_Spawner(self, pos):
        type = random.choice(self.types)
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        

        loot = loot_class(self.game, pos)

        return loot





