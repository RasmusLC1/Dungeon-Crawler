from scripts.decoration.decoration import Decoration
from scripts.entities.items.item import Item
from scripts.entities.items.weapons.weapon import Weapon
import random
import pygame


class Sword(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 5, 1, 'one_handed_melee')
        self.offset = 0
        self.max_animation = 3
        self.attack_animation_max = 3
        self.animation_speed = 20

    def Update_Flip(self):
        pass

    def Update_Animation(self):
        if not self.equipped:
            return
        super().Update_Animation()



    def Modify_Offset(self, change):
        self.offset -= change
        print(self.offset)

    def Set_Equipped_Position(self, direction_y):
        offset_x = 0
        if self.entity.flip[0]:
            self.flip_image = True
        else:
            self.flip_image = False
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.rotate = 10
                self.Move((self.game.player.pos[0] - 4, self.game.player.pos[1] - 14))
            else:
                if self.flip_image:
                    offset_x = 2
                    self.rotate = -30
                else:
                    offset_x = 11
                    self.rotate = 0
                self.Move((self.game.player.pos[0] + offset_x , self.game.player.pos[1] - 7))
        elif 'right' in self.inventory_type:
            
            if  direction_y < 0:
                self.rotate = 60
                self.Move((self.game.player.pos[0] + 1, self.game.player.pos[1] - 14))
            else:
                if self.flip_image:
                    offset_x = -11
                    self.rotate = 0

                else:
                    offset_x = -2
                    self.rotate = -30
                self.Move((self.game.player.pos[0] + offset_x, self.game.player.pos[1] - 7))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

