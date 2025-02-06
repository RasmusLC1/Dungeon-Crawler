from scripts.menu.button import Button
import math

class Portal_Button(Button):
    def __init__(self, game, pos, size, text, color = (0, 0, 0)) -> None:
        self.unlock_cost = 50 + game.level * 30
        text = text + ': ' + str(self.unlock_cost)
        super().__init__(game, pos, size, text, 'None', False, color)


    def Update(self):
        self.game.mouse.Menu_Mouse_Update()
        if self.rect().colliderect(self.game.mouse.rect_pos_menu()):
            # Brighten the color of the button on hover
            color_0 = min(250, min(self.background_color_holder[0] * 1.3, self.background_color[0] + self.button_speed))
            color_1 = min(250, min(self.background_color_holder[1] * 1.3, self.background_color[1] + self.button_speed))
            color_2 = min(250, min(self.background_color_holder[2] * 1.3, self.background_color[2] + self.button_speed))
            self.background_color = (color_0, color_1, color_2)
            self.rect_surface.fill(self.background_color)

            # Check if player can afford cost when clicking
            if self.rect().colliderect(self.game.mouse.rect_click()):
                if self.game.player.souls >= self.unlock_cost:
                    self.game.player.Decrease_Souls(self.unlock_cost)
                    self.game.state_machine.Set_State('run_game')
                    return True
            
            return False
        
        self.Reset_Color()
        return False
    
    def Render(self, surf):
        super().Render(surf)
        self.game.symbols.Render_Symbol(surf, 'soul',  (round(self.pos[0] + self.size[0] - 40), self.pos[1] + self.size[1] // 2 - 8))


