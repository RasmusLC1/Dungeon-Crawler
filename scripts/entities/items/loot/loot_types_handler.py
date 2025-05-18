from scripts.engine.assets.keys import keys
import random


class Loot_Types_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {}

        self.types = []


    def Loot_Spawner(self, pos, type = None):
        if not type:
            type = random.choice(self.types)
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        

        loot = loot_class(self.game, pos)

        return loot
