from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Blood_Pact(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "blood_pact")

    def Enable(self):
        pass

    def Disable(self):
        pass
    
    def Set_Decription(self):
        self.description = 'Revives you but\npermanently cursed'