from scripts.items.loot.gold import Gold
from scripts.items.loot.key import Key


class Loot_Handler():
    def __init__(self, game):
        self.game = game    

    def Loot_Spawner(self, name, pos_x, pos_y, amount = 0, data = None):
        loot = None
        if 'gold' == name:
            loot = self.Spawn_Gold(pos_x, pos_y, amount)
        elif 'key' == name:
            loot = self.Spawn_Key(pos_x, pos_y)

        if not loot:
            return False
        
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return True


    def Spawn_Gold(self, pos_x, pos_y, amount):
        loot = Gold(self.game, (pos_x, pos_y), amount)
        return loot
    
    def Spawn_Key(self, pos_x, pos_y):
        loot = Key(self.game, (pos_x, pos_y))
        return loot
