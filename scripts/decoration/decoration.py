import pygame
from scripts.entities.entities import PhysicsEntity


class Decoration(PhysicsEntity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, type, pos, size)
        self.game = game
        self.pos = pos
        self.size = size
        self.type = type
        self.active = 0
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
        print(self.light_level)
        self.animation = 0
        self.max_animation = 0
        self.animation_cooldown = 0

    def Update(self):
        self.Animation_Update()

    def Animation_Update(self):
        if not self.animation_cooldown:
            self.animation_cooldown = 10
            if self.animation < self.max_animation:
                self.animation += 1
            else:
                self.animation = 0
        else:
            self.animation_cooldown -= 1

    # def Update_Light_Level(self):
    #     # Set the light level based on the tile that the entity is placed on
    #     current_tile = self.game.tilemap.Current_Tile(self.pos)
    #     if not current_tile:
    #         return False

    #     new_light_level = min(255, current_tile['light'] * 30)

    #     if self.light_level < new_light_level:
    #         self.light_level += 5
    #     elif self.light_level > new_light_level:
    #         self.light_level -= 5

    #     # Ensuring light level is within the valid range and updating it correctly
    #     self.light_level = max(0, min(255, self.light_level))

    #     # 75 is the darkest level we want
    #     self.light_level = max(75, 255 - self.light_level)

    #     # If the light level is too low, we might choose not to render the entity
    #     return self.light_level > 75

    def Update_Light_Level(self):
        # Set the light level based on the tile that the entity is placed on
        tile = self.game.tilemap.Current_Tile(self.pos)
        if not tile:
            return True
        
        new_light_level = min(255, tile['light'] * 30)
        if self.light_level < new_light_level:
            self.light_level += 5
        elif self.light_level > new_light_level:
            print(new_light_level)
            self.light_level -= 5
        self.light_level = abs(self.light_level - 255)
        # 75 is the darkest level we want
        self.light_level = max(75, 255 - self.light_level)
        

        if self.light_level <= 75:
            return False
        else:
            return True

    def Render(self, surf, offset=(0, 0)):
        if not self.Update_Light_Level():
            return
        # Set image
        chest_image = self.game.assets[self.type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))
        chest_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(chest_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        chest_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(chest_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
