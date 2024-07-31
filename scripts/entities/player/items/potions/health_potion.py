from scripts.entities.player.items.item import Item


class Health_Potion(Item):
    def __init__(self, game, pos, amount):
        self.type = 'health_potion'
        super().__init__(game, type, pos, (10,10), amount)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4

    def Activate(self):
        if self.game.player.Healing(10):
            self.amount -= 1
        if self.amount <= 0:
            self.used = True
        self.Update()
    
    def Update(self):
        if self.amount == 1:
            self.sub_type = 'red_low'
        elif self.amount == 2:
            self.sub_type = 'red_half'
        elif self.amount == 3:
            self.sub_type = 'red_full'