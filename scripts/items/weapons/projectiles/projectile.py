from scripts.items.weapons.weapon import Weapon
import math
import pygame

class Projectile(Weapon):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, damage_type):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class,  damage_type)
        self.shoot_speed = 0
        self.pickup_allowed = True
        self.range_holder = range


    def Load_Data(self, data):
        
        super().Load_Data(data)
        self.range_holder = self.range


    def Set_Special_Attack(self, offset= (0,0)):
        super().Set_Special_Attack(offset)
        self.Point_Towards_Mouse()

    def Initialise_Shooting(self, speed):
        if not self.shoot_speed:
            self.range = self.range_holder
            self.active = 255
            self.shoot_speed = speed
            self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, self.special_attack * 2)
            return True
        return False


    def Shoot(self):
        if not self.Update_Range():
            self.shoot_speed = 0
            self.special_attack = 0
            return  

        dir_x = self.pos[0] + self.entity.attack_direction[0] * self.shoot_speed
        dir_y = self.pos[1] + self.entity.attack_direction[1] * self.shoot_speed
        
        if not self.Check_Tile((dir_x, dir_y)):
            self.special_attack = 0
            self.range = 0
            self.shoot_speed = 0
            return None
        self.Move((dir_x, dir_y))
        # Check for collision with enemy
        entity = self.Attack_Collision_Check()
        if entity:
            self.special_attack = 0
            self.range = 0
            self.shoot_speed = 0
            return entity
        return None

    def Update_Range(self):
        if not self.range:
            return False
        
        self.range = max(0, self.range - 1)
        return True

    def Drop_Weapon_After_Shot(self):
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        if self.entity.type == 'player':
            self.entity.Remove_Active_Weapon(self.inventory_type)
            weapon_inventory.Remove_Item(self, True)
            self.game.item_handler.Add_Item(self)
        self.game.entities_render.Add_Entity(self)
        self.picked_up = False
        self.equipped = False
        self.in_inventory = False

    def Pick_Up(self):
        if self.delete_countdown:
            return
        return super().Pick_Up()

    # For some reason calling the parent function does not work for render
    def Render(self, surf, offset=(0, 0)):
        
        # Check if item is in inventory. If yes we don't need offset, except if
        # the weapon has been picked up
        if self.in_inventory:

            if self.picked_up:
                self.Render_In_Inventory(surf)
        
        if not self.Update_Light_Level():
            return
        
        weapon_image = self.game.assets[self.type][self.animation].convert_alpha()

        if self.special_attack:
            weapon_image = pygame.transform.rotate(weapon_image, self.rotate)

        
        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))


        if not alpha_value:
            return
        
        weapon_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        weapon_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        
