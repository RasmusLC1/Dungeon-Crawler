from scripts.entities.textbox.textbox import Text_Box
import re

class Enemy_Textbox(Text_Box):


    def Edit_Entity_Name(self):
        entity_name = self.entity.type
        entity_name = entity_name.replace('skeleton_', '')
         # Remove _ followed by an integer
        entity_name = re.sub(r'_\d+', '', entity_name)
        return entity_name
    
    def Set_Text_Box_pos(self, offset):
        text_box_pos = (0,0)
        text_box_pos = (self.entity.pos[0] - offset[0], self.entity.pos[1] - offset[1] - self.y_size)
        return text_box_pos
    

    # Seperate function for size flexibility
    def Set_Y_Size(self):
        self.y_size = 80


    def Render(self, surf, text_box_pos):
        text_box_pos = super().Render(surf, text_box_pos)

        # Render health
        self.entity.game.symbols.Render_Symbol(surf, 'health',  (text_box_pos[0], text_box_pos[1] + 20))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.health), (text_box_pos[0] + 20, text_box_pos[1] + 20))

        # Render strength
        self.entity.game.symbols.Render_Symbol(surf, 'increase_strength',  (text_box_pos[0], text_box_pos[1] + 40))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.strength), (text_box_pos[0] + 20, text_box_pos[1] + 40))  

        # Render speed
        self.entity.game.symbols.Render_Symbol(surf, 'speed',  (text_box_pos[0], text_box_pos[1] + 60))
        self.entity.game.default_font.Render_Word(surf, str(self.entity.agility), (text_box_pos[0] + 20, text_box_pos[1] + 60)) 
