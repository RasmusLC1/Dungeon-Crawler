from scripts.entities.items.runes.projectile_rune import Projectile_Rune
from scripts.entities.items.weapons.magic_attacks.vampiric.soul_reap_shooter import Soul_Reap_Shooter

class Soul_Reap_Rune(Projectile_Rune):
    def __init__(self, game, pos):
        super().__init__(game, 'soul_reap_rune', pos, 1, 20)
        self.animation_time_max = 30
        self.animation_size_max = 15
        self.activate_cooldown_max = 100

    def Set_Charge(self):
        self.charge = self.current_power * 100

    def Generate_Projectile(self):
        self.charge = Soul_Reap_Shooter.Spawn_Soul_Reap(self.game ,self.game.player)
        self.Set_Activate_Cooldown(self.activate_cooldown_max)
        return
