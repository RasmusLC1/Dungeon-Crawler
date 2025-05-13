from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Bomb_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
 

        self.types = [
            game.keys.fire_bomb,
            game.keys.frozen_bomb,
            game.keys.electric_bomb,
            game.keys.poison_bomb,
            game.keys.vampiric_bomb,
        ]

    def Loot_Spawner(self, pos):
        type = random.choice(self.types)
        bomb = Bomb(self.game, type, pos)
        return bomb

