from scripts.decoration.decoration import Decoration
from scripts.entities.items.item import Item
from scripts.entities.items.weapons.weapon import Weapon
import random
import math


class Sword(Weapon):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 5, 10, 'one_handed_melee')
        self.offset = 0
        self.max_animation = 3
        self.attack_animation_max = 3
        self.distance_from_player = 0

        # self.animation_speed = 20
        self.slash = False # Slash if True, stab if False

    def Update_Flip(self):
        pass

    
    def Update_Animation(self):
        if not self.equipped:
            return
        

        super().Update_Animation()

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        self.Point_Towards_Mouse()
        if self.slash and self.attacking:
            self.sub_type = 'sword_attack'
        else:
            self.sub_type = 'sword'
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            self.rotate = 0
            return
        
        self.Stabbing_Attack_Handler()
        
        

    def Stabbing_Attack_Handler(self):
        # if not self.rotate:  

        self.Stabbing_Attack_Direction()
        self.Stabbing_Attack()

    def Stabbing_Attack_Direction(self):
        self.entity.Attack_Direction_Handler(self.game.render_scroll)
        self.attack_direction = self.entity.attack_direction
        # self.attack_direction = pygame.math.Vector2(self.attack_direction[0], self.attack_direction[1])
        self.attack_direction.normalize_ip()

    

    def Stabbing_Attack(self):
        if not self.return_to_holder:
            self.distance_from_player += 1
            y_offset = 0
            if abs(self.attack_direction[0]) >= abs(self.attack_direction[1]):
                y_offset = -5

                if self.attack_direction[0] < 0:
                    self.pos = self.entity.rect().topleft
                else:
                    self.pos = self.entity.rect().topright
            else:
                if self.attack_direction[1] < 0:
                    self.pos = self.entity.rect().center
                    y_offset = - 8
                else:
                    y_offset = 5
                    
            new_x_pos = int(self.pos[0]) + self.distance_from_player * self.attack_direction[0]
            new_y_pos = int(self.pos[1]) + self.distance_from_player * self.attack_direction[1] + y_offset
            self.Move((new_x_pos, new_y_pos))

            if self.distance_from_player <= self.range:
                return
            elif self.distance_from_player > self.range:
                self.return_to_holder = True
                return
        else:
            self.distance_from_player -= 1

            if self.distance_from_player <= 0:
                self.return_to_holder = False



        

    def Set_Attack(self):
        # self.slash = random.choice([True, False]) # Set either slash or stab
        return super().Set_Attack()

    def Update_Flip(self):
        pass

    def Modify_Offset(self, change):
        self.offset -= change
        print(self.offset)

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

