import pygame
from scripts.entities.entities import PhysicsEntity
import random
import math


class Decoration(PhysicsEntity):
    def __init__(self, game, type, pos, size) -> None:
        super().__init__(game, type, 'decoration', pos, size)
        self.game.tilemap.Add_Entity_To_Tile(self.tile, self)
        self.animation = 0
        self.Set_Sprite()


    def Update_Animation(self):
        pass

    def Open(self, generate_clatter = False):
        pass
    
    # Setting the initial sprite type from assets, only called during initial setup
    def Set_Sprite(self):
        self.sprite = self.game.assets[self.type]
        self.Set_Entity_Image()

    # Setting the item image and scaling it
    def Set_Entity_Image(self):
        entity_image = self.sprite[self.animation].convert_alpha()
        self.entity_image = pygame.transform.scale(entity_image, self.size)


    def Render(self, surf, offset = (0,0)):

        if not self.Update_Light_Level():
            return

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))  # Adjust the factor as needed
        if not alpha_value:
            return
        
        if self.render_needs_update:
            self.Update_Dark_Surface(alpha_value)
        
        
        # Render the chest
        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    

    def Update_Dark_Surface(self, alpha_value):
        # Set image
        self.rendered_image = self.entity_image.copy()

        self.rendered_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(self.rendered_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        self.rendered_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.render_needs_update = False