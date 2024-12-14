import math

class Light():
    _id_counter = 0  # Class variable to generate unique IDs

    def __init__(self, game, pos, light_level, tile) -> None:
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.pos_holder = pos
        self.tile = tile # Tile key where the light is located
        self.tiles = [] # Tiles illuminated by this light
        self.active = True
        self.number_rays = 60
        self.field_of_view = 360

        self.id = Light._id_counter
        Light._id_counter += 1  # Increment for the next light

        self.Compute_Angles()
        self.Setup_Tile_Light()

    def Compute_Angles(self):
        self.angle_cosines = [math.cos(math.radians(i * (self.field_of_view / self.number_rays))) * self.game.tilemap.tile_size for i in range(self.number_rays * self.light_level + 2)]
        self.angle_sines = [math.sin(math.radians(i * (self.field_of_view / self.number_rays))) * self.game.tilemap.tile_size for i in range(self.number_rays * self.light_level + 2)]

    def Check_Tile(self, tile):
        if not tile:
            return False
        if tile.physics:
            return False
        return True
    
    def Update_Light_Level(self, new_light_level):
        self.light_level = new_light_level
    
    def Setup_Tile_Light(self):
        # Setup the main tile under the light
        base_tile = self.game.tilemap.Current_Tile(self.tile)
        if not self.Check_Tile(base_tile):
            return

        # If current tile is dimmer than this light, add/update this light’s contribution
        if self.light_level > base_tile.light_level:
            base_tile.Add_Light_Contribution(self.id, self.light_level)
            self.tiles.append(base_tile)

        # Cast rays to illuminate surrounding tiles
        for j in range(self.number_rays):
            cos_angle = self.angle_cosines[j]
            sin_angle = self.angle_sines[j]
            for i in range(1, self.light_level + 1):
                pos_x = self.pos[0] + cos_angle * i
                pos_y = self.pos[1] + sin_angle * i
                tile_key = str(int(pos_x) // self.game.tilemap.tile_size) + ';' + str(int(pos_y) // self.game.tilemap.tile_size)
                
                tile = self.game.tilemap.Current_Tile(tile_key)
                if not self.Check_Tile(tile):
                    break

                new_light_level = max(0, self.light_level - i)
                # Add or update contribution if it's brighter than what’s currently recorded
                # Recalculate_Light_Level on the tile will determine if it needs updating
                if new_light_level > tile.light_level:
                    tile.Add_Light_Contribution(self.id, new_light_level)
                    self.tiles.append(tile)

    def Delete_Light(self):
        # Remove this light's contribution from all tiles it affected
        for tile in self.tiles:
            tile.Remove_Light_Contribution(self.id)
        self.tiles.clear()
        return True

    def Update_Position(self, pos):
        self.pos = pos

    def Move_Light(self, pos, tile_key):
        self.pos = pos
        self.tile = tile_key
        if not self.active:
            return
        if self.Delete_Light():
            self.Setup_Tile_Light()

    def Update(self):
        # If the light moves or changes, we can re-setup
        self.Delete_Light()
        self.Setup_Tile_Light()
