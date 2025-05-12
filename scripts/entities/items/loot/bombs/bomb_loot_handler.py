from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Bomb_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
 

        self.types = [
            game.dictionary.fire_bomb,
            game.dictionary.frozen_bomb,
            game.dictionary.electric_bomb,
            game.dictionary.poison_bomb,
            game.dictionary.vampiric_bomb,
        ]

    def Loot_Spawner(self, pos):
        type = random.choice(self.types)
        bomb = Bomb(self.game, type, pos)
        return bomb

