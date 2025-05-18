import pygame
import random
from scripts.entities.decoration.decoration import Decoration
from scripts.entities.decoration.chest.loot_container import Loot_Container
from scripts.engine.assets.keys import keys



class Vase(Loot_Container):
    def __init__(self, game, pos) -> None:
        vase_version = random.randint(1, 5)
        super().__init__(game, keys.vase + '_' + str(vase_version), pos, True, 5)


    def Open(self):
        return

    def Set_Loot_Types(self):
        self.loot_types = [keys.gold,
                           keys.key,
                           keys.revive]
        
        self.loot_weights = {keys.gold : 0.8,
                             keys.key : 0.3,
                             keys.revive : 0.02}


