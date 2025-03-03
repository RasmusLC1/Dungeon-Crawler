from scripts.entities.textbox.textbox import Text_Box

class Loot_Textbox(Text_Box):
    def __init__(self, entity):
        super().__init__(entity)

    # Seperate function for size flexibility
    def Set_Y_Size(self):
        self.y_size = 80