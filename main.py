import pygame

from scripts.game.game_initialiser import Game_Initialiser
from scripts.game.level_loader import Level_Loader
from scripts.game.camera_update import Camera_Update
from scripts.game.input_update import Input_Update
from scripts.game.logic_update import Logic_Update
from scripts.game.renderer import Renderer
from scripts.game.state_machine import State_Machine
from scripts.game.save_load_manager import Save_Load_Manager

import pygame


class Game:
    def __init__(self):
        self.save_load_manager = Save_Load_Manager(self, ".data", "save_data")
        
        # self.game_initialiser.Initialise_Game()

        # self.level_loader.load_level_From_Save(self.level)
        # self.level_loader.Load_Level_New_Map(self.level)

        self.state_machine = State_Machine(self)
        
        
        

    def run(self):  
        while True:
            self.state_machine.Game_State()
            
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()