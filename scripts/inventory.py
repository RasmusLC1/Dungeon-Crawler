import pygame
from scripts.Chest.item import Item

class Inventory:
    def __init__(self, game):
        self.x_size = 5
        self.y_size = 3
        self.game = game
        self.available_pos = []
        self.inventory = [[None for _ in range(self.x_size)] for _ in range(self.y_size)]

    def Update(self):
        for j in range(self.y_size):
            for i in range(self.x_size):
                if self.inventory[j][i]:
                    self.inventory[j][i].Update_Animation()

    def Add_Item(self, item):
        for j in range(self.y_size):
            for i in range(self.x_size):
                if not self.inventory[j][i]:
                    x = i * 8
                    y = j * 8
                    item.pos = (x, y)
                    self.inventory[j][i] = item
                    return True
        return False
    
    def render(self, surf):
        light_grey = (211, 211, 211)
        black = (0, 0, 0)
        box_surface = pygame.Surface((8, 8))
        box_surface.fill(light_grey)
        box_surface.set_alpha(179)
        for j in range(self.y_size):
            for i in range(self.x_size):
                x = i * 8
                y = j * 8
                surf.blit(box_surface, (x, y))
                pygame.draw.rect(surf, black, pygame.Rect(x, y, 8, 8), 1)
                if self.inventory[j][i]:
                    self.inventory[j][i].render(surf, (0, 0))

        # for row in self.inventory:
        #     for item in row:
        #         item.render(surf)         
