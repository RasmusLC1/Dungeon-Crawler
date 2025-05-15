from scripts.entities.items.weapons.weapon import Weapon
from scripts.entities.items.weapons.magic_attacks.vampiric.soul_reap_shooter import Soul_Reap_Shooter
from scripts.engine.assets.keys import keys

class Scythe(Weapon):
    def __init__(self, game, pos, damage_type = 'slash'):
        super().__init__(game, pos, keys.scythe, 4, 2, 6, 100, 'two_handed_melee', damage_type)
        self.max_animation = 7
        self.attack_animation_max = 9

    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.special_attack <= 0 or not self.equipped:
            return
        self.Spawn_Soul_Reap()
        

    # Initialise the charge logic
    def Spawn_Soul_Reap(self):
        Soul_Reap_Shooter.Spawn_Soul_Reap(self.game, self.entity)
        self.special_attack = 0