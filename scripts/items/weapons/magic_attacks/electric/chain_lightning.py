from scripts.items.weapons.magic_attacks.electric.electric_particle import Electric_Particle
import pygame
import math
class Chain_Lightning(Electric_Particle):
    def __init__(self, game, pos, entity, damage, speed, shoot_distance, special_attack, direction, effect):
        super().__init__(game, pos, damage, speed, shoot_distance, special_attack, direction, entity)
        self.shots_left = effect * 3
        self.reset_shot = False

    def Initialise_Shooting(self, speed):
        return_value = super().Initialise_Shooting(speed)
        self.Shoot_Enemy()

        
        return return_value

    def Shoot(self):
        entity = super().Shoot()
        if entity:
            self.nearby_enemies.pop(0)
            self.special_attack = 100
            self.Shoot_Enemy()

    def Reset_Shot(self):
        if not self.reset_shot:
            return
        self.delete_countdown = 1
        super().Reset_Shot()
    
    def Check_Tile(self, new_pos):
        tile_hit = super().Check_Tile(new_pos)

        # Wall has been hit
        if not tile_hit:
            self.reset_shot = True

        return tile_hit

    def Shoot_Enemy(self):
        if not self.nearby_enemies:
            self.reset_shot = True
            self.Reset_Shot()
            return
        self.enemy_hit = False
        self.nearby_enemies.sort(key=lambda entity: math.sqrt((self.pos[0] - entity.pos[0]) ** 2 + (self.pos[1] - entity.pos[1]) ** 2))
        self.delete_countdown = 50
        
        entity = self.nearby_enemies[0]
        self.direction = pygame.math.Vector2(entity.pos[0] - self.pos[0], entity.pos[1] - self.pos[1]).normalize()