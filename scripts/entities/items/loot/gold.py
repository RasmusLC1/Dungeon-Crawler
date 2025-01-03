from scripts.entities.items.loot.loot import Loot
import random

class Gold(Loot):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'gold', 'loot', pos, (20, 20), amount, 1)
        self.max_amount = 99
        self.animation = random.randint(1, 3)
