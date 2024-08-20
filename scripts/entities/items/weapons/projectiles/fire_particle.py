from scripts.entities.items.weapons.projectiles.projectile import Projectile


class Fire_Particle(Projectile):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class, entity, special_attack, offset):
        super().__init__(game, pos, size, type, damage, speed, range, weapon_class)
        self.entity = entity
        self.timer = range
        self.charge_time = special_attack
        self.Set_Special_Attack(offset)

    def Shoot(self):
        self.Initialise_Shooting(1)
        self.timer -= 1
        if self.timer <= 0:
            self.game.item_handler.Remove_Item(self)

        super().Shoot()



        

    def Pick_Up(self):
        pass
