
# TODO: Implement Hashing so that entities registrer with a tile when they move onto it
# Use dictionary keyed to pos in tilemap
class Offgrid_Tile():
    def __init__(self, game, type, variant, pos, size, active, light_level) -> None:
        self.game = game
        self.type = type
        self.variant = variant
        self.pos = pos
        self.size = size
        self.active = active
        self.light_level = light_level
        self.entities = []

    def Print_Type(self):
        print('type: ', self.pos)

    