from scripts.entities.items.loot.valueable.gold import Gold
from scripts.entities.items.loot.valueable.gem import Gem
from scripts.entities.items.loot.valueable.hunter_treasure import Hunter_Treasure 
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler
from scripts.engine.assets.keys import keys
import random



class Valuable_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)


        self.loot_map = {
            # keys.gold: self.Spawn_Gold,
            keys.gem: self.Spawn_Gem,
        }



    def Spawn_Gold(self, pos, amount = None):
        if not amount:
            amount = random.randint(5 * self.game.level, 10 * self.game.level)

        loot = Gold(self.game, pos, amount)
        return loot

    def Get_Gem_Effect(self):
        effects = {
            # keys.fire : 4,
            # keys.frozen : 4,
            # keys.electric : 4,
            # keys.poison : 4,
            # keys.electric : 4,
            # keys.vampiric : 6,
            keys.arcane_hunger : 8,
            # keys.blunt : 3,
            # keys.slash : 3,
            # keys.halo : 7,
            # keys.power : 8,
            # keys.range : 5,
            # keys.speed : 5,
            # keys.strength : 4,
            # keys.terror : 8,
            # keys.vulnerable : 6,
            # keys.weakness : 5,
            # keys.wet : 4,
            # keys.durability : 4,
        }


        max_val = max(effects.values())
        inverted_weights = [max_val - v + 1 for v in effects.values()]

        effect = random.choices(
            population=list(effects.keys()),
            weights=inverted_weights,
            k=1
        )[0]
        value = effects[effect]
        return effect, value
    
    def Spawn_Gem(self, pos, amount):
        if not amount:
            amount = random.randint(1 * self.game.level, 5 * self.game.level)
        
        effect, value = self.Get_Gem_Effect()
        loot = Gem(self.game, pos, amount, effect, value)
        return loot

    def Spawn_Hunter_Treasure(self, pos):
        loot = Hunter_Treasure(self.game, pos)
        self.game.item_handler.Add_Item(loot)
        return loot
    
    def Loot_Spawner(self, pos, type = None, amount = None):
        if not type:
            type = random.choice(list(self.loot_map.keys()))

        # Handle hunter treasure seperately
        if type == keys.hunter_treasure:
            self.Spawn_Hunter_Treasure(pos)
            return
        
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        
        loot = loot_class(pos, amount)

        return loot
