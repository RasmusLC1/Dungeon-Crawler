from scripts.entities.items.loot.loot import Loot
import random
from scripts.engine.assets.keys import keys

class Hunter_Treasure(Loot):
    def __init__(self, game, pos):
        super().__init__(game, keys.hunter_treasure, pos, (20, 20), 1, keys.hunter_treasure)
        self.max_amount = 1
        self.description = f"Return to\nhunter shrine"
