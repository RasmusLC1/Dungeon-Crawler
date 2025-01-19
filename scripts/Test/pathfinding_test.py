import pygame

class Pathfinding_Test():
    def __init__(self, game) -> None:
        self.game = game
        self.initialised = False
        self.tiles = []

    def Initialise(self):
        if self.initialised:
              return
        self.Update_Background_Image()
        self.Increase_Brightness()
        self.game.render_scale = 0.5
        self.game.display = pygame.Surface((self.game.screen_width/self.game.render_scale, self.game.screen_height/self.game.render_scale))
        self.game.camera_update.Set_Camera_Position((0, 0))
        self.initialised = True



    def Update_Background_Image(self):
        self.back_ground_image = pygame.transform.scale(self.game.assets['background'], (self.game.screen_width/self.game.render_scale, self.game.screen_height/self.game.render_scale))


    def Increase_Brightness(self):
        
        self.game.tilemap.Set_Global_Brightness(256)

    def Update(self):
        self.Initialise()
        self.Check_Keyboard_Input()
        self.Render()


    def Update_Path(self):
        # Reset tiles
        if self.tiles:
            for tile in self.tiles:
                tile.Set_Type('floor')
            self.tiles.clear()

        # self.game.
        

    def Render(self):
        self.game.display.blit(self.back_ground_image, (0, 0))
        
        self.game.tilemap.Render(self.game.display, offset=self.game.render_scroll)
            
    def Check_Keyboard_Input(self):
         if self.game.keyboard_handler.escape_pressed:
            self.game.keyboard_handler.Set_Escape_Key(False)
            self.game.state_machine.Set_State('pause_menu')