from scripts.entities.items.potions.potion import Potion


class Frozen_Resistance_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'frozen_resistance_potion', pos, amount, 5)
        self.max_amount = 3
        self.max_animation = 4
