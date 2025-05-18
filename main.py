import pygame

from scripts.game.input_update import Input_Update
from scripts.game.state_machine import State_Machine
from scripts.game.save_load_manager import Save_Load_Manager

class Game:
    def __init__(self):
        pygame.init()
        self.save_load_manager = Save_Load_Manager(self, ".data", "save_data")
        

        self.state_machine = State_Machine(self)
        self.input_update = Input_Update(self)
        self.clock = pygame.time.Clock()


        
    def Update_Display(self):
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
        pygame.display.update()
        

    def run(self):  
        while True:
            fps = int(self.clock.get_fps())
            pygame.display.set_caption('Dungeon Crawler             FPS: ' + str(fps))
            
            
            self.state_machine.Game_State()
            
            self.input_update.Input_Handler()
            
            self.Update_Display()
            self.clock.tick(60)



Game().run()

