from scripts.items.potions.potion import Potion



class Health_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'healing_potion', pos, amount, 10, 'red')
        self.max_amount = 3
        self.max_animation = 4

