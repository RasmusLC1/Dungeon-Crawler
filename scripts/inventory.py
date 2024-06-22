import pygame

class Inventory:
    def __init__(self):
        self.inventory = []

    def Update(self):
        pass

    def render(self, surf):
        light_grey = (211, 211, 211)
        black = (100,100,100)
        box_surface = pygame.Surface((8, 8))
        box_surface.fill(light_grey)
        box_surface.set_alpha(179)
        for i in range(5):
            for j in range(3):
                x = i * 8
                y = j * 8
                surf.blit(box_surface, (x, y))
                pygame.draw.rect(surf, black, pygame.Rect(x, y, 8, 8), 1)
