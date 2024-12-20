from scripts.items.weapons.projectiles.projectile import Projectile
import pygame
import random

class Electric_Particle(Projectile):
    def __init__(self, game, pos, damage, speed, shoot_distance, special_attack, direction, entity):
        super().__init__(game, pos, 'electric_particle', damage, speed, 1, 'particle', 'electric', shoot_distance, 'cut', (10, 10), False)
        self.special_attack = special_attack
        self.entity = entity
        self.direction = direction  # Store the direction vector
        self.attack_animation_max = 3
        self.delete_countdown = 100
        self.attack_animation_time = shoot_distance // self.attack_animation_max
    
    def Initialise_Shooting(self, speed):
        return_value = super().Initialise_Shooting(speed)
        entity = random.choice(self.nearby_enemies)
        self.direction = pygame.math.Vector2(entity.pos[0] - self.pos[0], entity.pos[1] - self.pos[1])
        return return_value

    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        # Use the stored direction to move the particle
        self.pos = (
            self.pos[0] + self.direction[0] * self.shoot_speed,
            self.pos[1] + self.direction[1] * self.shoot_speed
        )

        entity = super().Shoot()
        if entity:
            self.Set_Special_Attack(0)
            


    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass

        
        

    
    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):

        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

