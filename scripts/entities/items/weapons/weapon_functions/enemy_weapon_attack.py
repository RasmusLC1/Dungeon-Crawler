import pygame
from scripts.engine.assets.keys import keys

class Enemy_Weapon_Attack():
    def __init__(self, game, weapon):
        self.game = game
        self.weapon = weapon
        
        self.attacking = 0


    # Update the attack logic
    def Update_Attack(self):
        if not self.attacking:
            return False

        self.attacking -= 1


        self.weapon.entity.Reduce_Movement(4) # Reduce movement to a quarter when attacking
        return False
    
    # Initialise the attack and reset attack values
    def Set_Attack(self):
        if not self.Check_Entity_Cooldown():
            return
        entity = self.weapon.entity
        self.attacking = max(int((self.weapon.speed * 30) // entity.agility), self.weapon.attack_animation_max) 
        self.attack_animation_time = int(self.attacking / self.weapon.attack_animation_max)
        if entity.distance_to_player > self.game.tilemap.tile_size * 1.5:
            return
        self.weapon.Entity_Hit(self.game.player)

    def Reset_Attack(self):
        if not self.attacking <= 1:
            return False
        
        self.attacking = 0
        self.weapon.Reset_Attack_Animation()

        return True
        
    # Return False if entity weapon cooldown is not off
    def Check_Entity_Cooldown(self):
        if self.weapon.entity.left_weapon_cooldown:
            return False
        return True
