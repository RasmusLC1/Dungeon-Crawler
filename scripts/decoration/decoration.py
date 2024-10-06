import pygame
from scripts.entities.entities import PhysicsEntity


class Decoration(PhysicsEntity):
    def __init__(self, game, pos, size, type) -> None:
        super().__init__(game, type, pos, size)
        self.game = game
        self.pos = pos
        self.size = size
        self.type = type
        self.active = 0
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.pos)
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

  

    def Render(self, surf, offset=(0, 0)):
        if not self.Update_Light_Level():
            return
        # Set image
        entity_image = self.game.assets[self.type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))
        entity_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(entity_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        entity_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(entity_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
