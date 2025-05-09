from scripts.entities.items.loot.bombs.bomb import Bomb

import random


class Bomb_Loot_Handler():
    def __init__(self, game):
        self.game = game    

        self.loot_map = {
            'bomb': Bomb,
        }
        self.bomb_types = [
            'fire_bomb',
            'frozen_bomb',
            'electric_bomb',
            'poison_bomb',
            'vampiric_bomb',
        ]




    def Loot_Spawner(self, type, pos_x, pos_y, amount = 0, data = None):
        loot_class = self.loot_map.get(type)
        if not loot_class:
            return None
        

        loot = loot_class(self.game, (pos_x, pos_y))

        return self.Load_Data(loot, data)
    
    # Responsible for loading the data and adding the item to the itemhandler
    def Load_Data(self, loot, data = None):
        if not loot:
            return None
        if data:
            loot.Load_Data(data)
        self.game.item_handler.Add_Item(loot)
        return loot


    def Spawn_Bomb(self, pos_x, pos_y, type = None, data = None):
        if not type:
            type = random.choice(self.bomb_types)

        bomb = Bomb(self.game, type, (pos_x, pos_y))
        
        return self.Load_Data(bomb, data)
