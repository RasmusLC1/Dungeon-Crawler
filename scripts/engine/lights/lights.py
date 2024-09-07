import math

class Light():
    def __init__(self, game, pos, light_level) -> None:
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.pos_holder = pos
        self.tiles = []
        self.picked_up = False
        self.active = True
        self.number_rays = 80
        self.field_of_view = 360
        self.Compute_Angles()
        self.Setup_Tile_Light()

    # Precompute all the cos and sin angles
    def Compute_Angles(self):
        self.angle_cosines = [math.cos(math.radians(i * (self.field_of_view / self.number_rays))) for i in range(100)]
        self.angle_sines = [math.sin(math.radians(i * (self.field_of_view / self.number_rays))) for i in range(100)]

    def Setup_Tile_Light(self):

        # Setup light_level under the light itself
        tile = self.game.tilemap.Current_Tile(self.pos)
        if self.Check_Tile(tile):
            if self.light_level > tile['light']:
                self.game.tilemap.Set_Light_Level(tile, self.light_level)
                self.tiles.append(tile)

        for j in range(self.number_rays):
            cos_angle = self.angle_cosines[j] * 16
            sin_angle = self.angle_sines[j] * 16
            for i in range(1, self.light_level + 1):
                pos_x = self.pos[0] + cos_angle * i
                pos_y = self.pos[1] + sin_angle * i

                tile = self.game.tilemap.Current_Tile((pos_x, pos_y))

                if not self.Check_Tile(tile):
                    break

                new_light_level = max(0, self.light_level - i)
                if new_light_level > tile['light']:
                    self.game.tilemap.Set_Light_Level(tile, new_light_level)
                self.tiles.append(tile)

    def Setup_Under_entity_Light(self):
        tile = self.game.tilemap.Current_Tile(self.pos)
        if tile:
            if self.light_level > tile['light']:
                tile['light'] = self.light_level
                self.tiles.append(tile)
            if 'Wall' in tile['type']:
                return
        else:
            return

    def Check_Tile(self, tile):
        if not tile:
            return False
        if 'Wall' in tile['type']:
            return False
        return True
    
    def Update_Position(self, pos):
        self.pos = pos


    def Move_Light(self, pos):
        self.pos = pos
        if not self.active:
            return
        if self.Delete_Light():
            self.Setup_Tile_Light()
        else:
            self.Setup_Under_entity_Light()

    def Delete_Light(self):
        # If the light has no tiles to update, we don't need to delete
        if not self.tiles: 
            return False
        for tile in self.tiles:
            tile['light'] = 0
        self.tiles.clear()

        return True

    def Update(self):
        self.tiles.clear()
        self.Setup_Tile_Light()