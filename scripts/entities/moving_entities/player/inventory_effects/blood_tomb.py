from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Blood_Tomb(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "blood_tomb")

    def Enable(self):
        self.player.Set_Effect('blood_tomb', 1, True)
        

    def Disable(self):
        self.player.Remove_Effect('blood_tomb')
    
    def Set_Decription(self):
        self.description = 'Gain souls\nwhen damaged'