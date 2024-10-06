from scripts.items.item import Item
import random

class Key(Item):
    def __init__(self, game, pos):
        super().__init__(game, 'key', 'loot', pos, (10, 10), 1)
        self.value = 1

    def Update_Animation(self):
        pass

    def Unlock_Door(self):
        pass