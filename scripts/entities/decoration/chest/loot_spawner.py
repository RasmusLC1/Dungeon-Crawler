import pygame
import random
from scripts.entities.decoration.decoration import Decoration
from scripts.entities.items.loot.gold import Gold
from scripts.entities.items.loot.keys.key import Key
from scripts.entities.entities import PhysicsEntity


from scripts.entities.items.weapons.weapon_handler import Weapon_Handler
from scripts.entities.items.potions.potion_handler import Potion_Handler



class Loot_Spawner(Decoration):
    def __init__(self, game, type, pos, size, destructable, health) -> None:
        super().__init__(game, type, pos, size, destructable, health)
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.text_color = (255, 255, 255)
        self.weapon_handler = Weapon_Handler(self.game)
        self.potion_handler = Potion_Handler(self.game)

        
