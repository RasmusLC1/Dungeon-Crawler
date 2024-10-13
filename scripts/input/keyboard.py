import pygame


class Keyboard_Handler:
    def __init__(self, game) -> None:
        self.game = game

    def keyboard_Input(self, key_press, offset=(0, 0)):
        if key_press.type == pygame.KEYDOWN:
            if key_press.key == pygame.K_a:
                self.game.movement[0] = True
            if key_press.key == pygame.K_d:
                self.game.movement[1] = True
            if key_press.key == pygame.K_w:
                self.game.movement[2] = True
            if key_press.key == pygame.K_s:
                self.game.movement[3] = True
            if key_press.key == pygame.K_1:
                self.Item_Inventory_Keybindings(0)
            if key_press.key == pygame.K_2:
                self.Item_Inventory_Keybindings(1)
            if key_press.key == pygame.K_3:
                self.Item_Inventory_Keybindings(2)
            if key_press.key == pygame.K_4:
                self.Item_Inventory_Keybindings(3)
            if key_press.key == pygame.K_5:
                self.Item_Inventory_Keybindings(4)
            if key_press.key == pygame.K_6:
                self.Item_Inventory_Keybindings(5)
            if key_press.key == pygame.K_7:
                self.Item_Inventory_Keybindings(6)
            if key_press.key == pygame.K_e:
                nearby_items = self.game.item_handler.Find_Nearby_Item(self.game.player.pos, 30)
                for item in nearby_items:
                    item.Pick_Up()

                if self.Check_Doors():
                    return
                
                if self.Check_Chests():
                    return

            if key_press.key == pygame.K_SPACE:
                self.game.player.movement_handler.Roll_Forward(offset)
            if key_press.key == pygame.K_z:
                self.Rune_Inventory_Keybindings(0)
            if key_press.key == pygame.K_x:
                self.Rune_Inventory_Keybindings(1)
            if key_press.key == pygame.K_c:
                self.Rune_Inventory_Keybindings(2)
            if key_press.key == pygame.K_LALT:
                self.game.player.movement_handler.Back_Step(offset)


        if key_press.type == pygame.KEYUP:
            if key_press.key == pygame.K_a:
                self.game.movement[0] = False
            if key_press.key == pygame.K_d:
                self.game.movement[1] = False
            if key_press.key == pygame.K_w:
                self.game.movement[2] = False
            if key_press.key == pygame.K_s:
                self.game.movement[3] = False
    
    def Check_Doors(self):
        key_found = False
        
        
        nearby_doors = self.game.door_handler.Find_Nearby_Doors(self.game.player.pos, 20)
        if not nearby_doors:
            return False
        
        for inventory_slot in self.game.item_inventory.inventory:
            if not inventory_slot.item:
                continue
            
            if inventory_slot.item.type == 'key':
                inventory_slot.Remove_Item()
                key_found = True
                break

        if not key_found:
            return False
        
        if self.game.door_handler.Open_Doors(nearby_doors):
            return True
        
        return False

    def Check_Chests(self):
        nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.game.player.pos, 10)
        if self.game.chest_handler.Open_Chests(nearby_chests):
            return True
        return False

    def Item_Inventory_Keybindings(self, inventory_index):
        inventory_slot = self.game.item_inventory.inventory[inventory_index]
        if inventory_slot.item:
            inventory_slot.item.Activate()
            inventory_slot.Update()

    def Rune_Inventory_Keybindings(self, inventory_index):
        inventory_slot = self.game.rune_inventory.inventory[inventory_index]
        if inventory_slot.item:
            inventory_slot.item.Activate()
            inventory_slot.Update()

    # # Debugging and adjustment function, modify depending on animation needing to be done
    # def Animation_Adjustment_Helper(self, key_press):
        
    #     if key_press.key == pygame.K_p:
    #         if self.player.active_weapon_left:
    #             try:
    #                 self.player.active_weapon_left.Modify_Offset(1)
    #             except Exception as e:
    #                 print(f"Font load error: {e}")
    #         if self.player.active_weapon_right:
    #             try:
    #                 self.player.active_weapon_right.Modify_Offset(1)
    #             except Exception as e:
    #                 print(f"Font load error: {e}")
    #     if key_press.key == pygame.K_MINUS:
    #         if self.player.active_weapon_left:
    #             try:
    #                 self.player.active_weapon_left.Modify_Offset(-1)
    #             except Exception as e:
    #                 print(f"Font load error: {e}")
    #         if self.player.active_weapon_right:
    #             try:
    #                 self.player.active_weapon_right.Modify_Offset(-1)
    #             except Exception as e:
    #                 print(f"Font load error: {e}")

    