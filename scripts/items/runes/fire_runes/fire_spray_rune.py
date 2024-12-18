from scripts.items.runes.projectile_rune import Projectile_Rune
from scripts.items.weapons.magic_attacks.fire.flame_thrower import Flame_Thrower

class Fire_Spray_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'fire_spray_rune', pos, 1, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.fire_shooter = Flame_Thrower(self.game)
        self.activate_cooldown_max = 100


    def Set_Charge(self):
        self.charge = self.current_power * 100

    def Generate_Projectile(self):
        self.charge = self.fire_shooter.Fire_Particle_Creation(self.game.player, self.charge)
        if self.charge <= 0:
            self.Set_Activate_Cooldown(self.activate_cooldown_max )
        else:
            self.Set_Activate_Cooldown(0)
        return
