from scripts.items.potions.potion import Potion


class Speed_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'speed_potion', pos, amount, 5, 'yellow')
        self.max_amount = 3
        self.max_animation = 4
