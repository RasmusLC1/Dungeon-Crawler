from scripts.entities.items.item import Item
from scripts.entities.textbox.loot_textbox import Loot_Textbox

class Loot(Item):
    def __init__(self, game, type, sub_category, pos, size, value, amount = 1):
        super().__init__(game, type, sub_category, pos, size, amount, True, value)
        self.text_box = Loot_Textbox(self)


    def Update_Animation(self):
        pass
