from scripts.entities.items.weapons.projectiles.projectile import Projectile
import math
import pygame

class Spear(Projectile):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type, 3, 8, 10, 'two_handed_melee')
        self.max_animation = 3
        self.attack_animation_max = 3
        self.return_to_holder = False # Return the weapon to original positon after thrust
        self.distance_from_player = 0
        
    

    def Set_Attack(self):
        super().Set_Attack()
        if self.attacking == 0 or self.range == 0 or self.attack_animation_time == 0:
            return
        self.attack_animation_time = int(self.attacking / self.range / self.attack_animation_time) 
    
    def Shoot(self):
        self.Initialise_Shooting(self.entity.strength)

        super().Shoot()

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_After_Shot()

    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            self.rotate = 0
            return
        
        # Not updating the animation as the timer hasn't been hit yet
        if not self.attack_animation_counter >= self.attack_animation_time - 1:
            return
        self.Stabbing_Attack()

    # def Update_Flip(self):
    #     pass
        
