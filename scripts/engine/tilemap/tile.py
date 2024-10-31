
# TODO: Implement Hashing so that entities registrer with a tile when they move onto it
# Use dictionary keyed to pos in tilemap
class Tile():
    def __init__(self, game, type, variant, pos, size, active, light_level, physics) -> None:
        self.game = game
        self.type = type
        self.variant = variant
        self.pos = pos
        self.size = size
        self.active = active
        self.light_level = light_level
        self.physics = physics
        self.entities = []

    def Print_Type(self):
        print('type: ', self.pos)

    def Set_Type(self, new_type):
        self.type = new_type

    def Update(self):
        self.Clear_Entities()

    def Set_Light_Level(self, new_light_level):
        self.light_level = new_light_level

    def Add_Entity(self, entity):
        if entity in self.entities:
            return
        
        self.entities.append(entity)

    def Clear_Entity(self, entity_ID):
        if entity_ID not in self.entities:
            return
        for entity in self.entities:
            if entity.ID == entity_ID:
                self.entities.remove(entity)
                return
            
        return