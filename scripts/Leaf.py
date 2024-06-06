import pygame
import math
import random
from scripts.particle import Particle

class Leaf:

    def Leaf_Movement(self, render_scroll):
        for particle in self.particles.copy():
                kill = particle.update()
                particle.render(self.display, offset=render_scroll)
                if particle.type == 'leaf':
                    particle.pos[0] += math.sin(particle.animation.frame * 0.035) * 0.3 # Sin gives curve to leaf
                if kill:
                    self.particles.remove(particle)

    def Leaf_Spawner(self):
         for rect in self.leaf_spawners:
                # rect.width is the trees hitbox, so the amount of leaves scales with tree size
                if random.random() * 49999 < rect.width * rect.height:
                    pos = (rect.x + random.random() * rect.width, rect.y + random.random() * rect.height)
                    self.particles.append(Particle(self, 'leaf', pos, velocity = [-0.1, 0.3], frame = random.randint(0, 20)))
