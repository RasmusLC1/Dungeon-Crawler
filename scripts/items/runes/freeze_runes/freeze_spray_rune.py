from scripts.items.runes.projectile_rune import Projectile_Rune
from scripts.items.weapons.magic_attacks.ice.ice_shooter import Ice_Shooter

class Freeze_Spray_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'freeze_ball_rune', pos, 1, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.ice_shooter = Ice_Shooter(self.game)

    def Set_Charge(self):
        self.charge = self.current_power * 100

    def Generate_Projectile(self):
        print(self.charge)
        self.charge = self.ice_shooter.Ice_Particle_Creation(self.charge ,self.game.player)
        if self.charge <= 0:
            self.Set_Shoot_Cooldown()
        else:
            self.Set_Shoot_Cooldown(0)
        return
