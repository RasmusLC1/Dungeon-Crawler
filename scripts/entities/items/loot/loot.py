from scripts.entities.items.item import Item
from scripts.entities.textbox.loot_textbox import Loot_Textbox
from scripts.engine.assets.keys import keys

class Loot(Item):
    def __init__(self, game, type, pos, size, value, loot_type, amount = 1):
        super().__init__(game, type, keys.loot, pos, size, amount, True, value)
        self.loot_type =  loot_type

        self.text_box = Loot_Textbox(self)
        self.description = f"gold {self.value}\n"

    def Save_Data(self):
        # self.saved_data[keys.type] = self.type
        self.saved_data[keys.loot_type] = self.loot_type
        super().Save_Data()

    def Load_Data(self, data):
        # self.type = data[keys.type]
        self.loot_type = data[keys.loot_type]
        super().Load_Data(data)

    def Update_Animation(self):
        pass

    
    def Revive(self):
        return False