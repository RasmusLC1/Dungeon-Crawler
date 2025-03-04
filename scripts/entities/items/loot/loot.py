from scripts.entities.items.item import Item
from scripts.entities.textbox.loot_textbox import Loot_Textbox

class Loot(Item):
    def __init__(self, game, type, pos, size, value, amount = 1):
        super().__init__(game, type, 'loot', pos, size, amount, True, value)


        self.text_box = Loot_Textbox(self)
        self.description = (
                            f"gold {self.value}\n"
                        )


    def Update_Animation(self):
        pass
