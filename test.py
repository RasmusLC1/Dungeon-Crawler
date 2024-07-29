class Light():
    def __init__(self, game, pos, light_level):
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.tiles = []
        self.Setup_Tile_Light()

    # Light on the tile the light source is located
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

    # Use raycaster instead to prevent wall conflicts
    def Setup_Tile_Light(self):
        self.Setup_Under_entity_Light()
        x_position = int(self.pos[0] // 16)
        y_position = int(self.pos[1] // 16)
        radius = int(self.light_level // 2)
        radius_squared = radius**2
        
        for y in range(y_position - radius, y_position + radius + 1):
            for x in range(x_position - radius, x_position + radius + 1):
                current_x_pos = x - x_position
                current_y_pos = y - y_position
                distance_squared = current_x_pos**2 + current_y_pos**2
                if distance_squared <= radius_squared:
                    tile = self.game.tilemap.Current_Tile((x * 16, y * 16))
                    if tile:
                        new_light_level = self.light_level - int((distance_squared**0.5))
                        if new_light_level > tile['light']:                            
                            tile['light'] = new_light_level
                            self.tiles.append(tile)
                        if 'Wall' in tile['type']:
                            break

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