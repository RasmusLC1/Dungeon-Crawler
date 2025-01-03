from scripts.entities.items.loot.loot import Loot
import random

class Key(Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'key', 'loot', pos, (20, 20), 1)


    def Unlock_Door(self):
        pass