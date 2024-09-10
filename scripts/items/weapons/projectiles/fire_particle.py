from scripts.items.weapons.projectiles.projectile import Projectile
import pygame

class Fire_Particle(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, special_attack, attack_direction, entity):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class)
        self.delete_countdown = 30
        self.attack_direction = attack_direction
        self.special_attack = special_attack / 4
        self.entity = entity
        self.attack_animation_max = 3


    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(2)
        

        entity = super().Shoot()
        if entity:
            self.special_attack = 0
            entity.Set_Effect('Fire', 4)
        if self.special_attack <= 0:
            self.game.item_handler.Remove_Item(self, True)

    def Pick_Up(self):
        pass

    def Render(self, surf, offset=(0, 0)):

        # Set image
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
