from scripts.items.item import Item


class Potion(Item):
    def __init__(self, game, type, pos, amount):
        super().__init__(game, type, 'potion', pos, (10,10), amount)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4