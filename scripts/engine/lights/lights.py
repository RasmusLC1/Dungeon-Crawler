import math

class Light():
    def __init__(self, game, pos, light_level):
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.tiles = []
        self.Setup_Tile_Light()

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

    def Setup_Tile_Light(self):
        num_lines = 80
        spread_angle = 360
        angle_increment = spread_angle / num_lines
        base_angle = 0

        tile = self.game.tilemap.Current_Tile(self.pos)
        if self.Check_Tile(tile):
            if self.light_level > tile['light']:
                tile['light'] = self.light_level
                self.tiles.append(tile)

        for j in range(num_lines):
            angle = base_angle + math.radians(j * angle_increment)
            for i in range(1, self.light_level + 1):
                pos_x = self.pos[0] + math.cos(angle) * 16 * i
                pos_y = self.pos[1] + math.sin(angle) * 16 * i

                tile = self.game.tilemap.Current_Tile((pos_x, pos_y))

                if not self.Check_Tile(tile):
                    break

                new_light_level = max(0, self.light_level - i)
                if new_light_level > tile['light']:
                    tile['light'] = new_light_level
                    self.tiles.append(tile)

    def Move_Light(self, pos):
        self.pos = pos
        if self.Delete_Light():
            self.Setup_Tile_Light()
        else:
            self.Setup_Under_entity_Light()

    def Delete_Light(self):
        if not self.tiles:
            return False
        for tile in self.tiles:
            tile['light'] = 0

        self.tiles.clear()
        return True

    def Update(self):
        pass
