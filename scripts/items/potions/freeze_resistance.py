from scripts.items.potions.potion import Potion


class Freeze_Resistance_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'freeze_resistance_potion', pos, amount, 5)
        self.max_amount = 3
        self.max_animation = 4
