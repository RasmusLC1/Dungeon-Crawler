from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.key import Key


class Loot_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {
            'key': Key,
            'gold': Gold,
        }

    def Loot_Spawner(self, name, pos_x, pos_y, amount = 0, data = None):
        loot_class = self.loot_map.get(name)
        if amount:
            loot = loot_class(self.game, (pos_x, pos_y), amount)
        else:
            loot = loot_class(self.game, (pos_x, pos_y))
        if not loot:
            return None
        
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return loot
