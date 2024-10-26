
from scripts.game.camera_update import Camera_Update
from scripts.game.input_update import Input_Update
from scripts.game.logic_update import Logic_Update
from scripts.game.renderer import Renderer
from scripts.game.game_initialiser import Game_Initialiser
from scripts.game.level_loader import Level_Loader
import pygame
import sys

class State_Machine():
    def __init__(self, game) -> None:
        self.game = game
        self.game_state = 'init'
        self.game.game_initialiser = Game_Initialiser(self.game)
        self.game.level_loader = Level_Loader(self.game)
        self.game.camera_update = Camera_Update(self.game)
        self.game.logic_update = Logic_Update(self.game)
        self.game.renderer = Renderer(self.game)


    def Game_State(self):
        # print(self.game_state)
        if self.game_state == 'run_game':
            self.Game_Loop()
        elif self.game_state == 'main_menu':
            self.Main_Menu()
        elif self.game_state == 'pause_menu':
            self.Pause_Menu()
        elif self.game_state == 'shrine_menu':
            self.Shrine_Menu()
        elif self.game_state == 'exit_game':
            self.Exit_Game()
        elif self.game_state == 'load_game':
            self.Game_Load()
        elif self.game_state == 'new_game':
            self.New_Game()
        elif self.game_state == 'init':
            self.Initialise_Game()

    def Initialise_Game(self):
        self.game.game_initialiser.Initialise_Game()
        self.game_state = 'main_menu'


    def Set_State(self, state):
        self.game_state = state
        

    def Game_Load(self):

        self.game.level_loader.load_level_From_Save(self.game.level)

        self.Set_State('run_game')

    
    def New_Game(self):
        self.game.level_loader.Load_Level_New_Map(self.game.level)

        self.Set_State('run_game')

    def Game_Loop(self):
        self.game.camera_update.Camera_Scroll()
        self.game.renderer.Render()
        self.game.logic_update.Update()

    def Main_Menu(self):
        self.game.menu_handler.Select_Menu('main_menu')
        

    def Pause_Menu(self):
        self.game.menu_handler.Select_Menu('pause_menu')

    def Shrine_Menu(self):
        self.game.menu_handler.Select_Menu('shrine_menu')

        # Reset the buy menu if exited
        if self.game_state != 'shrine_menu':
            self.game.menu_handler.shrine_menu.Reset_Rune_Bought()



    def Exit_Game(self):
        self.game.save_load_manager.Save_Data_Structure()
        pygame.quit()
        sys.exit()

