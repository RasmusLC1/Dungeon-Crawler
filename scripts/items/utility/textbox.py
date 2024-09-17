import pygame

class Text_Box():
    def __init__(self, game, item) -> None:
        self.game = game
        self.item = item
        self.render = False

    def Update(self, offset):
        
        
        # Handle when item is in inventory
        if self.item.picked_up:
            if self.item.rect().colliderect(self.game.mouse.rect_pos(self.game.render_scroll)):
                self.render = True
                return
        else:
            if self.item.rect().colliderect(self.game.mouse.rect_pos()):
                self.render = True
                return
        if self.render:
            self.render = False

    
    def Render(self, surf, offset=(0, 0)):
        if not self.render:
            return
        x_size = 40
        y_size = 30
        rectangle_surface = pygame.Surface((x_size, y_size), pygame.SRCALPHA)
        rectangle_color = (0, 0, 0, 200)  # Black with 50% transparency (128 out of 255)
        rectangle_surface.fill(rectangle_color)

    
        if self.item.picked_up:
            x_pos = self.item.pos[0] - x_size / 4
            y_pos = self.item.pos[1] - y_size
            surf.blit(rectangle_surface, (x_pos, y_pos))
            self.game.default_font.Render_Word(surf, self.item.type, (x_pos, y_pos))
            if self.item.category == 'weapon':
                # damage_text = 'Damage: ' + str(self.item.damage)
                # print(damage_text)
                self.game.default_font.Render_Word(surf, str(self.item.damage), (x_pos, y_pos + 10))
                # self.game.default_font.Render_Word(surf, str(self.item.range), (x_pos, y_pos - 20))
        else:
            surf.blit(rectangle_surface, (self.item.pos[0] - offset[0], self.item.pos[1] - offset[1] - y_size))