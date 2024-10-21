from scripts.items.potions.potion import Potion

class Regen_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'regen_potion', pos, amount, 4, 'pink')
        self.max_amount = 3
        self.max_animation = 4
