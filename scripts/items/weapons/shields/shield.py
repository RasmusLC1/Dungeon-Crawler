from scripts.items.weapons.weapon import Weapon


import math
class Shield(Weapon):
    def __init__(self, game, pos, size, damage_type = 'block'):
        super().__init__(game, pos, size, 'shield', 2, 5, 2, 'shield', damage_type)
        self.charging = 0 # Charging value will be alligned with the entity's

    
    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.Charge():
            return
        
        if self.special_attack <= 0 or not self.equipped:
            return
        self.Initialise_Charge()

    def Set_Attack(self):
        pass
      

    def Charge_Attack(self, offset = (0, 0)):
        try:
            # Check that the weapon is in a weapon inventory
            if not self.inventory_type:
                return
            self.Set_Charging_Player()
            self.Player_Shooting()
        except TypeError as e:
            print(f"Entity neither enemy nor player: {e}")
        
        if not self.inventory_type:
            return

        self.Set_Charging_Player()


    def Set_Equipped_Position(self, direction_y):
        
        offset_x = 0
        if self.entity.flip[0] and not self.attacking:
            self.flip_image = True
        else:
            self.flip_image = False
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.entity.pos[0] - 4, self.entity.pos[1] - 12))
            else:
                if not self.attacking:
                    offset_x = self.Rotate_Left()
                self.Move((self.entity.pos[0] + offset_x , self.entity.pos[1]))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.entity.pos[0] + 1, self.entity.pos[1] - 12))
            else:
                if not self.attacking:
                    offset_x = self.Rotate_Right()
                self.Move((self.entity.pos[0] + offset_x, self.entity.pos[1]))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)




    def Rotate_Left(self):
        if self.flip_image:
            offset_x = 2
        else:
            offset_x = -4
            # self.slash = True
        return offset_x
        
    def Rotate_Right(self):
        if self.flip_image:
            offset_x = -4
        else:
            offset_x = 4
        return offset_x

    def Update_Flip(self):
        pass