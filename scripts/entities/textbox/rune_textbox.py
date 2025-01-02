from scripts.entities.textbox.textbox import Text_Box

class Rune_Textbox(Text_Box):

    def Edit_Entity_Name(self):
        entity_name = super().Edit_Entity_Name()
        entity_name = entity_name.replace('_rune', '')
        return entity_name

    def Set_Text_Box_pos(self, offset):
        text_box_pos = (self.entity.game.screen_width // self.entity.game.render_scale - self.x_size - 20, self.entity.pos[1] -  self.y_size - 20)
        return text_box_pos


    def Render(self, surf, text_box_pos):
        text_box_pos = super().Render(surf, text_box_pos)

        # Render Soul Cost
        self.entity.game.symbols.Render_Symbol(surf, 'soul',  (text_box_pos[0], text_box_pos[1] + 20))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.current_soul_cost), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        # Render Power
        self.entity.game.symbols.Render_Symbol(surf, 'power',  (text_box_pos[0], text_box_pos[1] + 40))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.current_power), (text_box_pos[0] + 20, text_box_pos[1] + 40))  


