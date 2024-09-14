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
            self.x_offset = 0
            self.y_offset = 0
            self.positions = []
            self.map = []
            self.standard_map = []
            self.flying_map = []
            self.ignore_lava_map = []
            self.path = []

    def Setup_Map(self, game):
        self.Extract_Map_Data(game)
        self.Standard_Map(game)
        self.Ignore_Lava_Map(game)
        # self.Flying_Map(game)
    
    def Extract_Map_Data(self, game):
        # Extract all pos values
        self.positions = game.tilemap.Get_Pos()

        # Separate x and y coordinates
        x_coords = [pos[0] for pos in self.positions]
        y_coords = [pos[1] for pos in self.positions]

        # Find min and max for x and y coordinates
        self.min_x = min(x_coords)
        self.max_x = max(x_coords)
        self.min_y = min(y_coords)
        self.max_y = max(y_coords)

        # Calculate offsets based on the minimum values (assuming they might be negative)
        self.x_offset = -self.min_x if self.min_x < 0 else 0
        self.y_offset = -self.min_y if self.min_y < 0 else 0

        # Define the number of rows and columns based on max values and offsets
        self.row = self.max_y - self.min_y + 1
        self.col = self.max_x - self.min_x + 1

        # Initialize the map with '1's



    def Standard_Map(self, game):

        # Fill with 1 to start with, add 0 for valid tiles later
        self.standard_map = [[1] * self.row for _ in range(self.col)]
        # Fill the map based on JSON data
        for position in self.positions:
            x = position[0]
            y = position[1]
            map_x = x + self.x_offset
            map_y = y + self.y_offset

            # Check if the position is within the bounds of the map
            if 0 <= map_x < self.col and 0 <= map_y < self.row:
                tile_type = game.tilemap.Current_Tile_Type_Without_Offset((x, y))
                if not tile_type:
                    continue
                
                if tile_type == 'Floor' or 'ice_env' in tile_type or 'water_env' in tile_type:
                    self.standard_map[map_x][map_y] = 0

        # Print the map to debug
        # print("STANDARD MAP")
        # for row in self.standard_map:
        #     print(row)  

    def Ignore_Lava_Map(self, game):
        # Fill with 1 to start with, add 0 for valid tiles later
        self.ignore_lava_map = [[1] * self.row for _ in range(self.col)]
        # Fill the map based on JSON data
        for position in self.positions:
            x = position[0]
            y = position[1]
            map_x = x + self.x_offset
            map_y = y + self.y_offset

            # Check if the position is within the bounds of the map
            if 0 <= map_x < self.col and 0 <= map_y < self.row:
                tile_type = game.tilemap.Current_Tile_Type_Without_Offset((x, y))
                if not tile_type:
                    continue

                if tile_type == 'Floor' or 'Lava' in tile_type or 'Fire' in tile_type:
                    self.ignore_lava_map[map_x][map_y] = 0
        
        # print("LAVA MAP")
        # for row in self.ignore_lava_map:
        #     print(row)  



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
        # First check if row and col indices are within the valid range
        if col > self.max_x or col < self.min_x or row > self.max_y or row < self.min_y:
            return False

        return self.map[row][col] == 0

    # Check if a cell is the destination
    def is_destination(self, row, col, dest):
        return row == dest[0] and col == dest[1]

    # Calculate the heuristic value of a cell (Euclidean distance to destination)
    def calculate_h_value(self, row, col, dest):
        return math.sqrt((row - dest[0])**2 + (col - dest[1])**2)

    

    def trace_path(self, path, cell_details, dest):
        node = dest
        while cell_details[node[0]][node[1]].parent_i != node[0] or cell_details[node[0]][node[1]].parent_j != node[1]:
            path.append(node)
            node = (cell_details[node[0]][node[1]].parent_i, cell_details[node[0]][node[1]].parent_j)
        path.append(node)  # add the start point
        path.reverse()
        return path

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
            self.map = self.standard_map.copy()
            
        elif map == 'ignore_lava':
            self.map = self.ignore_lava_map
        
        else:
            self.map = self.standard_map

        # Check if the source and destination are valid
        if not A_Star.is_valid(self, src[0], src[1]) or not A_Star.is_valid(self, dest[0], dest[1]):
            return

        # Check if the source and destination are unblocked
        if not A_Star.is_unblocked(self, src[0], src[1]) or not A_Star.is_unblocked(self, dest[0], dest[1]):
            return

        # Check if we are already at the destination
        if A_Star.is_destination(self, src[0], src[1], dest):
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
                    if A_Star.is_destination(self, new_i, new_j, dest):
                        # Set the parent of the destination cell
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        self.trace_path(path, cell_details, dest)
                        self.Check_For_Walls(path)
                        return
                    else:
                        # Calculate the new f, g, and h values
                        # g_new = cell_details[i][j].g + 1.0
                        g_new = cell_details[i][j].g + (1.41 if dir in directions_diagonal else 1.0)
                        h_new = A_Star.calculate_h_value(self, new_i, new_j, dest)
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
                            if A_Star.is_destination(self, new_i, new_j, dest):
                                # Set the parent of the destination cell
                                cell_details[new_i][new_j].parent_i = i
                                cell_details[new_i][new_j].parent_j = j
                                self.trace_path(path, cell_details, dest)
                                return
                            else:
                                # Calculate the new f, g, and h values
                                # g_new = cell_details[i][j].g + 1.0
                                g_new = cell_details[i][j].g + (1.41 if dir in directions_diagonal else 1.0)
                                h_new = A_Star.calculate_h_value(self, new_i, new_j, dest)
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
            


