class Decoration():
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = pos
        self.size = size
        self.light = self.game.light_handler.Initialise_Light_Level(self.pos)

    def Update(self):
        pass

    def Render(self, surf, offset=(0, 0)):
        pass
