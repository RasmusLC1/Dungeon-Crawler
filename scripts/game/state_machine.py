
from scripts.game.camera_update import Camera_Update
from scripts.game.input_update import Input_Update
from scripts.game.logic_update import Logic_Update
from scripts.game.renderer import Renderer
from scripts.game.game_initialiser import Game_Initialiser
from scripts.game.level_loader import Level_Loader

class State_Machine():
    def __init__(self, game) -> None:
        self.game = game
        self.game_state_list = ['load_game', 'game', 'start_menu', 'pause_menu', 'shrine_menu']
        self.game_state = self.game_state_list[0]
        self.game.game_initialiser = Game_Initialiser(self.game)
        self.game.level_loader = Level_Loader(self.game)
        self.game.input_update = Input_Update(self.game)
        self.game.camera_update = Camera_Update(self.game)
        self.game.logic_update = Logic_Update(self.game)
        self.game.renderer = Renderer(self.game)


    def Game_State(self):
        if self.game_state == self.game_state_list[0]:
            self.Game_Load(False)
        elif self.game_state == self.game_state_list[1]:
            self.Game_Loop()
        elif self.game_state == self.game_state_list[2]:
            self.Start_Menu()
        elif self.game_state == self.game_state_list[3]:
            self.Pause_Menu()
        elif self.game_state == self.game_state_list[4]:
            self.Shrine_Menu()

    def Game_Load(self, load_from_save = False):
        self.game.game_initialiser.Initialise_Game()

        if load_from_save:
            self.game.level_loader.load_level_From_Save(self.game.level)
        else:
            self.game.level_loader.Load_Level_New_Map(self.game.level)

        self.game_state = self.game_state_list[1]

    def Game_Loop(self):
        self.game.camera_update.Camera_Scroll()
        self.game.renderer.Render()
        self.game.logic_update.Update()
        self.game.input_update.Input_Handler()

    def Start_Menu(self):
        pass

    def Pause_Menu(self):
        pass

    def Shrine_Menu(self):
        pass