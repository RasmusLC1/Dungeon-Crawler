from scripts.items.weapons.magic_attacks.fire.fire_particle import Fire_Particle
import math

class Flame_Thrower():
    def __init__(self, game):
        self.game = game
        self.fire_cooldown = 0

    def Fire_Particle_Creation(self, entity, special_attack):
        # Handle cooldown for spacing between fire particles
        if self.fire_cooldown:
            self.fire_cooldown -= 1
            return special_attack
        else:
            self.fire_cooldown = 3
            special_attack = max(0, special_attack - 20)
            if not special_attack:
                return 0
            

        # Basic raycasting attributes
        num_lines = 8  # Define the number of lines and the spread angle (in degrees)
        spread_angle = 50  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1)  # Calculate the angle increment between each line

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(entity.attack_direction[1], entity.attack_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)

        damage = 2
        speed = 1  
        max_range = 100

        # Generate fire particles
        for j in range(num_lines):
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle) * speed
            pos_y = math.sin(angle) * speed
            direction = (pos_x, pos_y)

            # Create the fire particle with the direction
            fire_particle = Fire_Particle(
                self.game,
                entity.rect(),
                damage,
                speed,
                max_range,
                special_attack,
                direction,  # Pass the direction here
                entity
            )
            self.game.item_handler.Add_Item(fire_particle)

        return special_attack