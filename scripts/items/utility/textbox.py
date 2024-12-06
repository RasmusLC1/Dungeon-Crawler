import pygame

class Text_Box():
    def __init__(self, game, item) -> None:
        self.game = game
        self.item = item
        self.render = False
        self.x_size = 0
        self.y_size = 0

    def Update(self, hitbox_1, hitbox_2):
        
        # Handle when item is in inventory
        if hitbox_1.colliderect(hitbox_2):
            self.render = True
            return True
        
        if self.render:
            self.render = False

        return False

    def Edit_Item_Name(self):
        item_name = self.item.type
        item_name = item_name.replace('_resistance', ' res')
        if 'rune' in item_name:
            item_name = item_name.replace('_rune', '')
        if 'potion' in item_name:
            item_name = item_name.replace('_potion', '')
        return item_name
    
    def Set_Text_Box_pos(self, offset):
        text_box_pos = (0,0)
        # Render itembox different depending on if it's picked up or not
        if self.item.picked_up:
            # Move rune textbox to the left since they are located far right 
            if self.item.sub_category == 'rune':
                text_box_pos = (self.game.screen_width // self.game.render_scale - self.x_size - 20, self.item.pos[1] -  self.y_size - 20)
            else:
                text_box_pos = (self.item.pos[0], self.item.pos[1] -  self.y_size)
        else:
            text_box_pos = (self.item.pos[0] - offset[0], self.item.pos[1] - offset[1] - self.y_size)
        
        return text_box_pos
    
    def Set_Text_Box_Size(self, item_name):
        if self.item.sub_category == "weapon":
            self.y_size = 100
        else:
            self.y_size = 60
        item_name_len = len(item_name)
        self.x_size = 15 * item_name_len 
        rectangle_surface = pygame.Surface((self.x_size, self.y_size), pygame.SRCALPHA)
        rectangle_color = (0, 0, 0, 200)  # Black with 50% transparency (128 out of 255)
        rectangle_surface.fill(rectangle_color)
        return rectangle_surface

    def Text_Box_Setup(self, surf, item_name, offset):
        # Scale the textbox to the name of the item
        
        rectangle_surface = self.Set_Text_Box_Size(item_name)
        text_box_pos = self.Set_Text_Box_pos(offset)

        surf.blit(rectangle_surface, text_box_pos)
        return text_box_pos

    def Render(self, surf, offset=(0, 0)):
        if not self.render:
            return
        item_name = self.Edit_Item_Name()

        
        text_box_pos = self.Text_Box_Setup(surf, item_name, offset)
        self.game.default_font.Render_Word(surf, item_name, text_box_pos)

        if self.item.sub_category == 'weapon':
            self.Render_Weapon(surf, text_box_pos)

        elif self.item.sub_category == 'potion':
            self.Render_Potion(surf, text_box_pos)

        elif self.item.sub_category == 'loot':
            if self.item.type == 'gold':
                self.Render_Gold(surf, text_box_pos)
            else:
                self.Render_Loot(surf, text_box_pos)

        elif self.item.sub_category == 'rune':
            self.Render_Rune(surf, text_box_pos)

        else:
            print(self.item.sub_category)

    def Render_Rune(self, surf, text_box_pos):
        # Render Soul Cost
        self.game.symbols.Render_Symbol(surf, 'soul',  (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.current_soul_cost), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        # Render Power
        self.game.symbols.Render_Symbol(surf, 'power',  (text_box_pos[0], text_box_pos[1] + 40))
        self.game.default_font.Render_Word(surf, str(self.item.current_power), (text_box_pos[0] + 20, text_box_pos[1] + 40))  



    def Render_Loot(self, surf, text_box_pos):
        self.game.symbols.Render_Symbol(surf, 'gold',  (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.value), (text_box_pos[0] + 20, text_box_pos[1] + 20))        
    
    def Render_Gold(self, surf, text_box_pos):
        self.game.symbols.Render_Symbol(surf, 'gold',  (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.amount), (text_box_pos[0] + 20, text_box_pos[1] + 20)) 

    def Render_Potion(self, surf, text_box_pos):

        self.game.symbols.Render_Symbol(surf, self.item.effect,  (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.amount), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        self.game.symbols.Render_Symbol(surf, 'gold',  (text_box_pos[0], text_box_pos[1] + 40))
        self.game.default_font.Render_Word(surf, str(self.item.value), (text_box_pos[0] + 20, text_box_pos[1] + 40))        




    def Render_Weapon(self, surf, text_box_pos):
        
        # Render Damage and damage type
        self.game.symbols.Render_Symbol(surf, self.item.effect,  (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.damage), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        # Render Damage and damage type
        self.game.symbols.Render_Symbol(surf, "speed",  (text_box_pos[0], text_box_pos[1] + 40))
        self.game.default_font.Render_Word(surf, str(self.item.speed), (text_box_pos[0] + 20, text_box_pos[1] + 40))

        # Render Damage and damage type
        self.game.symbols.Render_Symbol(surf, 'arrow',  (text_box_pos[0], text_box_pos[1] + 60))
        self.game.default_font.Render_Word(surf, str(self.item.range), (text_box_pos[0] + 20, text_box_pos[1] + 60))

        # Render value
        surf.blit(self.game.assets['gold'][0], (text_box_pos[0], text_box_pos[1] + 80))
        self.game.default_font.Render_Word(surf, str(self.item.value), (text_box_pos[0] + 20, text_box_pos[1] + 80))