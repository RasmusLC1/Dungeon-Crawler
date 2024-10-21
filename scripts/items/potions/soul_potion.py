from scripts.items.potions.potion import Potion



class Soul_Potion(Potion):
    def __init__(self, game, pos, amount):
        super().__init__(game, 'soul_potion', pos, amount, 5, 'blue')
        self.max_amount = 3
        self.max_animation = 4

    def Activate(self):
        super().Activate()
        self.game.player.Increase_Souls(self.strength)
        self.Decrease_Amount(1)
        self.Update()
    
