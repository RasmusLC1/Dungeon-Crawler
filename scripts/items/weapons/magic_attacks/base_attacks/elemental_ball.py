from scripts.items.weapons.projectiles.projectile import Projectile
import pygame

class Elemental_Ball(Projectile):
    def __init__(self, game, pos, entity, type, damage, speed, range, damage_type, shoot_distance, special_attack, direction):
        super().__init__(game, pos, type, damage, speed, range, 'magic_projectile', damage_type, shoot_distance, 'cut', (16, 16), False)
        self.special_attack = special_attack
        
        self.entity = entity
        self.attack_direction = direction  # Store the direction vector
        self.delete_countdown = 100
        self.pickup_allowed = False

        
    
    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass


    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(self.speed)       

        self.rotate += 5
        super().Shoot()

    def Reset_Shot(self):
        self.delete_countdown = 1
        return super().Reset_Shot()


        # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        weapon_image = pygame.transform.rotate(weapon_image, self.rotate)


        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
