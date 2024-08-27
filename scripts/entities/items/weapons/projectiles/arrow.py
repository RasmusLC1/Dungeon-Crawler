from scripts.entities.items.weapons.projectiles.projectile import Projectile
import math
import pygame

class Arrow(Projectile):
    def __init__(self, game, pos, size, type, entity):
        super().__init__(game, pos, size, type, 2, 2, 10, 'arrow')
        self.max_animation = 0
        self.attack_animation_max = 0
        self.distance_from_player = 0
        self.entity = entity
        self.equipped = True
        self.in_inventory = True
        self.attacking = 10
        self.picked_up = True
        self.game.entities_render.Remove_Entity(self)

    
    def Update(self, offset=...):
        return super().Update(offset)
    
    def Set_Speed(self, speed):
        self.speed += speed
    
    def Set_Damage(self, damage):
        self.damage = damage
    

    def Update_Flip(self):
        pass


    def Shoot(self):
        # print(self.rotate, self.special_attack)
        self.Initialise_Shooting(self.entity.strength)


        super().Shoot()

    def Set_Equipped_Position(self, direction_y = 0):
        if self.entity.attack_direction[0] < 0:
            self.Move((self.entity.pos[0] - 4, self.entity.pos[1] - 3))
        else:
            self.Move((self.entity.pos[0] + 7, self.entity.pos[1] - 3))
        self.Set_Attack_Direction()
        self.Point_Towards_Mouse()

    def Set_Special_Attack(self, charge_time, offset = (0, 0)):
        self.charge_time = charge_time

        return super().Set_Special_Attack(offset)

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_After_Shot()

    def Point_Towards_Mouse(self):
        super().Point_Towards_Mouse()
        if self.entity.attack_direction[0] < 0:
            self.rotate += 90
            self.flip_image = True
            pass
        else:
            self.rotate -= 90
            self.rotate *= -1
            self.flip_image = False


    def Update_Attack_Animation(self):
        super().Update_Attack_Animation()
        # Reset the attack logic
        if not self.attacking:
            self.return_to_holder = False
            self.distance_from_player = 0
            self.rotate = 0
            return

        self.Stabbing_Attack_Handler()


        
    def Arrow_Inventory_Check(self, inventory_slot):
        if not 'arrow' in self.weapon_class:
            return True
        
        if not inventory_slot.inventory_type:
            return True
        if 'arrow' in inventory_slot.inventory_type:
            return True
        else:
            return False