import pygame
import math
import random
from scripts.particle import Particle

class Particle_Handler:

    def particle_update(self, offset = (0,0)):
        for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset)
                particle.render(self.display, offset)
                if kill:
                    self.particles.remove(particle)
