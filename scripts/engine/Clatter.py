
class Clatter():
    def __init__(self, game) -> None:
        self.game = game


    def Generate_Clatter(self, center, range): 
        nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.game.player, range)
        for enemy in nearby_enemies:
            if not enemy:
                continue
            print(enemy)
            enemy.Find_New_Path(center)
            print("CENTER", center)


    