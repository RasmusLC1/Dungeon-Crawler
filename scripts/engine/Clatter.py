
class Clatter():
    def __init__(self, game) -> None:
        self.game = game


    def Generate_Clatter(self, center, range):
        if self.game.player.effects.silence.effect:
            return

        nearby_enemies = self.game.enemy_handler.Find_Nearby_Enemies(self.game.player, range)
        for enemy in nearby_enemies:
            if not enemy:
                continue
            # Check if enemy already has a target
            if enemy.locked_on_target:
                continue
            self.game.enemy_handler.Add_To_Pathfinding_Queue(enemy, center)




    