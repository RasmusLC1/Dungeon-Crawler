from scripts.items.item import Item

class Rune(Item):
    def __init__(self, game, type, category, pos, size, strength, soul_cost):
        super().__init__(game, type, category, pos, size, 1)
        self.max_amount = 1
        self.strength = strength
        self.soul_cost = soul_cost

    
    def Activate(self):
        if self.game.player.Set_Effect(self.type, self.strength):
            self.game.player.Decrease_Souls(self.soul_cost)

    def Update(self):
        pass