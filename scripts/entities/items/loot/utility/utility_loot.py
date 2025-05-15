from scripts.entities.items.loot.interactive_loot import Interactive_Loot
from scripts.engine.assets.keys import keys

class Utility_Loot(Interactive_Loot):
    def __init__(self, game, type, pos, max_distance, amount):
        super().__init__(game, type, pos, max_distance, (16, 16), keys.utility, amount)