class Light():
    def __init__(self, game, pos, light_level):
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.tiles = []
        self.Setup_Tile_Light()

        
    def Setup_Tile_Light(self):
        x_position = int(self.pos[0] // 16)
        y_position = int(self.pos[1] // 16)
        radius = int(self.light_level / 2)
        diameter = radius**2
        iteration = 0
        # Light on the tile the light source is located
        tile = self.game.tilemap.Current_Tile(self.pos)
        if tile:
            self.tiles.append(tile)
            tile['light'] = max(tile['light'], self.light_level)
            if 'Wall' in tile['type']:
                return
        else:
            return
            
         
        for y in range(y_position - radius, y_position + radius + 1):
            for x in range(x_position - radius, x_position + radius + 1):
                iteration += 1
                current_x_pos = x - x_position
                current_y_pos = y - y_position
                if current_x_pos**2 + current_y_pos**2 <= diameter:
                    tile = self.game.tilemap.Current_Tile((x * 16, y * 16))
                    if tile:
                        self.tiles.append(tile)
                        new_light_level = self.light_level - current_x_pos - current_y_pos
                        tile['light'] = max(tile['light'], new_light_level)
                        if 'Wall' in tile['type']:
                            break
    
    def Move_Light(self, pos):
        self.pos = pos
        if self.Delete_Light():
            self.Setup_Tile_Light()

    def Delete_Light(self):
        tile = self.game.tilemap.Current_Tile(self.pos)
        if not self.tiles:
            return False
        if tile['pos'] != self.tiles[0]['pos']:
            for tile in self.tiles:
                tile['light'] = 0
                self.tiles.remove(tile)
            return True

        return False

        
    

    

                
            

    def Update(self):
        pass