from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Power_Totem(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "power_totem")

    def Enable(self):
        self.player.Set_Effect('power', 1, True)
        

    def Disable(self):
        self.player.Remove_Effect('power', 1)
    
    def Set_Decription(self):
        self.description = 'Increases rune power'