import pygame
from scripts.engine.assets.keys import keys
import random

class Player_Weapon_Attack():
    def __init__(self, game, weapon):
        self.game = game
        self.weapon = weapon
        
        self.attacking = 0
        self.attack_hitbox_size = (10, 10)
        self.attack_hitbox = pygame.Rect(self.weapon.pos[0], self.weapon.pos[1], self.attack_hitbox_size[0], self.attack_hitbox_size[1])

        self.entities_hit = [] # Enemies which have been hit by an attack
        self.nearby_enemies = [] # Nearby enemies that the weapon can interact with
        self.nearby_decoration = [] # Nearby decoration that the weapon can interact with
        self.player = self.game.player

    # Update the attack logic
    def Update_Attack(self):
        if not self.attacking:
            return False

        entity = self.Attack_Collision_Check()

        self.attacking -= 1
        self.player.Reduce_Movement(4) # Reduce movement to a quarter when attacking
        return True
    


    # Initialise the attack and reset attack values
    def Set_Attack(self):
        if not self.Check_Entity_Cooldown():
            return False
        self.Reset_Entities_Hit()
        
        # Compute attack each time to account for changing player agility level
        self.attacking = max(int((self.weapon.speed * 30) // self.player.agility), self.weapon.attack_animation_max) 
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.player, 3) # Find nearby enemies to attack
        self.nearby_decoration = self.game.decoration_handler.Find_Nearby_Decorations(self.player.pos, 3)
        return True
    
    def Attack_Collision_Check(self):
        self.Set_Attack_Hitbox()

        if not self.weapon.Check_Tile(self.attack_hitbox.center):
            self.Reset_Attack()

        enemy_hit = self.Enemy_Collision()        
        if enemy_hit:
            return enemy_hit
        return self.Decoration_Collision()
    

    def Enemy_Collision(self):
        for enemy in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if enemy.damage_cooldown:
                continue
            # Prevent from hitting enemy multiple times
            if enemy in self.entities_hit:
                continue
            # Check for collision with enemy
            # print(self.attack_hitbox.size, self.attack_hitbox.colliderect(enemy.rect()))
            if self.attack_hitbox.colliderect(enemy.rect()):
                self.weapon.Entity_Hit(enemy)
                self.entities_hit.append(enemy)

                # Return enemy in case further effects need to be added such as knockback
                return enemy
            
        return None
    
    def Decoration_Collision(self):
        for decoration in self.nearby_decoration:
            # Check if the decoration can be damaged
            if not decoration.destructable:
                continue
            # Prevent from hitting decoration multiple times
            if decoration in self.entities_hit:
                continue
            # Check for collision with enemy
            if self.attack_hitbox.colliderect(decoration.rect()):
                decoration.Damage_Taken(self.weapon.damage_handler.Calculate_Damage(), self.weapon.effect)
                return decoration
        
        return None
    
        # Return False if player weapon cooldown is not off
    def Check_Entity_Cooldown(self):
        if self.player.left_weapon_cooldown:
            return False
        return True

    def Reset_Attack(self):
        if not self.attacking <= 1:
            return False
        
        self.attacking = 0
        self.weapon.Reset_Attack_Animation()

        return True
    
    # Compute the hitbox for the weapon when attacking
    def Set_Attack_Hitbox(self):
        if not self.player:
            return
            
        pos_x = self.weapon.rect().center[0] - 2 + self.player.attack_direction[0] * self.game.tilemap.tile_size
        pos_y = self.weapon.rect().center[1] - 2 + self.player.attack_direction[1] * self.game.tilemap.tile_size
        self.attack_hitbox = pygame.Rect(pos_x, pos_y, self.attack_hitbox_size[0] * self.weapon.range, self.attack_hitbox_size[1] * self.weapon.range)
        
    
    def Reset_Entities_Hit(self):
        self.entities_hit.clear()