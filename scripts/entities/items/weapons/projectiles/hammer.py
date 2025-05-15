from scripts.entities.items.weapons.projectiles.projectile import Projectile
from scripts.engine.assets.keys import keys

class Hammer(Projectile):
    def __init__(self, game, pos, damage_type = 'blunt'):
        super().__init__(game, pos, keys.hammer, 5, 2, 5, 4, 40, 'one_handed_melee', damage_type, 20, keys.cut)
        self.max_animation = 3
        self.attack_animation_max = 3
        self.distance_from_player = 0
        
    
    def Shoot(self):
        self.Initialise_Shooting(self.entity_strength)
        self.rotate += 5

        super().Shoot()

    def Special_Attack(self):
        if not self.special_attack or not self.equipped:
            return
        self.Drop_Weapon_After_Shot()
