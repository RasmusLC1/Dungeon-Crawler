from scripts.entities.textbox.textbox import Text_Box



class Potion_Textbox(Text_Box):

    def Edit_Entity_Name(self):
        entity_name = super().Edit_Entity_Name()
        entity_name = entity_name.replace('_potion', '')
        return entity_name



    def Render(self, surf, text_box_pos):
        text_box_pos = super().Render(surf, text_box_pos)
        self.entity.game.symbols.Render_Symbol(surf, self.entity.effect,  (text_box_pos[0], text_box_pos[1] + 20))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.amount), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        self.entity.game.symbols.Render_Symbol(surf, 'gold',  (text_box_pos[0], text_box_pos[1] + 40))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.value), (text_box_pos[0] + 20, text_box_pos[1] + 40))

        return    

