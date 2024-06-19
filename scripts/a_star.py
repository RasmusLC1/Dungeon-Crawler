import json
import pygame
import numpy as np


class A_Star:
    def Setup_Map(self):
        tile_map = []  # This will be a list of lists, each representing a row.

        f = open('data/maps/0.json', 'r')
        map_data = json.load(f)
        f.close()

        # Assuming 'tilemap' is a dictionary with nested dictionaries
        tilemap = map_data['tilemap']
        min_x = 9999
        max_x = -9999
        min_y = 9999
        max_y = -9999
        for key, value in tilemap.items():
            
            pos_x = value['pos'][0]  # Extract the y value from the position
            if pos_x < min_x:
                min_x = pos_x
            if pos_x > max_x:
                max_x = pos_x

            pos_y = value['pos'][1]  # Extract the y value from the position
            if pos_y < min_y:
                min_y = pos_y
            if pos_y > max_y:
                max_y = pos_y
        print(min_x)
        print(max_x)
        print(min_y)
        print(max_y)

        for x in range(min_x, max_x+1):
            row = []
            for y in range(min_y, max_y+1):
                tile = self.tilemap.extract_On_Location([x, y])
                location = 1
                if tile == 'Floor':
                    location = 0
                
                row.append(location)
            if not any(row):  # If the row is full of Nones or empty, stop adding new rows
                break
            tile_map.append(row)
        transposed_map = [list(row) for row in zip(*tile_map)]

        # Printing the map
        for row in transposed_map:
            print(row)