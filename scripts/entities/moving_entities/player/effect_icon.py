from scripts.entities.textbox.effect_textbox import Effect_Textbox
import pygame

class Effect_Icon():
    def __init__(self, game):
        self.game = game
        self.effect = None
        self.pos = (-999, -999)
        self.size = (32, 32)
        self.textbox = Effect_Textbox(self)

    def Update(self):
        if not self.Check_Mouse_Collision():
            return

        print("TEXTBOX!!!!")    
    
    
    def Check_Mouse_Collision(self):
        return self.rect().colliderect(self.game.mouse.rect_pos())

    def Set_Effect(self, effect):
        self.effect = effect

    def Set_Position(self, pos):
        self.pos = pos

    def Set_Active(self, pos, effect):
        self.Set_Position(pos)
        self.Set_Effect(effect)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])