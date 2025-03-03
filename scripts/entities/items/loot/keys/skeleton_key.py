from scripts.entities.items.loot.keys.key import Key

class Skeleton_Key(Key):
    def __init__(self, game, pos):
        super().__init__(game, 'skeleton_key', pos)
        self.description = 'Opens any door, but only once'



    def Open_Door(self):
        self.game.inventory.Remove_Item(self)
        self.game.item_handler.Remove_Item(self, True)