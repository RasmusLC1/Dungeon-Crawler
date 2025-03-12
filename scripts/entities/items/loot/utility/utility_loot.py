from scripts.entities.items.loot.interactive_loot import Interactive_Loot

class Utility_Loot(Interactive_Loot):
    def __init__(self, game, type, pos, max_distance):
        super().__init__(game, type, pos, max_distance, (16, 16), 'utility')