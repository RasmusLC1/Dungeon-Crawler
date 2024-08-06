import pygame

class Mouse_Handler:
    def __init__(self, game):
        self.left_click = False  # Left mouse button has been clicked
        self.right_click = False  # Right mouse button has been clicked
        self.game = game  # Game
        self.click_pos = (0, 0)  # Get the position of the last click
        self.mpos = (0, 0)  # Mouse position, updated on clicks
        self.hold_down_left = 0  # Left mouse button hold down time in ticks
        self.hold_down_right = 0  # Right mouse button hold down time in ticks
        self.time_since_last_click = 0  # Check the time since last click
        self.double_click = 0  # Timer to signal double clicking
        self.single_click_delay = 0  # Single click timer

    # Mouse inputs that need to be updated for each frame
    def Mouse_Update(self):
        self.Double_Click_Timer()

    # Mouse inputs that only need to be updated when there is an input
    def Mouse_Input(self, key_press, offset=(0, 0)):
        self.Hold_Down_Left()
    
        if key_press.type == pygame.MOUSEBUTTONDOWN:
            if key_press.button == 1:  # Check for left click (button 1)
                self.left_click = True
                self.click_pos = (key_press.pos[0] / 4, key_press.pos[1] / 4)
                if self.time_since_last_click:
                    self.double_click = 20
                    # self.hold_down_left = 0

                self.time_since_last_click = 20

            if key_press.button == 3:  # Check for right click (button 3)
                self.right_click = True
                self.hold_down_right += 1

        if key_press.type == pygame.MOUSEBUTTONUP:
            if key_press.button == 1:  # Check for left click (button 1)
                self.left_click = False
                if not self.single_click_delay:
                    self.single_click_delay = 5  # Start the single click delay

            if key_press.button == 3:  # Check for right click (button 3)
                self.right_click = False

            if key_press.button in {4, 5}:  # Scroll wheel click
                self.game.weapon_inventory.Increment_inventory()

        if key_press.type == pygame.MOUSEMOTION:
            self.Mpos_Update(key_press, offset)

    def Hold_Down_Left(self):
        if self.left_click:
            self.hold_down_left += 1
        elif not self.left_click and self.hold_down_left:
            self.hold_down_left = 0

    def Double_Click_Timer(self):
        if self.time_since_last_click:
            self.time_since_last_click -= 1
        if self.double_click:
            self.double_click -= 1
        if self.single_click_delay:
            self.single_click_delay -= 1
            

        
    
    def Mpos_Update(self, key_press, offset=(0, 0)):
        if self.left_click == True:
            x = key_press.pos[0] / 4 + offset[0]
            y = key_press.pos[1] / 4 + offset[1]
            self.mpos = (x, y)
            self.mpos_not_offset = key_press.pos
            


    def rect_click(self):
        return pygame.Rect(self.click_pos[0], self.click_pos[1], 1, 1)    
    
    def rect_pos(self, offset):
        # print(self.mpos)
        return pygame.Rect(self.mpos[0] - offset[0], self.mpos[1]  - offset[1], 1, 1)  