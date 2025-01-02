from scripts.entities.textbox.textbox import Text_Box


class Weapon_Textbox(Text_Box):

    def Set_Y_Size(self):
        self.y_size = 100


    def Render(self, surf, text_box_pos):
        text_box_pos = super().Render(surf, text_box_pos)
        
        # Render Damage and damage type
        self.entity.game.symbols.Render_Symbol(surf, self.entity.effect,  (text_box_pos[0], text_box_pos[1] + 20))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.damage), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        # Render Damage and damage type
        self.entity.game.symbols.Render_Symbol(surf, "speed",  (text_box_pos[0], text_box_pos[1] + 40))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.speed), (text_box_pos[0] + 20, text_box_pos[1] + 40))

        # Render Damage and damage type
        self.entity.game.symbols.Render_Symbol(surf, 'arrow',  (text_box_pos[0], text_box_pos[1] + 60))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.range), (text_box_pos[0] + 20, text_box_pos[1] + 60))

        # Render value
        surf.blit(self.entity.game.assets['gold'][0], (text_box_pos[0], text_box_pos[1] + 80))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.value), (text_box_pos[0] + 20, text_box_pos[1] + 80))