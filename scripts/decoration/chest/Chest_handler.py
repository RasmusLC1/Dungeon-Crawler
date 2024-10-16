from scripts.decoration.chest.chest import Chest
import math

class Chest_Handler:
    def __init__(self, game) -> None:
        self.game = game
        self.chests = []
        depth = 3
        for chest in game.tilemap.extract([('Chest', 0)]):
            size = (game.assets[chest['type']][0].get_width(), game.assets[chest['type']][0].get_height())
            self.chests.append(Chest(game, chest['type'], chest['pos'], size, depth))  

    def Open_Chests(self, chests):
        if not chests:
            return False

        for chest in chests:
            chest.Open()
            self.chests.remove(chest)
            del(chest)
        
        return True

    def Find_Nearby_Chests(self, pos, max_distance):
        nearby_chests = []
        for chest in self.chests:  # Assuming self.traps is a list of traps
            # Calculate the Euclidean distance
            distance = math.sqrt((pos[0] - chest.pos[0]) ** 2 + (pos[1] - chest.pos[1]) ** 2)
            if distance < max_distance:
                nearby_chests.append(chest)
        return nearby_chests

    def Render(self, active_chests, surf, render_scroll = (0, 0)):
         for chest in active_chests:
            if not chest.text_cooldown:
                chest.Render(surf, render_scroll)
            else:
                chest.Render_text(surf, render_scroll)
