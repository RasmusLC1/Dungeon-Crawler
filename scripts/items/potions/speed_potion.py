from scripts.items.potions.potion import Potion



class Speed_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'speed_potion', pos, amount, 10)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4
        self.effect = 5

    def Activate(self):
        self.game.player.Increase_Souls(self.effect)
        self.Decrease_Amount(1)
        if self.amount <= 0:
            self.used = True
        self.Update()
    
    def Update(self):
        if self.amount == 1:
            self.sub_type = 'yellow_low'
        elif self.amount == 2:
            self.sub_type = 'yellow_half'
        elif self.amount == 3:
            self.sub_type = 'yellow_full'