import json
from scripts.lighting import LIGHT
import pygame
from pygame.locals import *

class Light_Handler:
    def __init__(self, game):
        self.light_test = LIGHT(150, (255, 185, 9), 1, False)
        self.lights = []

    def Update(self, render_scroll):
        if pygame.mouse.get_pressed()[1]: self.lights.append([LIGHT(150, (255, 185, 9), 1, False), [mx,my]])
        lights_display = pygame.Surface((self.display.get_size()))
        mx, my = pygame.mouse.get_pos()
        self.light_test.main(self.shadow_map, lights_display, self.player.pos[0] - render_scroll[0], self.player.pos[1] - render_scroll[1])

        self.display.blit(lights_display, (0,0), special_flags=BLEND_RGBA_MULT)
        for light in self.lights:
            light[0].main(self.shadow_map, lights_display, light[1][0], light[1][1])
            # self.display.blit(tiles_textures[90], (light[1][0]-8,light[1][1]-8))
        
        self.display.blit(lights_display, (0,0), special_flags=BLEND_RGBA_MULT)

    def Setup_Shadow_Map(self):
        FLOOR_TILE = ['Floor', 'spike', 'spike_poison', 'BearTrap', 'PitTrap', 'TopPush', 'Fire_Trap', 'Lava', 'shallow_water', 'medium_water', 'deep_water', 'shallow_ice', 'medium_ice', 'deep_ice']
        tile_map = []  # This will be a list of lists, each representing a row.

        f = open('data/maps/0.json', 'r')
        map_data = json.load(f)
        f.close()

        # Assuming 'tilemap' is a dictionary with nested dictionaries
        tilemap = map_data['tilemap']
        self.min_x = 9999
        self.max_x = -9999
        self.min_y = 9999
        self.max_y = -9999
        
        for key, value in tilemap.items():
            
            pos_x = value['pos'][0]  # Extract the y value from the position
            if pos_x < self.min_x:
                self.min_x = pos_x
            if pos_x > self.max_x:
                self.max_x = pos_x

            pos_y = value['pos'][1]  # Extract the y value from the position
            if pos_y < self.min_y:
                self.min_y = pos_y
            if pos_y > self.max_y:
                self.max_y = pos_y

        self.row = self.max_y - self.min_y + 1
        self.col = self.max_x - self.min_x + 1
        for x in range(self.min_x, self.max_x+1):
            row = []
            for y in range(self.min_y, self.max_y+1):
                tile = self.tilemap.extract_On_Location([x, y])
                location = 1
                if tile in FLOOR_TILE:
                    location = 0
                
                row.append(location)
            # if not any(row):  # If the row is full of Nones or empty, stop adding new rows
            #     break
            tile_map.append(row)
        



        self.shadow_map = [list(row) for row in zip(*tile_map)]