
# TODO: Implement Hashing so that entities registrer with a tile when they move onto it
# Use dictionary keyed to pos in tilemap
class Tile():
    def __init__(self, game, type, variant, pos, active, light_level) -> None:
        self.game = game
        self.type = type
        self.variant = variant
        self.pos = pos
        self.size = (16, 16)
        self.active = active
        self.light_level = light_level
        self.entities = []