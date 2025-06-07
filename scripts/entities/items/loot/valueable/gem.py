from scripts.entities.items.loot.valueable.valueable import Valuable
from scripts.engine.assets.keys import keys

class Gem(Valuable):
    def __init__(self, game, pos, amount, effect, value):
        super().__init__(game, effect + '_gem', pos, value)
        self.amount = amount
        self.max_amount = 100 # Amount acts as damage, each extra amount = 1 damage
        self.effect = effect
        self.description = f"Add {self.effect, str(self.amount)}\nto weapon\ngold {self.amount * self.value}\n"