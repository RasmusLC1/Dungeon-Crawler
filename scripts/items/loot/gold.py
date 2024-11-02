from scripts.items.item import Item
import random

class Gold(Item):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'gold', 'loot', pos, (10, 10), amount)
        self.max_amount = 99
        self.value = 1
        self.animation = random.randint(1, 3)

    def Update_Animation(self):
        pass