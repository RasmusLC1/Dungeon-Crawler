from scripts.entities.items.weapons.magic_attacks.fire.fire_particle import Fire_Particle
import math

class Flame_Thrower():
    def __init__(self, game):
        self.game = game
        self.fire_cooldown = 0
        self.last_used_index = 0
        self.index = 0
        self.fire_particle_pool = []

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
                fire_particle = self.Create_Extra_Fire_Particle()
            
            angle = start_angle + j * math.radians(angle_increment)
            pos_x = math.cos(angle) * speed
            pos_y = math.sin(angle) * speed
            direction = (pos_x, pos_y)
            
            fire_particle.Set_Enabled(entity.rect(), speed, special_attack, direction, entity)

        return special_attack
    
    # Append extra fire particle to the pool in case it runs out
    def Create_Extra_Fire_Particle(self):
        fire_particle = Fire_Particle(
                self.game,
                (-999, -999),
                100
            )
        self.fire_particle_pool.append(fire_particle)
        return fire_particle


    # Search for particles with an index
    def Find_Fire_Particle(self):
        # If there are no particles in the pool return None to spawn particle
        if not self.fire_particle_pool:
            return None
        
        # Check if the initial index is available, in which case loop the index back to 0
        if not self.fire_particle_pool[0].delete_countdown:
            self.index = 0
        
        # Overflow prevent
        if self.index >= len(self.fire_particle_pool) - 1:
            return None

        # Set the fire particle to be the next available index
        fire_particle = self.fire_particle_pool[self.index]
        self.index += 1

        # If there are no free fire particle return None to spawn a new one
        if fire_particle.delete_countdown:
            return None
        
        return fire_particle
