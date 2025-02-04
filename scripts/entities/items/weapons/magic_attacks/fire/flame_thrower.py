from scripts.entities.items.weapons.magic_attacks.fire.fire_particle import Fire_Particle
import math

class Flame_Thrower():
    def __init__(self, game, pool_size):
        self.game = game
        self.fire_cooldown = 0
        self.last_used_index = 0
        self.fire_particle_pool = []
        self.Create_Fire_Particle_Pool(pool_size)

    def Fire_Particle_Creation(self, entity, special_attack):
        # Handle cooldown for spacing between fire particles
        if self.fire_cooldown:
            self.fire_cooldown -= 1
            return special_attack
        else:
            self.fire_cooldown = 3
            special_attack = max(0, special_attack - 20)
            if special_attack <= 0:
                return 0
            

        # Basic raycasting attributes
        num_lines = 8  # Define the number of lines and the spread angle (in degrees)
        spread_angle = 50  # Total spread of the fan (in degrees)
        angle_increment = spread_angle / (num_lines - 1)  # Calculate the angle increment between each line

        # Calculate the base angle using atan2(y, x)
        base_angle = math.atan2(entity.attack_direction[1], entity.attack_direction[0])
        start_angle = base_angle - math.radians(spread_angle / 2)

        speed = 1  

        # Generate fire particles
        for j in range(num_lines):
            fire_particle = self.Find_Fire_Particle()

            if not fire_particle:
                print(len(self.fire_particle_pool))
                print("Not enough fireparticles in pool")
                return 0 
            
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle) * speed
            pos_y = math.sin(angle) * speed
            direction = (pos_x, pos_y)
            
            fire_particle.Set_Enabled(entity.rect(), speed, special_attack, direction, entity)

        return special_attack
    
    # Look for a fire particle that does not have a delete countdown
    def Find_Fire_Particle(self):
        fire_particle = None
        for particle in self.fire_particle_pool:
            if particle.delete_countdown:
                continue
            fire_particle = particle
            break
        return fire_particle


    def Create_Fire_Particle_Pool(self, amount):
        for _ in range(amount):
            fire_particle = Fire_Particle(
                self.game,
                (-999, -999),
                100
            )
            self.fire_particle_pool.append(fire_particle)


