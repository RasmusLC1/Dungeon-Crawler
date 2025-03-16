from scripts.entities.items.item import Item
from scripts.entities.textbox.loot_textbox import Loot_Textbox

class Loot(Item):
    def __init__(self, game, type, pos, size, value, loot_type, amount = 1):
        super().__init__(game, type, 'loot', pos, size, amount, True, value)
        self.loot_type =  loot_type

        self.text_box = Loot_Textbox(self)
        self.description = f"gold {self.value}\n"

    def Save_Data(self):
        # self.saved_data['type'] = self.type
        self.saved_data['loot_type'] = self.loot_type
        super().Save_Data()

    def Load_Data(self, data):
        # self.type = data['type']
        self.loot_type = data['loot_type']
        super().Load_Data(data)

    def Update_Animation(self):
        pass

    
    def Revive(self):
        return False