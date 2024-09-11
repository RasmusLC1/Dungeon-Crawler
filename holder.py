import json
import pygame
import numpy as np
import math
import heapq


class A_Star:
    def __init__(self) -> None:
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
            self.standard_map = []
            self.flying_map = []
            self.ignore_lava_map = []
            self.path = []

    def Setup_Map(self, game):
        self.Extract_Map_Data(game)
        self.Standard_Map(game)
        self.Ignore_Lava_Map(game)
        self.Flying_Map(game)
    
    def Extract_Map_Data(self, game):
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

        # # Print the results
        # print("x range:", [self.min_x, self.max_x])
        # print("y range:", [self.min_y, self.max_y])
        # print("ROW AND COLUMN", (self.row, self.col))

    def Standard_Map(self, game):
        self.standard_map.clear()

        for y in range(self.min_y, self.max_y + 1):
            row = []
            tilesize = game.tilemap.Get_Tile_Size()
            for x in range(self.min_x, self.max_x + 1):
                tile_type = game.tilemap.Current_Tile_Type((x * tilesize, y * tilesize))
                # tile_type = game.tilemap.Current_Tile_Type_Without_Offset((x, y))
                location = 1
                if tile_type == 'Floor':
                    location = 0
                row.append(location)
            self.standard_map.append(row)

        # Print the map to debug
        print("STANDARD MAP")
        for row in self.standard_map:
            print(row)  

    def Ignore_Lava_Map(self, game):
        self.ignore_lava_map.clear()

        for y in range(self.min_y, self.max_y + 1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                tile_type = game.tilemap.Current_Tile_Type_Without_Offset((x, y))
                location = 1
                if tile_type == 'Floor' or tile_type == 'Lava_env':
                    location = 0
                print(tile_type, location)
                row.append(location)
            self.ignore_lava_map.append(row)
        print("LAVA MAP")
        # Print the map to debug
        for row in self.ignore_lava_map:
            print(row)  


    def Flying_Map(self, game):
        self.flying_map.clear()
        for y in range(self.min_y, self.max_y + 1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                tile_type = game.tilemap.Current_Tile_Type_Without_Offset((x, y))
                location = 0
                
                if not tile_type:
                    location = 1
                    row.append(location)
                    continue

                
                if 'Wall' in tile_type:
                    location = 1

                row.append(location)
                
            self.flying_map.append(row)

        # Print the map to debug
        # for row in self.standard_map:
        #     print(row)  

    # Check if a cell is valid (within the grid)
    def is_valid(self, row, col):
        
        return (row >= 0) and (row < self.row) and (col >= 0) and (col < self.col)

    # Check if a cell is unblocked
    def is_unblocked(self, row, col):
        return self.map[row][col] == 0

    # Check if a cell is the destination
    def is_destination(row, col, dest):
        return row == dest[0] and col == dest[1]

    # Calculate the heuristic value of a cell (Euclidean distance to destination)
    def calculate_h_value(row, col, dest):
        return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

    # Trace the path from source to destination
    def trace_path(self, path, cell_details, dest):
        self.path.clear()
        row = dest[0]
        col = dest[1]

        # Trace the path from destination to source using parent cells
        while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
            # enemy.path.append((row, col))
            self.path.append((row, col))

            temp_row = cell_details[row][col].parent_i
            temp_col = cell_details[row][col].parent_j
            row = temp_row
            col = temp_col

        # Add the source cell to the path
        self.path.append((row, col))
        # Reverse the path to get the path from source to destination
        self.path.reverse()

        # Print the path
        # for i in path:
        #     print("->", i, end=" ")
        # print()

    def Check_For_Walls(self, path):
        if not self.path:
            return
        for point in self.path:
            row = point[1]
            col = point[0]
            if self.map[point[0]][point[1] + 1] == 1 and not self.map[point[0]][point[1] - 1] == 1:
                row = point[1] - 1
            elif self.map[point[0]][point[1] - 1] == 1 and not self.map[point[0]][point[1] + 1] == 1:
                row = point[1] + 1

            if self.map[point[0] + 1][point[1]] == 1 and not self.map[point[0] - 1][point[1]] == 1:
                col = point[0] - 1
            elif self.map[point[0] - 1][point[1]] == 1 and not self.map[point[0] + 1][point[1]] == 1:
                col = point[0] + 1

            path.append((col, row))
        return
    

    # Implement the A* search algorithm
    def a_star_search(self, path, src, dest, map = 'standard'):
        if map == 'standard':
            self.map = self.standard_map
        elif map == 'ignore_lava':
            print("LAVA MAP")
            self.map = self.ignore_lava_map
        
        else:
            self.map = self.standard_map
            print("MAP MISSING")

        # Check if the source and destination are valid
        if not A_Star.is_valid(self, src[0], src[1]) or not A_Star.is_valid(self, dest[0], dest[1]):
            return

        # Check if the source and destination are unblocked
        if not A_Star.is_unblocked(self, src[0], src[1]) or not A_Star.is_unblocked(self, dest[0], dest[1]):
            return

        # Check if we are already at the destination
        if A_Star.is_destination(src[0], src[1], dest):
            return
        
        # Initialize the closed list (visited cells)
        closed_list = [[False for _ in range(self.col)] for _ in range(self.row)]
        # Initialize the details of each cell
        cell_details = [[A_Star() for _ in range(self.col)] for _ in range(self.row)]

        # Initialize the start cell details
        i = src[0]
        j = src[1]
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
            directions_straight = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            directions_diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            wall_hit = False


            for dir in directions_straight:
                new_i = i + dir[0]
                new_j = j + dir[1]

                if not A_Star.is_unblocked(self, new_i, new_j):
                    wall_hit = True

                # If the successor is valid, unblocked, and not visited
                if A_Star.is_valid(self, new_i, new_j) and A_Star.is_unblocked(self, new_i, new_j) and not closed_list[new_i][new_j]:
                    # If the successor is the destination
                    if A_Star.is_destination(new_i, new_j, dest):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        self.trace_path(path, cell_details, dest)
                        self.Check_For_Walls(path)
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
                    

                if not wall_hit:
                    for dir in directions_diagonal:
                        new_i = i + dir[0]
                        new_j = j + dir[1]

                        # If the successor is valid, unblocked, and not visited
                        if A_Star.is_valid(self, new_i, new_j) and A_Star.is_unblocked(self, new_i, new_j) and not closed_list[new_i][new_j]:
                            # If the successor is the destination
                            if A_Star.is_destination(new_i, new_j, dest):
                                # Set the parent of the destination cell
                                cell_details[new_i][new_j].parent_i = i
                                cell_details[new_i][new_j].parent_j = j
                                self.trace_path(path, cell_details, dest)
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
            


