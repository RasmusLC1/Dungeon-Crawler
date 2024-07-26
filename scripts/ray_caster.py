import math
import pygame

class Ray_Caster():
    def __init__(self, game):
        self.tiles = []
        self.game = game

    def Ray_Caster(self, surf, offset=(0, 0)):
        self.tiles.clear()
        # Define the number of lines and the spread angle (in degrees)
        num_lines = 100
        spread_angle = 360  # Total spread of the fan (in degrees)
        
        # Calculate the angle increment between each line
        angle_increment = spread_angle / (num_lines - 1)
        
        # Calculate the starting angle
        base_angle = math.atan2(self.game.player.direction_y_holder, self.game.player.direction_x_holder)
        start_angle = base_angle - math.radians(spread_angle / 2)
        self.tiles.append(self.game.tilemap.Current_Tile((self.game.player.pos[0], self.game.player.pos[1])))
        # self.tiles.append(self.game.tilemap.Current_Tile((self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1])))
        # self.tiles.append(self.game.tilemap.Current_Tile((self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1])))
        # self.tiles.append(self.game.tilemap.Current_Tile((self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1])))
        # Draw the lines
        for j in range(num_lines):
            for i in range(1, 13):
                angle = start_angle + j * math.radians(angle_increment)
                pos_x = self.game.player.pos[0]  + math.cos(angle) * 16 * i
                pos_y = self.game.player.pos[1]  + math.sin(angle) * 16 * i
                tile = self.game.tilemap.Current_Tile((pos_x, pos_y))
                if tile:
                    self.tiles.append(tile)
                    if tile['type'] == 'BottomWall' or tile['type'] == 'TopWall' or tile['type'] == 'RightWall' or tile['type'] == 'LeftWall':
                        break
                # pygame.draw.line(surf, (255, 255, 255), (self.game.player.pos[0] - offset[0], self.game.player.pos[1] - offset[1]), (pos_x, pos_y), 1)

        # for tile in self.tiles:
        #     print(tile)