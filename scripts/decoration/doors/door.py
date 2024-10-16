from scripts.decoration.decoration import Decoration


class Door(Decoration):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'door', pos, size)
        self.closed = True

    def Animation_Update(self):
        pass

    def Open(self):
        self.closed = False
        x = self.pos[0] // 16
        y = self.pos[1] // 16
        self.game.tilemap.tilemap[str(x) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y), 'active': 0, 'light': 0}
        self.game.clatter.Generate_Clatter(self.pos, 300) # Generate clatter to alert nearby enemies


    

