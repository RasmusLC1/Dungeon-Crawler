from scripts.decoration.decoration import Decoration
from scripts.items.item import Item
from scripts.items.weapons.weapon import Weapon
import random
import math


class Sword(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 5, 10, 'one_handed_melee')
        self.offset = 0
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
        

    def Update_Flip(self):
        pass

    
    def Update_Animation(self):
        if not self.equipped:
            return
        

        super().Update_Animation()

    def Update_Attack_Animation(self):
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.slash_distance = 0
            self.rotate = 0
            return
        
        super().Update_Attack_Animation()

        self.Point_Towards_Mouse()
        self.Set_Attack_Direction()
        
        if self.slash:
            self.sub_type = 'sword_attack'
            self.Slash_Attack()
        else:
            self.sub_type = 'sword'
            self.Stabbing_Attack()


    def Slash_Attack(self):
            
            x_offset = 0
            y_offset = 0
            if not self.return_to_holder:
                if self.slash_distance <= self.max_slash_distance:
                    self.slash_distance += 1
                else:
                    self.return_to_holder = True
            else:
                if self.slash_distance <= 0:
                    self.return_to_holder = False
                else:
                    self.slash_distance -= 1
            new_x_pos = (0,0)
            new_y_pos = (0,0)
            # Condition for if x coordinate is dominant
            if abs(self.attack_direction[0]) >= abs(self.attack_direction[1]):
                y_offset = -5
                

                if self.attack_direction[0] < 0:
                    self.pos = self.entity.rect().midleft
                    x_offset = -5
                else:
                    x_offset = -2
                    self.pos = self.entity.rect().midright
                new_x_pos = int(self.pos[0]) + x_offset
                new_y_pos = int(self.pos[1]) + y_offset - self.slash_distance + y_offset
            # Dominant y coordinate
            else:
                
                self.pos = self.entity.rect().center
                if self.attack_direction[1] >= 0:
                    y_offset = -13
                else:
                    y_offset = - 20
                x_offset = -5
                new_x_pos = int(self.pos[0]) + x_offset + self.slash_distance
                new_y_pos = int(self.pos[1]) + y_offset
                    
            
            self.Move((new_x_pos, new_y_pos))

            if self.slash_distance <= self.range:
                return
            elif self.slash_distance > self.range:
                self.return_to_holder = True
                return


    def Stabbing_Attack(self):
        if not self.return_to_holder:
            self.slash_distance += 1
            y_offset = 0
            if abs(self.attack_direction[0]) >= abs(self.attack_direction[1]):
                y_offset = -5

                if self.attack_direction[0] < 0:
                    self.pos = self.entity.rect().topleft
                else:
                    self.pos = self.entity.rect().topright
            else:
                self.pos = self.entity.rect().center
                y_offset = - 15
                    
            new_x_pos = int(self.pos[0]) + self.slash_distance * self.attack_direction[0]
            new_y_pos = int(self.pos[1]) + self.slash_distance * self.attack_direction[1] + y_offset
            self.Move((new_x_pos, new_y_pos))

            if self.slash_distance <= self.range:
                return
            elif self.slash_distance > self.range:
                self.return_to_holder = True
                return
        else:
            self.slash_distance -= 1

            if self.slash_distance <= 0:
                self.return_to_holder = False


    def Set_Attack(self):
        self.slash = random.choice([True, False]) # Set either slash or stab
        return super().Set_Attack()

    def Update_Flip(self):
        pass
    
    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.Charge():
            return
        
        if self.special_attack <= 0 or not self.equipped:
            return
        self.Initialise_Charge()
        


        
    # Handle charging logic, return True if successfull else False
    def Charge(self):
        if not self.charging:
            return False
        if self.attack_direction[0] < 0:
            self.flip_image = False
        if self.attack_direction[0] > 0:
            self.flip_image = True
        self.rotate = self.stored_rotation
        new_x_pos = self.entity.pos[0] + self.attack_direction[0] * 10
        new_y_pos = self.entity.pos[1] + self.attack_direction[1] * 10 - 10
        self.Move((new_x_pos, new_y_pos))
        self.charging = self.entity.charging
        self.enemy_hit = False
        self.Attack_Collision_Check()
        return True
    
    # Initialise the charge logic
    def Initialise_Charge(self):
        print(self.charge_time, self.special_attack, self.entity.type)
        self.Point_Towards_Mouse()
        self.stored_rotation = self.rotate
        self.entity.Set_Charge(self.special_attack / 8)
        self.charging = self.entity.charging
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, self.special_attack) # Find nearby enemies to attack
        self.special_attack = 0


    def Set_Equipped_Position(self, direction_y):
        
        offset_x = 0
        if self.entity.flip[0] and not self.attacking:
            self.flip_image = True
        else:
            self.flip_image = False
        if 'left' in self.inventory_type:
            if direction_y < 0:
                if not self.attacking:
                    self.rotate = 10
                self.Move((self.entity.pos[0] - 4, self.entity.pos[1] - 12))
            else:
                if not self.attacking:
                    offset_x = self.Rotate_Left()
                self.Move((self.entity.pos[0] + offset_x , self.entity.pos[1] - 5))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                if not self.attacking:
                    self.rotate = 60
                self.Move((self.entity.pos[0] + 1, self.entity.pos[1] - 12))
            else:
                if not self.attacking:
                    offset_x = self.Rotate_Right()
                self.Move((self.entity.pos[0] + offset_x, self.entity.pos[1] - 5))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

    def Point_Towards_Mouse(self):
        self.rotate = 0

        dx = self.game.mouse.mpos[0] - self.entity.pos[0]
        dy = self.game.mouse.mpos[1] - self.entity.pos[1]
        # Calculate the angle in degrees

        self.rotate = math.degrees(math.atan2(dy, dx)) + 45
        self.rotate *= -1

    def Rotate_Left(self):
        if self.flip_image:
            offset_x = 2
            self.rotate = -30
            self.slash = False
        else:
            offset_x = 11
            self.rotate = 0
            # self.slash = True
        return offset_x
        
    def Rotate_Right(self):
        if self.flip_image:
            offset_x = -11
            self.rotate = 0
            # self.slash = True
        else:
            offset_x = -2
            self.rotate = -30
            self.slash = False
        return offset_x

