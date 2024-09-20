from scripts.items.item import Item

class Interactive_Item(Item):
    def __init__(self, game, type, category, pos, size, amount):
        super().__init__(game, type, category, pos, size, amount)
        self.used = False
