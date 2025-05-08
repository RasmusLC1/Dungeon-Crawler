from scripts.entities.items.potions.potion import Potion



class Soul_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'arcane_hunger_potion', pos, amount, 5)
        self.max_amount = 3
        self.max_animation = 4

