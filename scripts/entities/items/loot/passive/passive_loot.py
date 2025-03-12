from scripts.entities.items.loot.loot import Loot

class Passive_Loot(Loot):
    def __init__(self, game, type, pos):
        super().__init__(game, type, pos, (16, 16), 10)

    def Save_Data(self):
        self.saved_data['type'] = self.type
        super().Save_Data()

    def Load_Data(self, data):
        self.type = data['type']
        super().Load_Data(data)

    def Pick_Up(self):
        if not super().Pick_Up():
            return False
        
        self.game.player.inventory_effects.Enable(self.type)
        return True

    def Place_Down(self):
        if not super().Place_Down():
            return False
        
        self.game.player.inventory_effects.Disable(self.type)
        return True

        
