import math

class Particle_Shooter():
    def __init__(self, game):
        self.game = game
        self.fire_cooldown = 0
        self.index = 0
        self.particle_pool = []

    def Particle_Creation(self, entity, special_attack):
        pass
            
    def Shoot_Particles(self, entity, special_attack):
        pass
    
    # Append extra fire particle to the pool in case it runs out
    def Create_Extra_Particle(self):
        pass


    # Search for particles with an index
    def Find_Particle(self):
        # If there are no particles in the pool return None to spawn particle
        if not self.particle_pool:
            return None
        
        # Check if the initial index is available, in which case loop the index back to 0
        if not self.particle_pool[0].delete_countdown:
            self.index = 0
        
        # Overflow prevent
        if self.index >= len(self.particle_pool) - 1:
            return None

        # Set the fire particle to be the next available index
        particle = self.particle_pool[self.index]
        self.index += 1

        # If there are no free fire particle return None to spawn a new one
        if particle.delete_countdown:
            return None
        
        return particle
