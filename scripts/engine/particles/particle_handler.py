from scripts.engine.particles.particle import Particle
from scripts.engine.particles.particle_patterns import Particle_Patterns

class Particle_Handler:
    def __init__(self, game) -> None:
         self.game = game
         self.particle_pool = []
         self.active_particles = []
         self.index = 0
         self.Spawn_Particles(2000)

         self.particle_movement_patterns = {
             'dash' : Particle_Patterns.Dash_Particle,
             'fire' : Particle_Patterns.Fire_Particle,
             'spark' : Particle_Patterns.Spark_Particle,
             'blood' : Particle_Patterns.Spark_Particle,
             'gold' : Particle_Patterns.Spark_Particle,
             'bone' : Particle_Patterns.Spark_Particle,
             'vampire' : Particle_Patterns.Vampire_Particle,
         }
         

    def particle_update(self, offset = (0,0)):
        for particle in self.active_particles:
                particle.Update()
                particle.Render(self.game.display, offset)

                if not particle.active:
                    self.active_particles.remove(particle)


    def Activate_Particles(self, amount, type, pos, frame):
        for _ in range(amount):
            # Look for particle
            particle = self.Find_Particle()

            # If none are found, spawn 100 new ones and attach one
            if not particle:
                particle = self.Spawn_Extra_Particle()

            velocity_function = self.particle_movement_patterns.get(type)
            velocity = velocity_function()
            particle.Set_Active(type, pos, velocity, frame)
            self.active_particles.append(particle)


    # Search for particles with an index
    def Find_Particle(self):
        # If there are no particles in the pool return None to spawn particle
        if not self.particle_pool:
            return None
        
        # Check if the initial index is available, in which case loop the index back to 0
        if not self.particle_pool[0].active:
            self.index = 0
        
        # Overflow prevent
        if self.index >= len(self.particle_pool) - 1:
            return None

        # Set the fire particle to be the next available index
        particle = self.particle_pool[self.index]
        self.index += 1

        # If there are no free fire particle return None to spawn a new one
        if particle.active:
            return None
        
        return particle

    def Spawn_Extra_Particle(self):
        particle = Particle(self.game)
        self.particle_pool.append(particle)
        return particle

    def Spawn_Particles(self, amount):
        for _ in range(amount):
             self.particle_pool.append(Particle(self.game))


    