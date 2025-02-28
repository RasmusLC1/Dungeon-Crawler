from scripts.entities.textbox.textbox import Text_Box

class Rune_Textbox(Text_Box):

    def Edit_Entity_Name(self):
        entity_name = super().Edit_Entity_Name()
        entity_name = entity_name.replace('_rune', '')
        return entity_name

    def Set_Text_Box_pos(self, offset):
        inventory_slot = self.entity.game.inventory.Find_Inventory_Slot(self.entity.inventory_index)
        if not inventory_slot:
            return None
        text_box_pos = (inventory_slot.pos[0], inventory_slot.pos[1] -  self.y_size)
        return text_box_pos