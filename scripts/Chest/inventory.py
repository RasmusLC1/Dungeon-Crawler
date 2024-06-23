import pygame
from scripts.Chest.item import Item
import copy

class Inventory:
    def __init__(self, game):
        self.x_size = 7
        self.y_size = 2
        self.game = game
        self.available_pos = []
        self.size = (10, 10)
        self.active_item = None
        
        self.inventory = [[None for _ in range(self.x_size)] for _ in range(self.y_size)]

    def Update(self, offset=(0, 0)):
        for j in range(self.y_size):
            for i in range(self.x_size):
                if self.inventory[j][i]:
                    self.inventory[j][i].Update_Animation()
                    if self.game.mouse.left_click:
                        if self.inventory[j][i].rect().colliderect(self.game.mouse.mouse_rect()):
                            self.active_item = Inventory.clone(self.inventory[j][i])
                            self.active_item.active = True
                            self.game.items.append(self.active_item)
                            self.inventory[j][i] = None
                    if not self.game.mouse.left_click:
                        self.active_item = None
        if self.active_item:
            self.active_item.Move(self.game.mouse.mpos)
    
    
    def clone(self):
        # Create a new instance of Item with the same attributes
        new_item = Item(self.game, self.pos, self.type, self.quality)
        new_item.active = self.active
        new_item.animation = self.animation
        new_item.animation_cooldown = self.animation_cooldown
        new_item.size = self.size
        return new_item

    def Add_Item(self, item):
        for j in range(self.y_size):
            for i in range(self.x_size):
                if not self.inventory[j][i]:
                    x = i * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 40
                    y = j * self.size[0] + self.game.screen_height / self.game.render_scale - 25
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
                x = i * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 40 - 1
                y = j * self.size[0] + self.game.screen_height / self.game.render_scale - 25 - 1
                surf.blit(box_surface, (x, y))
                pygame.draw.rect(surf, black, pygame.Rect(x, y, self.size[0], self.size[1]), 1)
                if self.inventory[j][i]:
                    self.inventory[j][i].render(surf, (0, 0))

        # for row in self.inventory:
        #     for item in row:
        #         item.render(surf)         
