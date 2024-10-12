import pygame
import math
import random
from scripts.engine.particles.particle import Particle

class Particle_Handler:
    def __init__(self, game) -> None:
         self.game = game

    def particle_update(self, offset = (0,0)):
        for particle in self.game.particles.copy():
                kill = particle.Update()
                particle.Render(self.game.display, offset)
                particle.Render(self.game.display, offset)
                if kill:
                    self.game.particles.remove(particle)
