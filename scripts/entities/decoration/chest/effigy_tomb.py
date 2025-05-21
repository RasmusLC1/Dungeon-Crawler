from scripts.entities.decoration.chest.loot_container import Loot_Container
from scripts.engine.assets.keys import keys
import random


class Effigy_Tomb(Loot_Container):
    def __init__(self, game, pos) -> None:
        self.enemies = {}
        super().__init__(game, keys.effigy_tomb, pos, False, 99, (32, 64))
        self.animation_max = 1

    def Open(self):
        if not super().Open():
            return False
        
        self.game.sound_handler.Play_Sound('tomb_lid', 0.3)

        self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies
        self.animation += 1
        self.Set_Entity_Image()

    def Drop_Loot(self):
        weight_values = [self.loot_weights[loot_type] for loot_type in self.loot_types]
        loot_type = random.choices(self.loot_types, weight_values, k=1)[0]
        if loot_type == keys.enemy:
            enemy_type = random.choices(
                population=list(self.enemies.keys()),
                weights=list(self.enemies.values()),
                k=1
            )[0]
            self.game.enemy_handler.Enemy_Spawner(enemy_type, self.Get_Pos())
            return
        else:
            self.Spawn_Loot(loot_type, self.Get_Pos())



    def Set_Loot_Types(self):
        self.loot_types = [keys.enemy,
                           keys.revive,
                           keys.curse]
        
        self.loot_weights = {keys.enemy : 10.5,
                             keys.revive : 0.2,
                             keys.curse : 0.3}
        
        self.enemies = {
            keys.wight_king : 0.1,
            keys.skeleton_bell_toller : 0.2,
            keys.skeleton_warrior : 0.5,
            keys.skeleton_undertaker : 0.2,
            keys.skeleton_cleric : 0.1,
        }