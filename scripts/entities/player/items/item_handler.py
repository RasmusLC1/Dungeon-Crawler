from scripts.decoration.decoration import Decoration
from scripts.entities.player.items.weapons.torch import Torch
import math

class Item_Handler():
    def __init__(self, game):
        self.game = game
        self.items = []
        self.nearby_decoration = []
        self.Initialise()

    def Initialise(self):
        # top pusher initialisation
        for torch in self.game.tilemap.extract([('torch', 0)].copy()):
            pass
            self.items.append(Torch(self.game, torch['pos'], (self.game.assets[torch['type']][0].get_width(), self.game.assets[torch['type']][0].get_height()), torch['type']))

    def Add_Item(self, item):
        self.items.append(item)

        # self.game.entities_render.append(item)

    def Remove_Item(self, item):
        self.items.remove(item)


    def find_nearby_item(self, player_pos, max_distance):
        nearby_decoration = []
        for decoration in self.items:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
            if distance < max_distance:
                nearby_decoration.append(decoration)
        return nearby_decoration

    def Update(self):
        for item in self.items:
            item.Update_Animation()
            if not item.picked_up:
                    self.items.remove(item)

    def Render(self, decorations, surf, render_scroll = (0, 0)):
        for decoration in decorations:
            decoration.Render(surf, render_scroll)