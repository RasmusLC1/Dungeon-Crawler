from scripts.entities.items.weapons.weapon import Weapon
import math
import pygame

class Bow(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 8, 10, 'bow')
        self.max_animation = 0
        self.attack_animation_max = 2
        self.distance_from_player = 0
        self.attack_animation_counter
        
    

    def Set_Attack(self):
        pass
    
    def Update_Animation(self):
        if self.is_charging:
            return
        super().Update_Animation()
        

    def Update_Attack_Animation(self):
        self.sub_type = self.type + '_attack'
        self.animation = self.attack_animation
        
    def Charge_Attack(self, offset = (0, 0)):
        if not self.inventory_type:
            return
        
        
        self.Set_Charging()
        if self.is_charging:
            self.Update_Attack_Animation()
            if not self.charge_time:
                self.attack_animation_time = self.max_charge_time // (self.attack_animation_max + 1)
            # Increase charge time while holding the button
            self.charge_time += 1
            if self.charge_time >= self.max_charge_time:
                self.charge_time = self.max_charge_time  # Cap the charge time
                self.charged_attack = True  # Mark the attack as charged
            else:
                self.attack_animation_counter += 1
                if self.attack_animation_time <= self.attack_animation_counter:
                    self.attack_animation_counter = 0
                    self.attack_animation = min(self.attack_animation_max, self.attack_animation + 1)

        elif self.charge_time > 0:
            if self.attack_animation > 0:
                print("SHOOT")

            self.charge_time = 0
            self.animation = 0
            self.attack_animation_counter = 0
            self.attack_animation = 0

            
    def Set_Charging(self):
        super().Set_Charging()


    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        print(self.special_attack)

    

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
