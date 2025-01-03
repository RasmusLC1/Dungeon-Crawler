from scripts.entities.items.weapons.weapon import Weapon
import math
import pygame

class Projectile(Weapon):
    def __init__(self, game, pos, type, damage, speed, range, max_charge_time, weapon_class, damage_type, shoot_distance, attack_type = 'cut', size = (32, 32), add_to_tile = True):
        super().__init__(game, pos, type, damage, speed, range, max_charge_time, weapon_class,  damage_type, attack_type, size, add_to_tile)
        self.speed = speed
        self.shoot_speed = 0
        self.shoot_distance = shoot_distance
        self.pickup_allowed = True
        self.shoot_distance_holder = shoot_distance
        self.entity_strength = 0
        self.attack_direction = (0, 0)
        self.is_projectile = True


    def Save_Data(self):
        super().Save_Data()
        self.saved_data['shoot_speed'] = self.shoot_speed
        self.saved_data['shoot_distance'] = self.shoot_distance
        self.saved_data['shoot_distance_holder'] = self.shoot_distance_holder


    def Load_Data(self, data):
        
        super().Load_Data(data)
        self.shoot_distance = data['shoot_distance'] 
        self.shoot_distance_holder = data['shoot_distance_holder'] 
        self.shoot_speed = data['shoot_speed']


    def Set_Special_Attack(self, offset= (0,0)):
        super().Set_Special_Attack(offset)
        if not self.entity:
            return
        
        if self.entity.category == 'player':
            self.Point_Towards_Mouse_Player()
        else:
            self.Point_Towards_Mouse_Enemy()

    # Run once to setup the shooting
    def Initialise_Shooting(self, speed):
        if not self.shoot_speed:
            self.render = True
            self.shoot_distance = self.shoot_distance_holder
            self.active = 255
            self.shoot_speed = speed * 2
            self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, self.shoot_distance * self.shoot_speed)
            if self.entity.category == "enemy":
                self.nearby_enemies.append(self.game.player)

            return True
        return False


    # Continously updated shooting effect
    def Shoot(self):
        if not self.Update_Shoot_Distance():
            self.Reset_Shot()
            return
       

        dir_x = self.pos[0] + self.attack_direction[0] * self.shoot_speed
        dir_y = self.pos[1] + self.attack_direction[1] * self.shoot_speed

        self.Update_Tile(self.pos)
        if not self.Check_Tile((dir_x, dir_y)):
            self.Reset_Shot()
            return None
        self.Move((dir_x, dir_y))
        entity_hit = None
        # Check for collision with enemy
        entity_hit = self.Attack_Collision_Check_Projectile()
        if entity_hit:
            self.Reset_Shot()
            return entity_hit
        return None
    
    # Reset the weapon after the maximum distance has been rached
    def Reset_Shot(self):
        self.shoot_speed = 0
        self.special_attack = 0
        self.shoot_speed = 0
        self.picked_up = False
        self.equipped = False
        self.in_inventory = False
        self.Set_Entity(None)
        return True

    # Check for collision on attack
    def Attack_Collision_Check_Projectile(self):
        for enemy in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if enemy.damage_cooldown:
                continue

            # Check for collision with enemy
            if self.rect().colliderect(enemy.rect()):
                self.Entity_Hit(enemy)
                # Return enemy in case further effects need to be added such as knockback
                return enemy
            
        return None

    def Update_Shoot_Distance(self):
        if not self.shoot_distance:
            return False
        
        self.shoot_distance = max(0, self.shoot_distance - 1)
        return True

    def Drop_Weapon_After_Shot(self):
        active_inventory = self.game.weapon_inventory.active_inventory
        weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
        if self.entity.category == 'player':
            self.entity.Remove_Active_Weapon(self.inventory_type)
            weapon_inventory.Remove_Item(self, True)
            self.game.item_handler.Add_Item(self)
        self.attack_direction = self.entity.attack_direction
        self.entity_strength = self.entity.strength
        self.in_inventory = False
        self.picked_up = False

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
        
