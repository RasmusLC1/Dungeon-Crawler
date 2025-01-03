from scripts.entities.items.potions.potion import Potion


class Silence_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'silence_potion', pos, amount, 10)
        self.max_amount = 3
        self.max_animation = 4

