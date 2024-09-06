from scripts.items.weapons.projectiles.projectile import Projectile
import math
import pygame

class Arrow(Projectile):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size, 'arrow', 2, 2, 10, 'arrow')
        self.max_animation = 0
        
        self.max_amount = 20
        self.amount = 1


    
    def Set_Speed(self, speed):
        self.speed += speed

    def Update_Flip(self):
        pass

    def Shooting_Setup(self, entity):
        self.attack_animation_max = 0
        self.distance_from_player = 0
        self.entity = entity
        self.equipped = True
        self.in_inventory = True
        self.picked_up = True
        self.attacking = 10
        self.game.entities_render.Remove_Entity(self)


    def Shoot(self):
        self.Initialise_Shooting(self.entity.strength)
        if not self.special_attack:
            return None
        return self.Collision_Detection()   

    def Collision_Detection(self):
        dir_x = self.pos[0] + self.attack_direction[0] * self.shoot_speed
        dir_y = self.pos[1] + self.attack_direction[1] * self.shoot_speed
        
        if not self.Check_Tile((dir_x, dir_y)):
            self.special_attack = 0
            self.game.item_handler.Remove_Item(self, True)
            return None
        
        self.Move((dir_x, dir_y))
        # Check for collision with enemy
        entity = self.Attack_Collision_Check()
        if entity:
            self.special_attack = 0
            self.game.item_handler.Remove_Item(self, True)
            return entity
        self.special_attack = max(0, self.special_attack - self.shoot_speed)
        return None   

    def Set_Equipped_Position(self, direction_y = 0):
        if not self.entity:
            return
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

    def Send_To_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):
        if not self.Arrow_Inventory_Check(inventory_slot):
            return False
        return super().Send_To_Inventory(inventory_slot, sending_inventory, receiving_inventory)


        
    def Arrow_Inventory_Check(self, inventory_slot):
        if not 'arrow' in self.weapon_class:
            return True
        
        if not inventory_slot.inventory_type:
            return True
        if 'arrow' in inventory_slot.inventory_type:
            return True
        else:
            return False