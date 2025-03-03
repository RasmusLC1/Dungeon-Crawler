from scripts.entities.items.loot.keys.key import Key
import random

class Lockpick(Key):
    def __init__(self, game, pos):
        super().__init__(game, 'lockpick', pos)
        self.description = '33`% to break'


    def Open_Door(self):
        random_value = random.randint(0, 3)
        if random_value > 0:
            return
        game = self.game # cache game for quick lookup
        game.inventory.Remove_Item(self)
        game.item_handler.Remove_Item(self, True)
        game.clatter.Generate_Clatter(self.pos, 1000) # Generate extra clatter for failure
        
