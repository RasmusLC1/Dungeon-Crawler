from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Demonic_Strength(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "demonic_strength")

    def Enable(self):
        pass

    def Disable(self):
        pass
    
    def Set_Decription(self):
        self.description = 'Damage scales\nwith health lost'