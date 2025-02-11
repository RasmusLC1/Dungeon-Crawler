import random
import math

class Particle_Patterns():

    @staticmethod
    def Dash_Particle():
        angle = random.random() * math.pi * 2
        speed = random.random() * 0.5 + 0.5
        velocity = [
                    math.cos(angle) * speed,
                    math.sin(angle) * speed
                    ]
        
        return velocity
    
    @staticmethod
    def Fire_Particle():
        # Constrain most of the motion to upward directions with slight spread
        base_angle = math.pi/2  # Straight up (90 degrees)
        angle_variation = math.pi/8  # 22.5 degrees spread in each direction
        angle = base_angle + random.uniform(-angle_variation, angle_variation)
        
        # Fire tends to have faster initial speeds that taper off
        speed = - (random.random() * 0.4 + 0.1)
        velocity = [
            math.cos(angle) * speed,  # Reduce horizontal movement
            math.sin(angle) * speed     # Ensure upward movement remains positive
        ]
        return velocity
    

    # Shoot the particles straight
    @staticmethod
    def Spark_Particle():
        direction_x = random.randrange(-1, 1)
        direction_y = random.randrange(-1, 1)
        velocity = [direction_x, direction_y]
        return velocity
