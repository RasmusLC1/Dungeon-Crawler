from scripts.items.weapons.magic_attacks.ice.ice_particle import Ice_Particle
import math

class Ice_Shooter():
    def __init__(self, game):
        self.game = game
        self.ice_cooldown = 0

    def Ice_Particle_Creation(self, special_attack, entity):
        # Handle cooldown for spacing between fire particles
        if self.ice_cooldown:
            self.ice_cooldown -= 1
            return special_attack
        else:
            self.ice_cooldown = 3
            special_attack = max(0, special_attack - 20)
            if not special_attack:
                return 0

        damage = 1
        speed = 1.2
        max_range = 240
       

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(entity.attack_direction[1], entity.attack_direction[0])

        pos_x = math.cos(base_angle) * speed
        pos_y = math.sin(base_angle) * speed
        direction = (pos_x, pos_y)
        ice_particle = Ice_Particle(
                self.game,
                entity.rect(),
                damage,
                speed,
                max_range,
                special_attack,
                direction,  # Pass the direction here
                entity
            )
        
        self.game.item_handler.Add_Item(ice_particle)
        
        return special_attack