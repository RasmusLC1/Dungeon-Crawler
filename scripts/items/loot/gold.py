from scripts.items.item import Item
import random

class Gold(Item):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'gold_coins', 'loot', pos, (10, 10), amount)
        self.max_amount = 999
        self.value = 1
        self.animation = random.randint(1, 3)

        print(self.sub_type, self.animation)

    def Update_Animation(self):
        pass