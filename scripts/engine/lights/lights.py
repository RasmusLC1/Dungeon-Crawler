import math

class Light():
    def __init__(self, game, pos, light_level, tile) -> None:
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.pos_holder = pos
        self.tile = tile # Tile light source is on
        self.tiles = [] # sorrounding tiles
        self.picked_up = True
        self.active = True
        self.number_rays = 60
        self.field_of_view = 360
        self.Compute_Angles()
        self.Setup_Tile_Light()

    # Precompute all the cos and sin angles
    def Compute_Angles(self):
        self.angle_cosines = [math.cos(math.radians(i * (self.field_of_view / self.number_rays))) * self.game.tilemap.tile_size for i in range(self.number_rays * self.light_level + 2)]
        self.angle_sines = [math.sin(math.radians(i * (self.field_of_view / self.number_rays))) * self.game.tilemap.tile_size for i in range(self.number_rays * self.light_level + 2)]

    def Update_Light_Level(self, new_light_level):
        self.light_level = new_light_level

    def Setup_Tile_Light(self):
        # Setup light_level under the light itself
        tile = self.game.tilemap.Current_Tile(self.tile)
        # If there is no tile present, then simply return
        if not self.Check_Tile(tile):
            return
        
         # If the current tile is brigther than the lightsource, then just return as nothing can be updated
        if self.light_level < tile.light_level:
            return 
        
        self.game.tilemap.Set_Light_Level(tile, self.light_level)
        self.tiles.append(tile)

        for j in range(self.number_rays):
            # Compute the precalculated angles on the new points
            cos_angle = self.angle_cosines[j]
            sin_angle = self.angle_sines[j]
            for i in range(1, self.light_level + 1):
                pos_x = self.pos[0] + cos_angle * i
                pos_y = self.pos[1] + sin_angle * i
                tile_key = str(int(pos_x) // self.game.tilemap.tile_size) + ';' + str(int(pos_y) // self.game.tilemap.tile_size)
                try:
                    tile = self.game.tilemap.Current_Tile(tile_key)
                except Exception as e:
                    print("DATA WRONG, LIGHT HANDLER", (pos_x, pos_y), self.tile, e)

                if not self.Check_Tile(tile):
                    break
                new_light_level = max(0, self.light_level - i)
                # Add the tile if it's darker than the current tile
                if new_light_level > tile.light_level:
                    self.game.tilemap.Set_Light_Level(tile, new_light_level)
                    self.tiles.append(tile)


                

    def Setup_Under_entity_Light(self):
        tile = self.game.tilemap.Current_Tile(self.tile)
        if tile:
            if self.light_level > tile.light_level:
                tile.light_level= self.light_level
                self.tiles.append(tile)
            if tile.physics:
                return
        else:
            return

    def Check_Tile(self, tile):
        if not tile:
            return False

        if tile.physics:
            return False
        
        return True
    
    def Update_Position(self, pos):
        self.pos = pos


    def Move_Light(self, pos, tile):
        self.pos = pos
        self.tile = tile
        if not self.active:
            return
        if self.Delete_Light():
            self.Setup_Tile_Light()
        else:
            self.Setup_Under_entity_Light()

    def Delete_Light(self):
        for tile in self.tiles:
            tile.light_level = 0
            tile.active = 0

        self.tiles.clear()
        return True

    def Update(self):
        self.tiles.clear()
        self.Setup_Tile_Light()