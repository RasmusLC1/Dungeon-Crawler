import pygame

from scripts.game.game_initialiser import Game_Initialiser
from scripts.game.level_loader import Level_Loader
from scripts.game.camera_update import Camera_Update
from scripts.game.input_update import Input_Update
from scripts.game.logic_update import Logic_Update
from scripts.game.state_machine import State_Machine
from scripts.game.save_load_manager import Save_Load_Manager

import pygame


class Game:
    def __init__(self):
        self.save_load_manager = Save_Load_Manager(self, ".data", "save_data")
        

        self.state_machine = State_Machine(self)
        self.input_update = Input_Update(self)
        self.clock = pygame.time.Clock()


        
        
        

    def run(self):  
        while True:
            fps = int(self.clock.get_fps())
            pygame.display.set_caption('Dungeons of Madness             FPS: ' + str(fps))
            
            
            self.state_machine.Game_State()
            
            self.input_update.Input_Handler()
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()