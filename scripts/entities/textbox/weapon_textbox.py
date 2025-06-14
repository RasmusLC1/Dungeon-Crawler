from scripts.entities.textbox.textbox import Text_Box


class Weapon_Textbox(Text_Box):

    def Set_Y_Size(self):
        self.y_size = 80

    # def Set_X_Size(self, entity_name):
    #     self.x_size = 150

    def Set_Text_Box_pos(self, offset):
        text_box_pos = (0,0)
        # Render entitybox different depending on if it's picked up or not
        if self.entity.picked_up:
            try:
                inventory_slot = self.entity.game.inventory.Find_Inventory_Slot(self.entity.inventory_index)
                if not inventory_slot:
                    return
                text_box_pos = (inventory_slot.pos[0], inventory_slot.pos[1] -  self.y_size)
            except TypeError as e:
                print(f"Item does not have index {e}", self.entity.type, self.entity.inventory_index, inventory_slot)
        
        else:
            text_box_pos = (self.entity.pos[0] - offset[0], self.entity.pos[1] - offset[1] - self.y_size)
        
        return text_box_pos
    