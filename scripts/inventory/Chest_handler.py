from scripts.inventory.chest import Chest
import math

class Chest_Handler:
    def __init__(self, game):
        self.chests = []
        depth = 3
        for chest in game.tilemap.extract([('Chest', 0)]):
            self.chests.append(Chest(game, chest['pos'], (game.assets[chest['type']][0].get_width(), game.assets[chest['type']][0].get_height()), depth))  


    def Update(self):
        for chest in self.chests:
                if chest.empty:
                    if not chest.text_cooldown:
                        self.chests.remove(chest)
                else:
                    chest.Update()

    def find_nearby_chests(self, player_pos, max_distance):
        nearby_chests = []
        for chest in self.chests:  # Assuming self.traps is a list of traps
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - chest.pos[0]) ** 2 + (player_pos[1] - chest.pos[1]) ** 2)
            if distance < max_distance:
                nearby_chests.append(chest)
        return nearby_chests

    def Render(self, active_chests, surf, render_scroll = (0, 0)):
         for chest in active_chests:
            if not chest.text_cooldown:
                chest.Render(surf, render_scroll)
            else:
                chest.Render_text(surf, render_scroll)
