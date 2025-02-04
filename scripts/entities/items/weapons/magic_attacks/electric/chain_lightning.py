from scripts.entities.items.weapons.magic_attacks.electric.electric_particle import Electric_Particle
import pygame
import math
class Chain_Lightning(Electric_Particle):
    def __init__(self, game, pos, entity, damage, speed, shoot_distance, special_attack, direction, effect):
        super().__init__(game, pos, shoot_distance)
        self.shots_left = min (20, effect * 3)
        self.reset_shot = False
        self.Set_Enabled(pos, speed, special_attack, direction, entity, 100)


    def Shoot(self):
        entity = super().Shoot()
        if entity:
            self.Electrocute_Nearby_Enemies()

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
    
    def Electrocute_Nearby_Enemies(self):
        self.nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self, 3)
        for enemy in self.nearby_enemies:
            enemy.Set_Effect("electric", 3)
