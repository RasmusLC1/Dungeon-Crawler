from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Vampire_Locket(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "vampire_locket")

    def Enable(self):
        self.player.Set_Effect('vampiric', 2, True)
        

    def Disable(self):
        self.player.Remove_Effect('vampiric', 2)
    
    def Set_Decription(self):
        self.description = 'lifesteal, but drains health'