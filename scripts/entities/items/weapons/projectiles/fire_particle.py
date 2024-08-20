from scripts.entities.items.weapons.projectiles.projectile import Projectile


class Fire_Particle(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, special_attack, attack_direction, entity):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class)
        self.timer = 30
        self.attack_direction = attack_direction
        self.special_attack = special_attack / 2
        self.entity = entity

    def Shoot(self):
        if not self.shoot_speed:
            self.Initialise_Shooting(2)
        
        self.timer -= 1

        entity = super().Shoot()
        if entity:
            self.special_attack = 0
            entity.Set_Effect('Fire', 4)
        if self.special_attack <= 0 or not self.timer:
            self.game.item_handler.Remove_Item(self)

    def Pick_Up(self):
        pass
