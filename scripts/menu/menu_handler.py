from scripts.menu.pause_menu import Pause_Menu
from scripts.menu.main_menu import Main_Menu
from scripts.menu.shrine_menu import Shrine_Menu
from scripts.menu.loading_menu import Loading_Menu


class Menu_Handler():
    def __init__(self, game):
        self.game = game
        self.pause_menu = Pause_Menu(self.game)
        self.main_menu = Main_Menu(self.game)
        self.shrine_menu = Shrine_Menu(self.game)
        self.loading_menu = Loading_Menu(self.game)


    
    def Select_Menu(self, menu):
        if menu == 'pause_menu':
            self.Menu_Updater(self.pause_menu)
        elif menu == 'main_menu':
            self.Menu_Updater(self.main_menu)
        elif menu == 'shrine_menu':
            self.Menu_Updater(self.shrine_menu)
        elif menu == 'loading_menu':
            self.Menu_Updater(self.loading_menu)

    def Menu_Updater(self, menu):
        menu.Update()
        menu.Render(self.game.display)

    def Loading_Menu_Reset(self):
        self.loading_menu.Reset()

    def Loading_Menu_Update(self, value):
        self.loading_menu.Update(value)
        self.loading_menu.Render(self.game.display)