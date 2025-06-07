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
            keys.gold: Gold,
            keys.gem: Gem,
            keys.hunter_treasure: Hunter_Treasure,
        }



    def Spawn_Gold(self, pos, amount):
        loot = Gold(self.game, pos, amount)
        return loot


    def Spawn_Hunter_Treasure(self, pos):
        loot = Hunter_Treasure(self.game, pos)
        self.game.item_handler.Add_Item(loot)
        return loot
    
    def Loot_Spawner(self, pos, type = None):
        if not type:
            type = random.choice(self.types)
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        

        loot = loot_class(self.game, pos)

        return loot
