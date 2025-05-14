from scripts.entities.moving_entities.player.inventory_effects.inventory_effect import Inventory_Effect
from scripts.engine.assets.keys import keys

class Forsaken_Grimoire(Inventory_Effect):
    def __init__(self, entity):
        super().__init__(entity, "forsaken_grimoire")

    def Enable(self):
        pass

    def Disable(self):
        pass
    
    def Set_Decription(self):
        self.description = 'Increases rune power/nbut cursed'