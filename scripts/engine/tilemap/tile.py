import math
import pygame

# TODO: Implement Hashing so that entities registrer with a tile when they move onto it
# Use dictionary keyed to pos in tilemap
class Tile():
    def __init__(self, game, type, variant, pos, size, active, light_level, physics) -> None:
        self.game = game
        self.type = type
        self.variant = variant
        self.pos = pos
        self.size = size
        self.active = active
        self.light_level = light_level
        self.physics = physics
        self.entities = []


    def Set_Type(self, new_type):
        self.type = new_type

    def Update(self):
        self.Clear_Entities()

    def Set_Light_Level(self, new_light_level):
        self.light_level = new_light_level

    def Set_Active(self, new_active_level):
        self.active = max(new_active_level, self.active)

    def Search_Entities(self, category):
        entities = []
        for entity in self.entities:
            if not entity.category == category:
                continue

            entities.append(entity)

        return entities
    
    def Set_Entity_Active(self):
        for entity in self.entities:
            entity.Set_Active(self.active)
        

    def Add_Entity(self, entity):
        if entity in self.entities:
            return
        
        self.entities.append(entity)

    def Clear_Entity(self, entity_ID):
        for entity in self.entities:
            if entity.ID == entity_ID:
                self.entities.remove(entity)
                return
            
        return
    
    def Render(self, surf, offset = (0,0)):
        # Get the tile surface from the assets
        tile_surface = self.game.assets[self.type][self.variant].copy()
        # Adjust the tile activeness calculation
        tile_activeness = max(0, min(255, 700 - self.active))
        
        # Apply a non-linear scaling for a smoother transition
        tile_darken_factor = min(255, (255 * (1 - math.exp(-tile_activeness / 255)) + 150))

        if self.light_level > 0:
            light_level = min(255, self.light_level * 25)
        else:
            light_level = 1
        tile_darken_factor = max(0, min(220, tile_darken_factor - light_level))

        # Create a darkening surface with an alpha channel
        darkening_surface = pygame.Surface(tile_surface.get_size(), flags=pygame.SRCALPHA)
        darkening_surface.fill((0, 0, 0, int(tile_darken_factor)))
        
        # Blit the darkening surface onto the tile surface
        tile_surface.blit(darkening_surface, (0, 0))
        
        # Blit the darkened tile surface onto the main surface
        surf.blit(tile_surface, (self.pos[0] * self.size - offset[0], self.pos[1] * self.size - offset[1]))