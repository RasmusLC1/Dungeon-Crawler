import random
import math
import pygame

class Trap:
    def __init__(self, game, pos, size, type):
        self.game = game
        self.pos = pos
        self.size = size
        self.Cooldown = 0
        self.animation = 0
        self.animation_cooldown = 0
        self.animation_max = 0
        self.type = type
        self.active = 0
        self.light = 0

    def Update(self, entity):
        pass

    def Animation_Update(self):
        pass

    def Set_Active(self, duration):
        self.active = duration

    def Reduce_Active(self):
        self.active -= 1

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def Render(self, surf, offset=(0, 0)):
        # Get the tile surface from the assets
        tile_surface = self.game.assets[self.type][self.animation].copy()
        
        # Adjust the tile activeness calculation
        tile_activeness = max(0, min(255, 700 - self.active))
            
        # Apply a non-linear scaling for a smoother transition
        tile_darken_factor = min(255, (255 * (1 - math.exp(-tile_activeness / 255)) + 150))

        tile = self.game.tilemap.Current_Tile(self.pos)
        if tile['light'] > 0:
            light_level = min(255, tile['light'] * 25)
        else:
            light_level = 1
        tile_darken_factor = max(0, min(220, tile_darken_factor - light_level))
        
        # Create a darkening surface with an alpha channel
        darkening_surface = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        darkening_surface.fill((0, 0, 0, int(tile_darken_factor)))
        
        # Blit the darkening surface onto the tile surface
        tile_surface.blit(darkening_surface, (0, 0))
        
        # Blit the darkened tile surface onto the main surface
        surf.blit(tile_surface, (self.pos[0] * self.size[0] - offset[0], self.pos[1] * self.size[1] - offset[1]))


        surf.blit(tile_surface, (self.pos[0] - offset[0], self.pos[1] - offset[1]))