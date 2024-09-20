from scripts.items.interactive_item import Interactive_Item


class Potion(Interactive_Item):
    def __init__(self, game, type, pos, amount, effect):
        super().__init__(game, type, 'potion', pos, (10,10), amount)
        self.Update()
        self.max_amount = 3
        self.max_animation = 4
        self.effect = effect
