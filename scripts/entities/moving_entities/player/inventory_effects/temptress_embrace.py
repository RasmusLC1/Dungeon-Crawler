from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
from scripts.engine.assets.keys import keys

class Temptress_Embrace(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "temptress_embrace")

    def Enable(self):
        self.player.Set_Effect('temptress_embrace', 1, True)
        

    def Disable(self):
        self.player.Remove_Effect('temptress_embrace', 1)
    
    
    def Set_Decription(self):
        self.description = 'Damage scales\nwith health lost'