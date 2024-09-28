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
                self.Inventory_Keybindings(0)
            if key_press.key == pygame.K_2:
                self.Inventory_Keybindings(1)
            if key_press.key == pygame.K_3:
                self.Inventory_Keybindings(2)
            if key_press.key == pygame.K_4:
                self.Inventory_Keybindings(3)
            if key_press.key == pygame.K_5:
                self.Inventory_Keybindings(4)
            if key_press.key == pygame.K_6:
                self.Inventory_Keybindings(5)
            if key_press.key == pygame.K_7:
                self.Inventory_Keybindings(6)
            if key_press.key == pygame.K_e:
                nearby_items = self.game.item_handler.Find_Nearby_Item(self.game.player.pos, 30)
                for item in nearby_items:
                    item.Pick_Up()

                nearby_chests = self.game.chest_handler.Find_Nearby_Chests(self.game.player.pos, 30)
                self.game.chest_handler.Open_Chests(nearby_chests)

            if key_press.key == pygame.K_SPACE:
                self.game.player.movement_handler.Roll_Forward(offset)
            if key_press.key == pygame.K_x:
                self.game.player.movement_handler.Dash(offset)
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
    
    def Inventory_Keybindings(self, inventory_index):
        inventory_slot = self.game.item_inventory.inventory[inventory_index]
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

    