from scripts.entities.items.weapons.magic_attacks.electric.electric_particle import Electric_Particle
import math

class Electric_Shooter():
    def __init__(self, game):
        self.game = game
        self.electric_cooldown = 0

    def Electric_Particle_Creation(self, entity, special_attack):
        # Handle cooldown for spacing between fire particles
        if self.electric_cooldown:
            self.electric_cooldown -= 1
            return special_attack
        else:
            self.electric_cooldown = 9
            special_attack = max(0, special_attack - 60)
            if not special_attack:
                return 0
            

        damage = 2
        speed = 2
        max_range = 240
       

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(entity.attack_direction[1], entity.attack_direction[0])

        pos_x = math.cos(base_angle) * speed
        pos_y = math.sin(base_angle) * speed
        direction = (pos_x, pos_y)
        electric_particle = Electric_Particle(
                self.game,
                entity.rect(),
                damage,
                speed,
                max_range,
                special_attack,
                direction,  # Pass the direction here
                entity
            )
        
        self.game.item_handler.Add_Item(electric_particle)
        
        return special_attack