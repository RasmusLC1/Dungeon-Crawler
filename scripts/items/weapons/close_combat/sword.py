from scripts.decoration.decoration import Decoration
from scripts.items.item import Item
from scripts.items.weapons.weapon import Weapon
import random
import math


class Sword(Weapon):
    def __init__(self, game, pos, damage_type = 'slash'):
        super().__init__(game, pos, 'sword', 3, 5, 10, 'one_handed_melee', damage_type)
        self.max_charge_time = 50
        self.max_animation = 3
        self.attack_animation_max = 3 
        self.slash_distance = 0 # Current slash distance
        self.max_slash_distance = 10 # Limit to the slashing animation distance
        # self.animation_speed = 20
        self.slash = False # Slash if True, stab if False
        self.charging = 0 # Charging value will be alligned with the entity's
        self.stored_rotation = 0 # Store the rotation for the charge

    def Update(self, offset = (0, 0)):
        if not super().Update(offset):
            return
        
    def Update_Attack(self):
        if not super().Update_Attack():
            return False
        self.Set_Block_Direction()
        
        if self.slash: # Handle Slashing
            self.attack_type = 'cut'
            self.Slash_Attack()
        else: # Handle Stabbing
            self.attack_type = 'cut'
            self.Stabbing_Attack()
    
    def Update_Animation(self):
        if not self.equipped:
            return
        

        super().Update_Animation()

    def Update_Attack_Animation(self):
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.slash_distance = 0
            return
        
        super().Update_Attack_Animation()

        


    def Set_Attack(self):
        self.slash = random.choice([True, False]) # Set either slash or stab
        return super().Set_Attack()


    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.Charge():
            return
        
        if self.special_attack <= 0 or not self.equipped:
            return
        self.Initialise_Charge()
        


        
    # Handle charging logic, return True if successful else False
    def Charge(self):
        if not self.charging:
            return False
        if self.entity.attack_direction[0] < 0:
            self.flip_image = False
        if self.entity.attack_direction[0] > 0:
            self.flip_image = True
        self.rotate = self.stored_rotation
        new_x_pos = self.entity.pos[0] + self.entity.attack_direction[0] * 10
        new_y_pos = self.entity.pos[1] + self.entity.attack_direction[1] * 10
        self.Move((new_x_pos, new_y_pos))
        self.charging = self.entity.charging
        self.enemy_hit = False
        self.Attack_Collision_Check()
        return True
    
    # Initialise the charge logic
    def Initialise_Charge(self):
        self.stored_rotation = self.rotate
        self.entity.Set_Charge(self.special_attack / 4)
        self.charging = self.entity.charging
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, 8) # Find nearby enemies to attack
        self.special_attack = 0


    # def Set_Equipped_Position(self, direction_y):
        
    #     offset_x = 0
    #     if self.entity.flip[0] and not self.attacking:
    #         self.flip_image = True
    #     else:
    #         self.flip_image = False
    #     if 'left' in self.inventory_type:
    #         if direction_y < 0:
    #             if not self.attacking:
    #                 self.rotate = 10
    #             self.Move((self.entity.pos[0] - 4, self.entity.pos[1]))
    #         else:
    #             if not self.attacking:
    #                 offset_x = self.Rotate_Left()
    #             self.Move((self.entity.pos[0] + offset_x , self.entity.pos[1]))
    #     elif 'right' in self.inventory_type:
    #         if  direction_y < 0:
    #             if not self.attacking:
    #                 self.rotate = 60
    #             self.Move((self.entity.pos[0] + 1, self.entity.pos[1]))
    #         else:
    #             if not self.attacking:
    #                 offset_x = self.Rotate_Right()
    #             self.Move((self.entity.pos[0] + offset_x, self.entity.pos[1]))
    #     else:
    #         print("DIRECTION NOT FOUND", self.inventory_type)



    # def Rotate_Left(self):
    #     if self.flip_image:
    #         offset_x = 2
    #         self.rotate = -30
    #         self.slash = False
    #     else:
    #         offset_x = 11
    #         self.rotate = 0
    #         # self.slash = True
    #     return offset_x
        
    # def Rotate_Right(self):
    #     if self.flip_image:
    #         offset_x = -11
    #         self.rotate = 0
    #         # self.slash = True
    #     else:
    #         offset_x = -2
    #         self.rotate = -30
    #         self.slash = False
    #     return offset_x

