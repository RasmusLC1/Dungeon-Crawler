from scripts.entities.items.loot.loot import Loot
import random
from scripts.engine.assets.keys import keys

class Gold(Loot):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'gold', pos, (20, 20), 1, 'gold',amount)
        self.max_amount = 99
        self.animation = random.randint(1, 3)
        self.description = f"gold {self.amount}\n"
