import pygame
from scripts.entities.player.items.item import Item
from scripts.entities.entities import PhysicsEntity

class Weapon(Item):
    def __init__(self, game, pos, size, type, damage, speed, range):
        super().__init__(game, type, pos, size, 1)
        self.damage = damage
        self.speed = speed
        self.range = range
        # Can be expanded to damaged or dirty versions of weapons later
        self.sub_type = self.type


    # def Update(self):
    #     pass

    def Render_In_Inventory(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    def Render(self, surf, offset=(0, 0)):
        if not self.picked_up:
            self.Render_In_Inventory(surf, offset)

        if not self.Update_Light_Level():
            return
        
        # Set image
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))
        weapon_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        weapon_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
