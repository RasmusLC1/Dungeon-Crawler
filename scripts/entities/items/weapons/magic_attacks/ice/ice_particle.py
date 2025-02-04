from scripts.entities.items.weapons.magic_attacks.base_attacks.particle import Particle


class Ice_Particle(Particle):
    def __init__(self, game, pos, shoot_distance):
        super().__init__(game, pos, 'ice_particle', 2, 1.2, 240, 100, 'frozen', shoot_distance)
        # self.delete_countdown = 100
        # self.attack_animation_time = shoot_distance // self.attack_animation_max
   





