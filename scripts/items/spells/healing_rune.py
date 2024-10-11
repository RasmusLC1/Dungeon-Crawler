from scripts.items.spells.rune import Rune

class Healing_Rune(Rune):
    def __init__(self, game, type, category, pos, size, strength, soul_cost):
        super().__init__(game, type, category, pos, size, strength, soul_cost)

