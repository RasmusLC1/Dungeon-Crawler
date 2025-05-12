from scripts.entities.items.loot.revive.phoenix_feather import Phoenix_Feather
from scripts.entities.items.loot.revive.light_pendant import Light_Pendant
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler


class Revive_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
 

        self.loot_map = {
            self.game.dictionary.phoenix_feather: Phoenix_Feather,
            self.game.dictionary.light_pendant: Light_Pendant,
        }

 

        self.types = [
            self.game.dictionary.phoenix_feather,
            self.game.dictionary.light_pendant,
        ]





