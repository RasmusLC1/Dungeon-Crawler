from scripts.inventory.items.item import Item


class Mana_Potion(Item):
    def __init__(self, game, pos, amount):
        self.type = 'mana_potion'
        super().__init__(game, self.type, pos, amount)
        self.Update()
        self.max_amount = 3

    def Activate(self):
        if self.game.player.Increase_Mana(10):
            self.amount -= 1
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