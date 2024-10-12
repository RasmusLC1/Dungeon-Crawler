from scripts.items.runes.healing_rune import Healing_Rune


class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = {}
        self.Initialise()

    def Initialise(self):
        healing_rune = Healing_Rune(self.game, (9999, 9999), 10, 5)
        self.add_rune(healing_rune)
    
    def add_rune(self, rune):
        type = rune.type
        print(type)
        if type not in self.runes:
            self.runes[type] = []
        self.runes[type].append(rune)

    def Update(self, offset = (0,0)):
        pass