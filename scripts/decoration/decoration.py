import pygame
from scripts.entities.entities import PhysicsEntity
import random
import math


class Decoration(PhysicsEntity):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'decoration', pos, size)
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self)
        self.animation = 0


    def Update_Animation(self):
        pass

    def Open(self, generate_clatter = False):
        pass


    def Render(self, surf, offset = (0,0)):

        if not self.Update_Light_Level():
            return
        # Set image
        decoration_image = self.game.assets[self.type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))  # Adjust the factor as needed
        if not alpha_value:
            return
        
        decoration_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(decoration_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        decoration_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(decoration_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    