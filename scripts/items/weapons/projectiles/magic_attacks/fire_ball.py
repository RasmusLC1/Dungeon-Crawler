from scripts.items.weapons.projectiles.projectile import Projectile
from scripts.items.weapons.projectiles.magic_attacks.fire_explosion import Fire_Explosion
import math
import pygame

class Fire_Ball(Projectile):
    def __init__(self, game, pos, entity, damage, speed, special_attack, direction):
        super().__init__(game, pos, 'fire_ball', damage, speed, 2, 'magic_projectile', 'fire', 200, 'cut', (16, 16), False)
        self.special_attack = special_attack
        self.entity = entity
        self.attack_direction = direction  # Store the direction vector
        self.target_hit = 0
        self.delete_countdown = 100
        self.attack_animation_max = 3
        self.attack_animation_time = shoot_distance // self.attack_animation_max

        
    
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass

    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        if self.target_hit:
            self.target_hit -= 1
            if not self.target_hit:
                self.Set_Special_Attack(0)
            return

        self.rotate += 5
        super().Shoot()
        if not self.special_attack:
            fire_explosion = Fire_Explosion(self.game, self.pos, self.damage)


    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):

        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
