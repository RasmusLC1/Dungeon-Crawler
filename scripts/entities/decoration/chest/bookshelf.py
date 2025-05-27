from scripts.entities.decoration.chest.loot_container import Loot_Container
from scripts.engine.assets.keys import keys
import random


class Bookshelf(Loot_Container):
    def __init__(self, game, pos) -> None:
        self.enemies = {}
        super().__init__(game, keys.effigy_tomb, pos, False, 99, (32, 64))

    def Open(self):
        if not super().Open():
            return False
        
        self.Set_Entity_Image()



    def Set_Loot_Types(self):
        self.loot_types = [keys.recipe_scroll,
                           keys.temptress_embrace,
                           keys.demonic_bargain,
                           keys.blood_tomb,
                           'empty'
                           ]
        
        self.loot_weights = {keys.recipe_scroll : 0.1,
                             keys.temptress_embrace: 0.1,
                             keys.demonic_bargain: 0.1,
                             keys.blood_tomb: 0.1,
                             }
