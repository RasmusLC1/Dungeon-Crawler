from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Halo(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "halo")

    def Enable(self):
        pass

    def Disable(self):
        pass
    
    def Set_Decription(self):
        self.description = 'Drains nearby enemies/nDestroyed on damage'