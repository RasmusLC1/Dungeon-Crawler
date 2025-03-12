from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Magnet(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "magnet")

    def Enable(self):
        self.player.Set_Effect(self.effect, 4, True)


    def Disable(self):
        self.player.Remove_Effect(self.effect)
        
    
    def Set_Decription(self):
        self.description = 'Auto pickup'