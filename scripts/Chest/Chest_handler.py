from scripts.Chest.chest import Chest

class Chest_Handler:
    def __init__(self):
        self.chests = []
        for chest in self.tilemap.extract([('Chest', 0)]):
            self.chests.append(Chest(self, chest['pos'], (self.assets[chest['type']][0].get_width(), self.assets[chest['type']][0].get_height())))  


    def Update(self):
        for chest in self.chests:
                if chest.empty:
                    if not chest.text_cooldown:
                        self.chests.remove(chest)
                else:
                    chest.Update()

    def Render(self, render_scroll):
         for chest in self.chests:
            if not chest.text_cooldown:
                chest.Render(self.display, render_scroll)
            else:
                chest.Render_text(self.display, render_scroll)
