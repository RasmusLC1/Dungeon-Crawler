from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.item import Item
from scripts.entities.player.items.weapons.weapon import Weapon
import random
import pygame


class Sword(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 5, 1, 'one_handed_melee')
        self.attack_animation_max = 1


    def Place_Down(self):
        # Parent class Place_down function
        super().Place_Down()

        return False

