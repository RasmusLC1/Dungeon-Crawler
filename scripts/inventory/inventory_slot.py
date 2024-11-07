
import pygame
import pygame.freetype
import random

class Inventory_Slot():
    def __init__(self, game, pos, size, item, index):
        self.game = game
        self.pos = pos
        self.index = index
        self.size = size
        self.item = item
        self.background = None
        self.inventory_type = None
        self.Setup_Inventory_Texture()
        self.active = False
        self.activate_counter = 0
        self.white_list_items = []
        self.saved_data = {}
      

    def Setup_Inventory_Texture(self):
        light_grey = (211, 211, 211)
        self.box_surface = pygame.Surface(self.size)
        self.box_surface.fill(light_grey)
        self.box_surface.set_alpha(179)

    def Set_Active(self, status):
        self.active = status

    def Reset_Inventory_Slot(self):
        self.item = None
        self.active = False
        self.activate_counter = 0

    def Update(self):
        if self.active:
            self.activate_counter += 1
            return
        if self.item and self.item.used:
            self.item = None
        return
    
    def Update_Item(self):
        if not self.item:
            return
        self.item.Update()

    def Add_Item(self, item):
        if not item:
            return False
        if not item.sub_category in self.white_list_items:
            return False
        
        self.item = item
        self.item.active = True
        self.item.picked_up = True
        self.item.Move((self.pos[0] + 5, self.pos[1] + 5))
        self.item.Set_Inventory_Index(self.index)
        if self.inventory_type:
            self.item.Set_Inventory_Type(self.inventory_type)
        else:
            self.item.Set_Inventory_Type(None)
        return True

    def Remove_Item(self):
        self.item = None

    def Remove_Item_On_Amount(self):
        if not self.item.amount <= 0:
            return False
        self.item = None
        return True
    
    def Set_White_List(self, items):
        self.white_list_items = items

    def Add_Background(self, background):
        self.background = background

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def Render(self, surf):
        black = (0, 0, 0)

        # Render the box surface with scaling
        scaled_box_surface = pygame.transform.scale(self.box_surface, (self.size[0], self.size[1]))
        surf.blit(scaled_box_surface, self.pos)
        pygame.draw.rect(surf, black, self.rect(), 1)
       

        if self.background and not self.item:
            background_image = pygame.transform.scale(self.background, self.size)
            surf.blit(background_image, self.pos)


        if self.item and not self.active:
            self.item.Render(surf)
        else:
            return

        if not self.item.amount > 1:
            return
        
        self.Render_Item_Amount(surf)


    def Render_Item_Amount(self, surf):
        x_offset = 9
        if self.item.amount > 10:
            x_offset = 5
        self.game.default_font.Render_Word(surf, str(self.item.amount), (self.pos[0] + x_offset, self.pos[1] + self.item.size[1]))