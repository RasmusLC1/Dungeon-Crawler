from scripts.items.potions.potion import Potion


class Fire_Resistance_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'fire_resistance_potion', pos, amount, 5, 'fire_resistance')
        self.max_amount = 3
        self.max_animation = 4

