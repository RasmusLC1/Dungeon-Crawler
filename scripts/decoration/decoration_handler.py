from scripts.decoration.decoration import Decoration
from scripts.entities.items.weapons.close_combat.torch import Torch
import math

class Decoration_Handler():
    def __init__(self, game):
        self.game = game
        self.decorations = []
        self.nearby_decoration = []
        self.Initialise()

    def Initialise(self):
        pass
        # top pusher initialisation
        # for torch in self.game.tilemap.extract([('torch', 0)].copy()):
        #     self.decorations.append(Torch(self.game, torch['pos'], (self.game.assets[torch['type']][0].get_width(), self.game.assets[torch['type']][0].get_height()), torch['type']))

    def find_nearby_decoration(self, player_pos, max_distance):
        nearby_decoration = []
        for decoration in self.decorations:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
            if distance < max_distance:
                nearby_decoration.append(decoration)
        return nearby_decoration

    def Update(self):
        self.nearby_decoration = self.find_nearby_decoration(self.game.player.pos, 200)
        for decoration in self.nearby_decoration:
            decoration.Animation_Update()

    def Render(self, decorations, surf, render_scroll = (0, 0)):
        for decoration in decorations:
            decoration.Render(surf, render_scroll)