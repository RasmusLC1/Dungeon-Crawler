from scripts.items.weapons.projectiles.projectile import Projectile
import pygame

class Fire_Particle(Projectile):
    def __init__(self, game, pos, damage, speed, shoot_distance, special_attack, direction, entity):
        super().__init__(game, pos, 'fire_particle', damage, speed, 2, 'particle', 'fire', shoot_distance, 'cut', (10, 10), False)
        self.delete_countdown = 50
        self.special_attack = special_attack 
        self.entity = entity
        self.direction = direction  # Store the direction vector
        self.attack_animation_max = 3
        self.effect = 'fire'


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
