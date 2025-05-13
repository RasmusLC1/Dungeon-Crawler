from scripts.entities.items.weapons.weapon import Weapon
import math
import pygame

class Projectile(Weapon):
    def __init__(self, game, pos, type, damage, ranged_damage, speed, range, max_charge_time, weapon_class, damage_type, shoot_distance, attack_type = 'cut', size = (32, 32), add_to_tile = True):
        super().__init__(game, pos, type, damage, speed, range, max_charge_time, weapon_class,  damage_type, attack_type, size, add_to_tile)
        self.speed = speed
        self.shoot_speed = 0
        self.ranged_damage = ranged_damage
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
        
        if self.entity.category == self.game.keys.player:
            self.Point_Towards_Mouse_Player()
        else:
            self.Point_Towards_Mouse_Enemy()

    # Run once to setup the shooting
    def Initialise_Shooting(self, speed):
        if not self.shoot_speed:
            # Set the tile, so projectile can interact with environment
            self.Set_Tile()
            # Initialise the rendering
            self.active = 255
            self.render = True
            self.render_needs_update = True
            self.Update_Dark_Surface()

            self.shoot_distance = self.shoot_distance_holder
            self.shoot_speed = speed * 2
            self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.entity, self.shoot_distance * self.shoot_speed)
            if self.entity.category == self.game.keys.enemy:
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
        self.entity = None
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
        for entity in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if entity.damage_cooldown:
                continue

            # Check for collision with enemy
            if self.rect().colliderect(entity.rect()):
                self.Entity_Hit_Ranged(entity)
                # Return enemy in case further effects need to be added such as knockback
                return entity
            
        return None
    
    # Damage Entity
    def Entity_Hit_Ranged(self, entity):
        if not self.entity:
            return
        damage = self.Calculate_Ranged_Damage()
        entity.Damage_Taken(damage, self.entity.attack_direction)
        self.enemy_hit = True

        if entity.effects.thorns.effect:
            self.entity.Damage_Taken(entity.effects.thorns.effect, self.entity.attack_direction)

        if not self.entity:
            return
        
        self.Check_Effects(damage, entity)

    def Calculate_Ranged_Damage(self):
        return self.ranged_damage * 5

    def Update_Shoot_Distance(self):
        if not self.shoot_distance:
            return False
        
        self.shoot_distance = max(0, self.shoot_distance - 1)
        return True

    def Drop_Weapon_After_Shot(self):
        # Set the attack attributes
        entity = self.entity
        self.attack_direction = entity.attack_direction
        self.entity_strength = entity.strength


        if entity.category == self.game.keys.player:
            entity.Remove_Active_Weapon()
            self.entity = entity
            self.game.inventory.Remove_Item(self)
            self.game.item_handler.Add_Item(self)
        self.in_inventory = False
        self.picked_up = False

    def Pick_Up(self):
        if self.delete_countdown and not self.pickup_allowed:
            return
        return super().Pick_Up()
