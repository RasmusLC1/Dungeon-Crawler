from scripts.items.potions.potion import Potion


class Poison_Resistance_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'poison_resistance_potion', pos, amount, 5)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4

    def Update(self):
        if self.amount == 1:
            self.sub_type = 'swamp_green_low'
        elif self.amount == 2:
            self.sub_type = 'swamp_green_half'
        elif self.amount == 3:
            self.sub_type = 'swamp_green_full'