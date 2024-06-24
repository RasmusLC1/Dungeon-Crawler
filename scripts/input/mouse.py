import pygame

class Mouse_Handler:
    def __init__(self, game):
        self.right_click = False
        self.left_click = False
        self.game = game
        self.click_pos = (0,0)
        self.mpos = (0, 0)
        self.mouse_rel = (0, 0)
        self.hold_down_left = 0
        self.hold_down_right = 0


    def Mouse_Input(self, key_press, offset=(0, 0)):

        if self.left_click:
            self.hold_down_left += 1
        elif not self.left_click and self.hold_down_left:
            self.hold_down_left = 0
            print(self.hold_down_left)

        if key_press.type == pygame.MOUSEBUTTONDOWN:
            # Check for left click (button 1)
            if key_press.button == 1:
                self.left_click = True
                self.click_pos = ((key_press.pos[0] / 4), (key_press.pos[1] / 4))
            # Check for right click (button 3)
            if key_press.button == 3:
                self.right_click = True
                self.click_pos = (key_press.pos[0] / 4, key_press.pos[1] / 4)
                self.hold_down_right += 1
        if key_press.type == pygame.MOUSEBUTTONUP:
            # Check for left click (button 1)
            if key_press.button == 1:
                self.left_click = False
                self.click_pos = 0
            # Check for right click (button 3)
            if key_press.button == 3:
                self.right_click = False
                self.click_pos = 0
        if key_press.type == pygame.MOUSEMOTION:
            if self.left_click == True:
                x = key_press.pos[0] / 4 + offset[0]
                y = key_press.pos[1] / 4 + offset[1]
                self.mpos = (x, y)
                # for item in self.game.items:  # Assuming you have a list of items
                #     item.Move(self.mpos)
            


    def mouse_rect(self):
        return pygame.Rect(self.click_pos[0], self.click_pos[1], 1, 1)    