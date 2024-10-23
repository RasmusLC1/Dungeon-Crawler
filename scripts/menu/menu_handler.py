from scripts.menu.pause_menu import Pause_Menu
from scripts.menu.main_menu import Main_Menu


class Menu_Handler():
    def __init__(self, game):
        self.game = game
        self.pause_menu = Pause_Menu(self.game)
        self.main_menu = Main_Menu(self.game)


    
    def Select_Menu(self, menu):
        if menu == 'pause_menu':
            self.Menu_Updater(self.pause_menu)
        elif menu == 'main_menu':
            self.Menu_Updater(self.main_menu)

    def Menu_Updater(self, menu):
        menu.Update()
        menu.Render(self.game.display)