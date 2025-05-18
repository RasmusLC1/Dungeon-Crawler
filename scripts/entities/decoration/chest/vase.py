import pygame
import random
from scripts.entities.decoration.chest.loot_container import Loot_Container
from scripts.engine.assets.keys import keys



class Vase(Loot_Container):
    def __init__(self, game, pos) -> None:
        self.version = random.randint(1, 5)
        super().__init__(game, keys.vase + '_' + str(self.version), pos, True, 5)

    # Ensure the correct version of the vase is saved and loaded
    def Save_Data(self):
        super().Save_Data()
        self.saved_data[keys.type] = keys.vase
        self.saved_data['version'] = self.version
        

    def Load_Data(self, data):
        super().Load_Data(data)
        self.version = data['version']
        self.type = keys.vase + '_' + str(self.version)
        self.Set_Sprite() # Initialise sprite again with correct type

    def Open(self):
        return

    def Set_Loot_Types(self):
        self.loot_types = [keys.gold,
                           keys.key,
                           keys.revive]
        
        self.loot_weights = {keys.gold : 0.8,
                             keys.key : 0.3,
                             keys.revive : 0.02}


