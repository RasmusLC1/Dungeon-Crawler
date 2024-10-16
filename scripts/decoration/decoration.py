import pygame
from scripts.entities.entities import PhysicsEntity
import random

class Decoration(PhysicsEntity):
    def __init__(self, game, type, category, pos, size) -> None:
        super().__init__(game, type, category, pos, size)
        self.ID = random.randint(1, 100000)

