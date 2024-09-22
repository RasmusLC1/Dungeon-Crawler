from scripts.items.potions.potion import Potion



class Soul_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'soul_potion', pos, amount, 5)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4

    def Activate(self):
        self.game.player.Increase_Souls(self.strength)
        self.Decrease_Amount(1)
        if self.amount <= 0:
            self.used = True
        self.Update()
    
    def Update(self):
        if self.amount == 1:
            self.sub_type = 'blue_low'
        elif self.amount == 2:
            self.sub_type = 'blue_half'
        elif self.amount == 3:
            self.sub_type = 'blue_full'