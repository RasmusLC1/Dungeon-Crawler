import pygame
from scripts.entities.entities import PhysicsEntity
import random
import math


class Decoration(PhysicsEntity):
    def __init__(self, game, type, category, pos, size) -> None:
        super().__init__(game, type, category, pos, size)


    def Update_Animation(self):
        pass

    def Open(self, generate_clatter = False):
        pass


    