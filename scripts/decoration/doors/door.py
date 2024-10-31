from scripts.decoration.decoration import Decoration
import random

class Door(Decoration):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, pos, size)
        self.is_open = False

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['is_open'] = self.is_open


    def Load_Data(self, data):
        super().Load_Data(data)
        self.is_open = data['is_open']
        if self.is_open:
            self.Open(False)


    # TODO: IMPLEMENT walls that can be walked through, I.E walls without physics in tilemap
    def Open(self, generate_clatter = True):
        self.is_open = True
        x = self.pos[0] // 16
        y = self.pos[1] // 16
        self.game.tilemap.Add_Tile('Floor', 0, (x, y), False, self.active, self.light_level)
        
        
        if generate_clatter:
            self.game.clatter.Generate_Clatter(self.pos, 300) # Generate clatter to alert nearby enemies


    

