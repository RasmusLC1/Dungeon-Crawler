import pygame

class Text_Box():
    def __init__(self, game, item) -> None:
        self.game = game
        self.item = item
        self.render = False

    def Update(self, hitbox_1, hitbox_2):
        
        # Handle when item is in inventory
        if hitbox_1.colliderect(hitbox_2):
            self.render = True
            return True
        
        if self.render:
            self.render = False

        return False

    
    def Render(self, surf, offset=(0, 0)):
        if not self.render:
            return
        x_size = 40
        y_size = 30
        rectangle_surface = pygame.Surface((x_size, y_size), pygame.SRCALPHA)
        rectangle_color = (0, 0, 0, 200)  # Black with 50% transparency (128 out of 255)
        rectangle_surface.fill(rectangle_color)
        if self.item.picked_up:
            text_box_pos = (self.item.pos[0], self.item.pos[1] -  30)
        else:
            text_box_pos = (self.item.pos[0] - offset[0], self.item.pos[1] - offset[1] - 30)

        surf.blit(rectangle_surface, text_box_pos)
        if self.item.category == 'weapon':
            self.Render_Weapon(surf, text_box_pos)
        elif self.item.category == 'potion':
            self.Render_Potion(surf, text_box_pos)


    def Render_Potion(self, surf, text_box_pos):
        effect = self.item.type.replace('_potion', '')
        self.game.default_font.Render_Word(surf, effect, text_box_pos)

        self.game.potion_symbols.Render_Symbol(surf, effect,  (text_box_pos[0], text_box_pos[1] + 10))
        self.game.default_font.Render_Word(surf, str(self.item.effect), (text_box_pos[0] + 10, text_box_pos[1] + 10))

        surf.blit(self.game.assets['gold_coins'][0], (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.value), (text_box_pos[0] + 10, text_box_pos[1] + 20))        




    def Render_Weapon(self, surf, text_box_pos):
        # Render weapon name
        self.game.default_font.Render_Word(surf, self.item.type, text_box_pos)

        # Render Damage and damage type
        self.game.damage_symbols.Render_Symbol(surf, self.item.damage_type,  (text_box_pos[0], text_box_pos[1] + 10))
        self.game.default_font.Render_Word(surf, str(self.item.damage), (text_box_pos[0] + 10, text_box_pos[1] + 10))

        # Render value
        surf.blit(self.game.assets['gold_coins'][0], (text_box_pos[0], text_box_pos[1] + 20))
        self.game.default_font.Render_Word(surf, str(self.item.value), (text_box_pos[0] + 10, text_box_pos[1] + 20))