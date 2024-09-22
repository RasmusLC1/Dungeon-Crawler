from scripts.items.potions.potion import Potion

class Regen_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'regen_potion', pos, amount, 4)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4


    
    def Update(self):
        if self.amount == 1:
            self.sub_type = 'pink_low'
        elif self.amount == 2:
            self.sub_type = 'pink_half'
        elif self.amount == 3:
            self.sub_type = 'pink_full'