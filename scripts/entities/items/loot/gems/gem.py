from scripts.entities.items.loot.loot import Loot
from scripts.engine.assets.keys import keys

# Generic passive loot that changes depending on the type, simplified to one
# class since it uses effects
class Gem_Loot(Loot):
    def __init__(self, game, type, pos, damage, effect):
        super().__init__(game, type, pos, (16, 16), 10, keys.passive)
        self.damage = damage
        self.effect = effect
        self.Set_Value()

    def Set_Value(self):

        type_value = {
            keys.fire : 40,
            keys.frozen : 40,
            keys.electric : 40,
            keys.poison : 40,
            keys.electric : 40,
            keys.vampiric : 60,
            keys.arcane_hunger : 80,
            keys.blunt : 30,
            keys.slash : 30,
            keys.halo : 70,
            keys.power : 80,
            keys.range : 50,
            keys.speed : 50,
            keys.strength : 40,
            keys.terror : 90,
            keys.vulnerable : 60,
            keys.weakness : 50,
            keys.wet : 40,
            keys.durability : 40,
            # keys.multishot : 100
        }
        

    def Increase_Damage(self, damage):
        self.damage += damage