import pygame

class Inventory_Slot():
    def __init__(self, game, pos, size, item):
        self.game = game
        self.pos = pos
        self.size = size
        self.item = item
        Inventory_Slot.Setup_Inventory_Texture(self)
        self.active = False
        
    def Setup_Inventory_Texture(self):
        light_grey = (211, 211, 211)
        self.box_surface = pygame.Surface(self.size)
        self.box_surface.fill(light_grey)
        self.box_surface.set_alpha(179)

    def Set_Active(self):
        self.active = not self.active

    def Update(self):
        pass

    def Add_Item(self, item):
        self.item = item
        self.item.Move(self.pos)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def render(self, surf):
        black = (0, 0, 0)
        surf.blit(self.box_surface, self.pos)
        pygame.draw.rect(surf, black, self.rect(), 1)
        if self.item and not self.active:
            self.item.render(surf)
