from scripts.decoration.decoration import Decoration
import random

class Door(Decoration):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'door', pos, size)
        self.is_open = False

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['is_open'] = self.is_open

    def Load_Data(self, data):
        super().Load_Data(data)
        self.is_open = data['is_open']



    def Open(self, generate_clatter = True):
        self.is_open = True
        x = self.pos[0] // 16
        y = self.pos[1] // 16
        self.game.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y), 'active': 0, 'light': 0}
        if generate_clatter:
            self.game.clatter.Generate_Clatter(self.pos, 300) # Generate clatter to alert nearby enemies


    

