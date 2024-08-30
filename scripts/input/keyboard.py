import pygame


class Keyboard_Handler:
    def keyboard_Input(self, key_press, offset=(0, 0)):
        if key_press.type == pygame.KEYDOWN:
            if key_press.key == pygame.K_a:
                self.movement[0] = True
            if key_press.key == pygame.K_d:
                self.movement[1] = True
            if key_press.key == pygame.K_w:
                self.movement[2] = True
            if key_press.key == pygame.K_s:
                self.movement[3] = True

            if key_press.key == pygame.K_e:
                nearby_items = self.item_handler.Find_Nearby_Item(self.player.pos, 30)
                for item in nearby_items:
                    item.Pick_Up()

                nearby_chests = self.chest_handler.Find_Nearby_Chests(self.player.pos, 30)
                self.chest_handler.Open_Chests(nearby_chests)

            if key_press.key == pygame.K_SPACE:
                pass
            if key_press.key == pygame.K_x:
                self.player.Dash(offset)
        if key_press.type == pygame.KEYUP:
            if key_press.key == pygame.K_a:
                self.movement[0] = False
            if key_press.key == pygame.K_d:
                self.movement[1] = False
            if key_press.key == pygame.K_w:
                self.movement[2] = False
            if key_press.key == pygame.K_s:
                self.movement[3] = False
    
    # Debugging and adjustment function, modify depending on animation needing to be done
    def Animation_Adjustment_Helper(self, key_press):
        
        if key_press.key == pygame.K_p:
            if self.player.active_weapon_left:
                try:
                    self.player.active_weapon_left.Modify_Offset(1)
                except Exception as e:
                    print(f"Font load error: {e}")
            if self.player.active_weapon_right:
                try:
                    self.player.active_weapon_right.Modify_Offset(1)
                except Exception as e:
                    print(f"Font load error: {e}")
        if key_press.key == pygame.K_MINUS:
            if self.player.active_weapon_left:
                try:
                    self.player.active_weapon_left.Modify_Offset(-1)
                except Exception as e:
                    print(f"Font load error: {e}")
            if self.player.active_weapon_right:
                try:
                    self.player.active_weapon_right.Modify_Offset(-1)
                except Exception as e:
                    print(f"Font load error: {e}")