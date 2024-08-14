from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.item import Item
from scripts.entities.player.items.weapons.weapon import Weapon
import random
import pygame


class Spear(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 5, 1, 'two_handed_melee')
        self.max_animation = 3
        self.attack_animation_max = 3
        



    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()
        return False

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        self.Move((self.pos[0] + 20, self.pos[1] + 20))