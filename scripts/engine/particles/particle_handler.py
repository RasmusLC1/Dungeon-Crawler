import pygame
import math
import random
from scripts.engine.particles.particle import Particle

class Particle_Handler:

    def particle_update(self, offset = (0,0)):
        for particle in self.particles.copy():
                kill = particle.update()
                particle.Render(self.display, offset)
                particle.Render(self.display, offset)
                if kill:
                    self.particles.remove(particle)
