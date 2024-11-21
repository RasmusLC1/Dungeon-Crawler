from scripts.decoration.decoration import Decoration
from scripts.items.item import Item
from scripts.items.weapons.weapon import Weapon
import random
import math

class Sword(Weapon):
    def __init__(self, game, pos, damage_type = 'slash'):
        super().__init__(game, pos, 'sword', 3, 6, 5, 'one_handed_melee', damage_type)
        self.max_charge_time = 50
        self.max_animation = 3
        self.attack_animation_max = 3 

        
    def Update_Attack(self):
        if not super().Update_Attack():
            return False
        self.Set_Block_Direction()
        self.Set_Attack_Type()
        
        
    def Set_Attack_Type(self):
        if self.attack_type == 'cut': # Handle Slashing
            self.Slash_Attack()
        else: # Handle Stabbing
            self.Stabbing_Attack() 
    
    def Set_Equipped_Position(self, direction_y):
        if 'left' in self.inventory_type:
            if direction_y < 0:
                self.Move((self.entity.pos[0] - 5 , self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] + 5 , self.entity.pos[1]))
        elif 'right' in self.inventory_type:
            if  direction_y < 0:
                self.Move((self.entity.pos[0] + 7, self.entity.pos[1]))
            else:
                self.Move((self.entity.pos[0] - 7, self.entity.pos[1]))
        else:
            print("DIRECTION NOT FOUND", self.inventory_type)

    def Set_Attack(self):
        self.attack_type = random.choice(['cut', 'stab']) # Set either cut or stab
        return super().Set_Attack()


    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.Charge():
            return
        
        if self.special_attack <= 0 or not self.equipped:
            self.Reset_Special_Attack()
            return
        self.Initialise_Charge()
        


        
    # Handle charging logic, return True if successful else False
    def Charge(self):
        if not self.entity.charging:
            return False
        self.rotate = self.stored_rotation
        new_x_pos = self.entity.pos[0] + self.entity.attack_direction[0] * 10
        new_y_pos = self.entity.pos[1] + self.entity.attack_direction[1] * 10
        self.Move((new_x_pos, new_y_pos))
        self.enemy_hit = False
        self.Attack_Collision_Check()
        return True
    
    # Initialise the charge logic
    def Initialise_Charge(self):
        self.stored_rotation = self.rotate
        self.entity.Set_Charge(self.special_attack // 4)
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, 8) # Find nearby enemies to attack
        self.special_attack = 0
