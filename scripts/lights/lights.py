class Light():
    def __init__(self, game, pos, light_level):
        self.game = game
        self.light_level = light_level
        self.pos = pos
        self.Setup_Tile_Light()

        
    def Setup_Tile_Light(self):
        x_position = int(self.pos[0] // 16)
        y_position = int(self.pos[1] // 16)
        radius = int(self.light_level / 2)
        diameter = radius**2
        iteration = 0
        for y in range(y_position - radius, y_position + radius + 1):
            for x in range(x_position - radius, x_position + radius + 1):
                iteration += 1
                current_x_pos = x - x_position
                current_y_pos = y - y_position
                if current_x_pos**2 + current_y_pos**2 <= diameter:
                    tile = self.game.tilemap.Current_Tile((x * 16, y * 16))
                    if tile:
                        new_light_level = self.light_level - current_x_pos - current_y_pos
                        tile['light'] = max(tile['light'], new_light_level)
                        if 'Wall' in tile['type']:
                            break

    

                
            

    def Update(self):
        pass