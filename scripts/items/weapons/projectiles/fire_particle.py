from scripts.items.weapons.projectiles.projectile import Projectile
import pygame

class Fire_Particle(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, special_attack, direction, entity):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class, 'fire')
        self.delete_countdown = 30
        self.special_attack = special_attack / 4
        self.entity = entity
        self.direction = direction  # Store the direction vector
        self.attack_animation_max = 3
        self.effect = 'fire'


    def Shoot(self):
        
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)

        # Use the stored direction to move the particle
        dir = (
            self.pos[0] + self.direction[0] * self.shoot_speed,
            self.pos[1] + self.direction[1] * self.shoot_speed
        )
        if not self.Check_Tile(dir):
            self.special_attack = 0
            self.range = 0
            return None
    
        # entity = super().Shoot()
        self.Move(dir)
        # Check for collision with enemy
        entity = self.Attack_Collision_Check()
        if entity:
            self.special_attack = 0
            self.range = 0
            return entity
        return None
        
        
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass
    
    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):

        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
