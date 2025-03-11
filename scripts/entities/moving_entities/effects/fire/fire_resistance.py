from scripts.entities.moving_entities.effects.effect import Effect
import pygame
import random

# Reduce fire damage
class Fire_Resistance(Effect):
    def __init__(self, entity):
        description = 'Prevents fire damage'
        super().__init__(entity, "fire_resistance", 0, 0, (200, 250), description)

