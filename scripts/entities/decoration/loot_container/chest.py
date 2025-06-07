from scripts.entities.decoration.loot_container.loot_container import Loot_Container
from scripts.engine.assets.keys import keys



class Chest(Loot_Container):
    def __init__(self, game, pos, version) -> None:
        super().__init__(game, keys.chest, pos, True, 5)
        self.version = version

    def Save_Data(self):
        super().Save_Data()
        self.saved_data['version'] = self.version
        

    def Load_Data(self, data):
        super().Load_Data(data)
        self.version = data['version']

    def Open(self):
        if not super().Open():
            return False
        
        self.game.decoration_handler.Remove_Decoration(self)
        self.game.sound_handler.Play_Sound('chest_open', 0.1)

        self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies

    def Set_Loot_Types(self):
        self.loot_weights = {keys.passive : 0.05,
                             keys.key : 0.1,
                             keys.bomb : 0.2,
                             keys.potion : 0.3,
                             keys.revive : 0.05,
                             keys.utility : 0.2,
                             keys.curse : 0.1,
                             keys.valuable : 100}


