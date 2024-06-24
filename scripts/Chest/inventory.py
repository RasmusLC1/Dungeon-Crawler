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
        self.item_clicked = 0
        self.saved_position = (0,0)
        
        self.inventory = [[None for _ in range(self.x_size)] for _ in range(self.y_size)]

    def Update(self, offset = (0,0)):
        Inventory.Active_Item(self, offset)
        # Check if an item is being dragged
        for j in range(self.y_size):
            for i in range(self.x_size):
                if self.inventory[j][i]:
                    self.inventory[j][i].Update_Animation()
                    if self.game.mouse.left_click:
                        # Check for collision with inventory slot
                        if self.inventory[j][i].rect().colliderect(self.game.mouse.mouse_rect()):
                            self.item_clicked += 1
                            if self.game.mouse.hold_down_left > 10:
                                self.active_item = Inventory.clone(self.inventory[j][i])
                                self.active_item.active = True
                                # self.game.items.append(self.active_item)
                                self.saved_position = (j,i)
                                self.inventory[j][i] = None
                            

    # Active item is an item being dragged
    def Active_Item(self, offset = (0,0)):
        # Check if there is an active item
        if self.active_item:
            # Check for out of bounds
            item_out_of_bounds = self.active_item.Move_Legal(self.game.mouse.mpos, self.game.player.pos, self.game.tilemap)
            if item_out_of_bounds == False:
                # Render with fadeout depending on distance
                self.active_item.render_out_of_bounds(self.game.player.pos, self.game.mouse.mpos, self.game.display, offset)  
                # Return the item to Inventory
                if self.game.mouse.left_click == False:
                    x = self.saved_position[1] * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 40
                    y = self.saved_position[0] * self.size[0] + self.game.screen_height / self.game.render_scale - 25
                    self.active_item.pos = (x,y)
                    self.inventory[self.saved_position[0]][self.saved_position[1]] = self.active_item
            else:
                # Render legal item position and move it
                self.active_item.render(self.game.display, offset)  
                self.active_item.Move(self.game.mouse.mpos)
                # Add item back to item list
                if self.game.mouse.left_click == False:
                    self.game.items.append(self.active_item)
                    self.active_item = None

            # Clicking on item
            if not self.game.mouse.left_click and self.item_clicked:
                        if self.item_clicked < 30 and self.game.mouse.hold_down_left < 5:
                            print("ACTIVATE")
                        else:
                            self.active_item = None
                        self.item_clicked = 0  

        
    
    
    # Create a new instance of Item with the same attributes
    def clone(self):
        new_item = Item(self.game, self.pos, self.type, self.quality)
        new_item.active = self.active
        new_item.animation = self.animation
        new_item.animation_cooldown = self.animation_cooldown
        new_item.size = self.size
        return new_item

    # Add item to the inventory
    def Add_Item(self, item):
        for j in range(self.y_size):
            for i in range(self.x_size):
                if not self.inventory[j][i]:
                    # Calculate inventory position for item.pos
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