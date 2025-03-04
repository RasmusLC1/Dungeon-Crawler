from scripts.entities.items.weapons.projectiles.projectile import Projectile
import pygame

class Particle(Projectile):
    def __init__(self, game, pos, type, damage, speed, range, max_charge_time, damage_type, shoot_distance):
        super().__init__(game, pos, type, 0, damage, speed, range, max_charge_time, 'particle', damage_type, shoot_distance, 'cut', (4, 4), False)
        self.attack_animation_max = 3
        self.disabled = True

    def Save_Data(self):
        pass

    def Update(self, offset=...):
        if self.disabled:
            return
        return super().Update(offset)
    
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
            self.Set_Disabled()

        return entity

    def Reset_Shot(self):
        self.Set_Disabled()
        super().Reset_Shot()

    def Set_Direction(self, direction):
        self.direction = direction

    def Delete_Item(self):
        self.Set_Disabled()

    def Set_special_attack(self, special_attack):
        self.special_attack = special_attack

    def Set_Speed(self, speed):
        self.speed = speed

    def Set_Disabled(self):
        self.disabled = True
        self.delete_countdown = 0
        self.Set_Position((-999, -999))
        self.Set_Special_Attack(0)
        self.Set_Direction((0,0))
        self.Set_Entity(None)
        self.Set_Speed(0)
        self.game.item_handler.Remove_Item(self)


    def Set_Enabled(self, pos, speed, special_attack, direction, entity, delete_countdown):
        self.disabled = False
        self.game.item_handler.Add_Item(self)
        self.delete_countdown = delete_countdown
        self.Set_Position(pos)
        self.Set_Speed(speed)
        self.Set_Direction(direction)
        self.Set_Entity(entity)
        self.Set_special_attack(special_attack)


    def Update_Text_Box(self, hitbox_1, hitbox_2):
        pass
    
    # Own render function since we don't need to compute light
    def Render(self, surf, offset=(0, 0)):
        if self.disabled:
            return
        
        weapon_image = self.entity_image.convert_alpha()

        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
