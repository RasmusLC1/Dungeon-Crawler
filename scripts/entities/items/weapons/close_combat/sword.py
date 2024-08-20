from scripts.decoration.decoration import Decoration
from scripts.entities.items.item import Item
from scripts.entities.items.weapons.weapon import Weapon
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

    def Set_Equipped_Position(self, direction_y):
        # self.rotate = -180
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.game.player.pos[0] , self.game.player.pos[1] ))
            else:
                self.Move((self.game.player.pos[0] , self.game.player.pos[1]))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.game.player.pos[0], self.game.player.pos[1]))
            else:
                self.Move((self.game.player.pos[0], self.game.player.pos[1]))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

