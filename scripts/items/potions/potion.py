from scripts.items.item import Item


class Potion(Item):
    def __init__(self, game, type, pos, amount, strength):
        super().__init__(game, type, 'potion', pos, (10,10), amount)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4
        self.strength = strength
        self.effect = self.type.replace('_potion', '')

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['effect'] = self.effect
        self.saved_data['strength'] = self.strength

    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.effect = data['effect']
        self.strength = data['strength']

    def Activate(self):
        if self.game.player.Set_Effect(self.effect, self.strength):
            self.Decrease_Amount(1)
            self.Update()
        if self.amount <= 0:
            self.used = True

    def Update(self):
        pass