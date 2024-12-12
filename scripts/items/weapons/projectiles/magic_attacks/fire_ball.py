from scripts.items.weapons.projectiles.projectile import Projectile
from scripts.items.weapons.projectiles.magic_attacks.fire_explosion import Fire_Explosion
import math
import pygame
import inspect

class Fire_Ball(Projectile):
    def __init__(self, game, pos, entity, damage, speed, special_attack, direction):
        super().__init__(game, pos, 'fire_ball', damage, speed, 2, 'magic_projectile', 'fire', 200, 'cut', (16, 16), False)
        self.special_attack = special_attack
        
        self.entity = entity
        self.attack_direction = direction  # Store the direction vector
        self.target_hit = 0
        self.delete_countdown = 100
        self.pickup_allowed = False
        self.light_source = self.game.light_handler.Add_Light(self.pos, 5, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)
        self.update_light_cooldown = 0

        
    
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass

    def Update_Light(self):
        if self.update_light_cooldown >= 30:
            self.light_source.Move_Light(self.pos, self.tile)
            self.update_light_cooldown = 0
            return
        
        self.update_light_cooldown += 1


    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        self.Update_Light()
       
        if self.target_hit:
            self.target_hit -= 1
            if not self.target_hit:
                self.Set_Special_Attack(0)
            return

        self.rotate += 5
        super().Shoot()

    def Reset_Shot(self):
        fire_explosion = Fire_Explosion(self.game, self.pos, self.damage)
        self.game.item_handler.Add_Item(fire_explosion)
        self.delete_countdown = 1
        self.game.light_handler.Remove_Light(self.light_source)
        return super().Reset_Shot()

    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
