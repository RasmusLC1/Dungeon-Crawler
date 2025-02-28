from scripts.entities.textbox.textbox import Text_Box


class Weapon_Textbox(Text_Box):

    def Set_Y_Size(self):
        self.y_size = 100

    def Set_Text_Box_pos(self, offset):
        
        text_box_pos = (0,0)
        # Render entitybox different depending on if it's picked up or not
        if self.entity.picked_up:
            # text_box_pos = (self.entity.pos[0], self.entity.pos[1] -  self.y_size)
            inventory_slot = self.entity.game.inventory.Find_Inventory_Slot(self.entity.inventory_index)
            if not inventory_slot:
                return None
            text_box_pos = (inventory_slot.pos[0], inventory_slot.pos[1] -  self.y_size)
        else:
            text_box_pos = (self.entity.pos[0] - offset[0], self.entity.pos[1] - offset[1] - self.y_size)
        
        return text_box_pos
    

        