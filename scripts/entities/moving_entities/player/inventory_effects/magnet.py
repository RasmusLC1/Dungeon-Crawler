from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
class Magnet(Inventory_Effect):

    def Enable(self):
        self.player.Set_Effect(self.effect, 4, True)


    def Disable(self):
        self.player.Remove_Effect(self.effect)
        