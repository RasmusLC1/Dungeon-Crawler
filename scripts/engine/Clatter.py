
class Clatter():
    def __init__(self, game) -> None:
        self.game = game

    def Update(self):
        pass

    def Generate_Clatter(self, center, range): 
        nearby_enemies = self.game.enemy_handler.Find_Nerby_Enemies(self.game.player, range)


    