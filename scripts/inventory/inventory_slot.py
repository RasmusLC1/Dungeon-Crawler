import pygame

class Inventory_Slot():
    def __init__(self, game, pos, size, item):
        self.game = game
        self.pos = pos
        self.size = size
        self.item = item
        Inventory_Slot.Setup_Inventory_Texture(self)
        self.active = False
        self.activate_counter = 0
        
    def Setup_Inventory_Texture(self):
        light_grey = (211, 211, 211)
        self.box_surface = pygame.Surface(self.size)
        self.box_surface.fill(light_grey)
        self.box_surface.set_alpha(179)

    def Set_Active(self, status):
        self.active = status

    def Update(self):
        if self.active:
            self.activate_counter += 1
            return
        if self.item.used:
            self.item = None


        return

    def Add_Item(self, item):
        item.active = True
        self.item = item
        self.item.Move((self.pos[0] + 3, self.pos[1] + 3))

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Render(self, surf):
        black = (0, 0, 0)
        surf.blit(self.box_surface, self.pos)
        pygame.draw.rect(surf, black, self.rect(), 1)
        if self.item and not self.active:
            self.item.Render(surf)