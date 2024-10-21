import pygame


class Keyboard_Handler:
    def __init__(self, game) -> None:
        self.game = game
        self.a_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.d_pressed = False
        self.e_pressed = False
        self.z_pressed = False
        self.x_pressed = False
        self.c_pressed = False
        self.space_pressed = False
        self.alt_pressed = False
        self._1_pressed = False
        self._2_pressed = False
        self._3_pressed = False
        self._4_pressed = False
        self._5_pressed = False
        self._6_pressed = False
        self._7_pressed = False
        self._8_pressed = False
        self._9_pressed = False

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
                self._1_pressed = True
            if key_press.key == pygame.K_2:
                self._2_pressed = True
            if key_press.key == pygame.K_3:
                self._3_pressed = True
            if key_press.key == pygame.K_4:
                self._4_pressed = True
            if key_press.key == pygame.K_5:
                self._5_pressed = True
            if key_press.key == pygame.K_6:
                self._6_pressed = True
            if key_press.key == pygame.K_7:
                self._7_pressed = True
            if key_press.key == pygame.K_e:
                nearby_items = self.game.item_handler.Find_Nearby_Item(self.game.player.pos, 30)
                for item in nearby_items:
                    item.Pick_Up()

                self.Check_Decorations()
                

            if key_press.key == pygame.K_SPACE:
                self.game.player.movement_handler.Roll_Forward(offset)
            if key_press.key == pygame.K_z:
                self.z_pressed = True
            if key_press.key == pygame.K_x:
                self.x_pressed = True
            if key_press.key == pygame.K_c:
                self.c_pressed = True
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
            if key_press.key == pygame.K_1:
                self._1_pressed = False
            if key_press.key == pygame.K_2:
                self._2_pressed = False
            if key_press.key == pygame.K_3:
                self._3_pressed = False
            if key_press.key == pygame.K_4:
                self._4_pressed = False
            if key_press.key == pygame.K_5:
                self._5_pressed = False
            if key_press.key == pygame.K_6:
                self._6_pressed = False
            if key_press.key == pygame.K_7:
                self._7_pressed = False
            if key_press.key == pygame.K_z:
                self.z_pressed = False
            if key_press.key == pygame.K_x:
                self.x_pressed = False
            if key_press.key == pygame.K_c:
                self.c_pressed = False
    
    

    def Check_Decorations(self):      
        nearby_decorations = self.game.decoration_handler.Find_Nearby_Decorations(self.game.player.pos, 20)
        if not nearby_decorations:
            return False
        
        self.game.decoration_handler.Open_Decoration(nearby_decorations)


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

    