import json
import pygame
import numpy as np
import math
import heapq


class A_Star:
    def __init__(self):
            self.parent_i = 0 # Parent cell's row index
            self.parent_j = 0 # Parent cell's column index
            self.f = float('inf') # Total cost of the cell (g + h)
            self.g = float('inf') # Cost from start to this cell
            self.h = 0 # Heuristic cost from this cell to destination
            self.x_min = 0
            self.y_min = 0
            self.x_max = 0
            self.y_max = 0
            self.row = 0
            self.col = 0
            self.map = []

    

    def Setup_TileMap(self, game):
        self.map.clear()
        # Extract all pos values
        positions = game.tilemap.Get_Pos()

        # Separate x and y coordinates
        x_coords = [pos[0] for pos in positions]
        y_coords = [pos[1] for pos in positions]

        # Find min and max for x and y coordinates
        self.min_x = min(x_coords)
        self.max_x = max(x_coords)
        self.min_y = min(y_coords)
        self.max_y = max(y_coords)

        self.row = self.max_y - self.min_y + 1
        self.col = self.max_x - self.min_x + 1

        # Print the results
        print("x range:", [self.min_x, self.max_x])
        print("y range:", [self.min_y, self.max_y])
        print("ROW AND COLUMN", (self.row, self.col))

        tilesize = game.tilemap.Get_Tile_Size()

        for y in range(self.min_y, self.max_y + 1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                tile_type = game.tilemap.Current_Tile((x * tilesize, y * tilesize))
                location = 1
                if tile_type == 'Floor':
                    location = 0
                row.append(location)
            self.map.append(row)

        # Print the map to debug
        for row in self.map:
            print(row)

        

    # Check if a cell is valid (within the grid)
    def is_valid(self, row, col):
        return (row >= 0) and (row < self.row) and (col >= 0) and (col < self.col)

    # Check if a cell is unblocked
    def is_unblocked(self, row, col):
        return self.map[row][col] == 0

    # Check if a cell is the destination
    def is_destination(self, row, col, dest):
        return row == dest[0] and col == dest[1]

    # Calculate the heuristic value of a cell (Euclidean distance to destination)
    def calculate_h_value(row, col, dest):
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

    # Trace the path from source to destination
    def trace_path(enemy, cell_details, dest):
        row = dest[0]
        col = dest[1]

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            enemy.path.append((row, col))
            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        enemy.path.append((row, col))
        # Reverse the path to get the path from source to destination
        enemy.path.reverse()

        # Print the path
        # for i in path:
        #     print("->", i, end=" ")
        # print()
        

    # Implement the A* search algorithm
    def a_star_search(self, enemy, src, dest):
        tilesize = enemy.game.tilemap.Get_Tile_Size()
        adjusted_x_src = int(src[0] // tilesize)
        adjusted_y_src = int(src[1] // tilesize)
        
        adjusted_x_dest = int(dest[0] // tilesize)
        adjusted_y_dest = int(dest[1] // tilesize)
        # print(self.is_valid(adjusted_x_src, adjusted_y_src))
        # print(self.row, self.col)
        # Check if the source and destination are valid
        if not self.is_valid(adjusted_x_src, adjusted_y_src) or not self.is_valid(adjusted_x_dest, adjusted_y_dest):
            return

        # Check if the source and destination are unblocked
        if not self.is_unblocked(adjusted_x_src, adjusted_y_src) or not self.is_unblocked(adjusted_x_dest, adjusted_y_dest):
            return
        

        # Check if we are already at the destination
        if self.is_destination(adjusted_x_src, adjusted_y_src, dest):
            return
        

        
        
        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(self.col)] for _ in range(self.row)]
        # Initialize the details of each cell
        cell_details = [[A_Star() for _ in range(self.col)] for _ in range(self.row)]

        # Initialize the start cell details
        i = adjusted_x_src
        j = adjusted_y_src
        cell_details[i][j].f = 0
        cell_details[i][j].g = 0
        cell_details[i][j].h = 0
        cell_details[i][j].parent_i = i
        cell_details[i][j].parent_j = j

        # Initialize the open list (cells to be visited) with the start cell
        open_list = []
        heapq.heappush(open_list, (0.0, i, j))

        # Initialize the flag for whether destination is found
        found_dest = False

        # Main loop of A* search algorithm
        while len(open_list) > 0:
            # Pop the cell with the smallest f value from the open list
            p = heapq.heappop(open_list)

            # Mark the cell as visited
            i = p[1]
            j = p[2]
            closed_list[i][j] = True
            # For each direction, check the successors
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]
                
                # If the successor is valid, unblocked, and not visited
                if self.is_valid(new_i, new_j) and self.is_unblocked(new_i, new_j) and not closed_list[new_i][new_j]:
                    # If the successor is the destination
                    # TODO Unable to verify the destination
                    if self.is_destination(new_i * tilesize, new_j * tilesize, dest):
                        print("TEST")
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        A_Star.trace_path(enemy, cell_details, dest)
                        found_dest = True

                        return
                    else:
                        # Calculate the new f, g, and h values
                        g_new = cell_details[i][j].g + 1.0
                        h_new = A_Star.calculate_h_value(new_i, new_j, dest)
                        f_new = g_new + h_new

                        # If the cell is not in the open list or the new f value is smaller
                        if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                            # Add the cell to the open list
                            heapq.heappush(open_list, (f_new, new_i, new_j))
                            # Update the cell details
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j



