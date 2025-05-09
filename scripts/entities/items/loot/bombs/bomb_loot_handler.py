from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler

import random


class Bomb_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)
 

        self.loot_map = {
            'bomb': Bomb,
        }
        self.types = [
            'fire_bomb',
            'frozen_bomb',
            'electric_bomb',
            'poison_bomb',
            'vampiric_bomb',
        ]
