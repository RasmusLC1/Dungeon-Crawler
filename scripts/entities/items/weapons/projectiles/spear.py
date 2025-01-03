from scripts.entities.items.weapons.projectiles.projectile import Projectile
import math
import pygame

class Spear(Projectile):
    def __init__(self, game, pos, damage_type = 'slash'):
        super().__init__(game, pos, 'spear', 3, 6, 8, 50, 'two_handed_melee', damage_type, 30, 'stab')
        self.max_animation = 3
        self.attack_animation_max = 3
        self.distance_from_player = 0
        
    

    def Shoot(self):
        self.Initialise_Shooting(self.entity_strength)

        super().Shoot()

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_After_Shot()

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()

        
        

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



