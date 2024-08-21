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
        self.slash = True # Slash if True, stab if False

    def Update_Flip(self):
        pass

    
    def Update_Animation(self):
        if not self.equipped:
            return
        super().Update_Animation()

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        # Reset the attack logic
        if not self.attacking:
            self.rotate = 0
            return
        
        # Not updating the animation as the timer hasn't been hit yet
        if not self.attack_animation_counter >= self.attack_animation_time - 1:
            return
        if self.slash:
            pass
        else:
            self.Stabbing_Attack()

    def Set_Attack(self):
        self.slash = random.choice([True, False]) # Set either slash or stab
        return super().Set_Attack()


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
                self.Move((self.game.player.pos[0] - 4, self.game.player.pos[1] - 12))
            else:
                offset_x = self.Rotate_Left()
                self.Move((self.game.player.pos[0] + offset_x , self.game.player.pos[1] - 5))
        elif 'right' in self.inventory_type:
            
            if  direction_y < 0:
                self.rotate = 60
                self.Move((self.game.player.pos[0] + 1, self.game.player.pos[1] - 12))
            else:
                offset_x = self.Rotate_Right()
                self.Move((self.game.player.pos[0] + offset_x, self.game.player.pos[1] - 5))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

    def Rotate_Left(self):
        if self.flip_image:
            offset_x = 2
            self.rotate = -30
            self.slash = False
        else:
            offset_x = 11
            self.rotate = 0
            self.slash = True
        return offset_x
        
    def Rotate_Right(self):
        if self.flip_image:
            offset_x = -11
            self.rotate = 0
            self.slash = True
        else:
            offset_x = -2
            self.rotate = -30
            self.slash = False
        return offset_x

