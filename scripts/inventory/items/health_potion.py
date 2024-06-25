from scripts.inventory.items.item import Item


class Health_Potion(Item):
    def __init__(self, game, pos, amount):
        super().__init__(game, pos, amount)
        self.Update()
        self.max_amount = 3
        self.type = 'health_potion'

    def Activate(self):
        pass
    
    def Update(self):
        print(self.amount)
        if self.amount == 1:
            self.sub_type = 'red_low'
        elif self.amount == 2:
            self.sub_type = 'red_half'
        elif self.amount == 3:
            self.sub_type = 'red_full'