import math
import random
import pygame

from scripts.particle import Particle
from scripts.traps.trap_handler import Trap_Handler
from scripts.entities.effects import Status_Effect_Handler


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        
    def update(self):
        pass


    def render(self, surf, offset=(0, 0)):
        pass