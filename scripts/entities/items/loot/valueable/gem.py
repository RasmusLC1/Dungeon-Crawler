from scripts.entities.items.loot.loot import Loot
from scripts.engine.assets.keys import keys

class Gem(Loot):
    def __init__(self, game, type, pos, amount, effect):
        super().__init__(game, type, pos, (16, 16), 1, keys.valuable, amount)
        self.max_amount = 100 # Amount acts as damage, each extra amount = 1 damage
        self.effect = effect
        self.Set_Value()
        self.description = f"Add {self.effect, self.amount} to weapon\ngold {self.amount * self.value}\n"


    def Set_Value(self):

        type_value = {
            keys.fire : 4,
            keys.frozen : 4,
            keys.electric : 4,
            keys.poison : 4,
            keys.electric : 4,
            keys.vampiric : 6,
            keys.arcane_hunger : 8,
            keys.blunt : 3,
            keys.slash : 3,
            keys.halo : 7,
            keys.power : 8,
            keys.range : 5,
            keys.speed : 5,
            keys.strength : 4,
            keys.terror : 8,
            keys.vulnerable : 6,
            keys.weakness : 5,
            keys.wet : 4,
            keys.durability : 4,
        }
        self.value = type_value.get(self.effect, 1)