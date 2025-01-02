from scripts.entities.textbox.textbox import Text_Box

class Loot_Textbox(Text_Box):

    def Render(self, surf, text_box_pos):
        text_box_pos = super().Render(surf, text_box_pos)
        self.entity.game.symbols.Render_Symbol(surf, 'gold',  (text_box_pos[0], text_box_pos[1] + 20))
        if self.entity.type == 'gold':
            self.entity.game.default_font.Render_Word(surf, str(self.entity.amount), (text_box_pos[0] + 20, text_box_pos[1] + 20)) 
        else:
            self.entity.game.default_font.Render_Word(surf, str(self.entity.value), (text_box_pos[0] + 20, text_box_pos[1] + 20))        

        return