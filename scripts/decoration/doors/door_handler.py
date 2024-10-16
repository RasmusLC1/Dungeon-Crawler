
import math
from scripts.decoration.doors.door import Door



class Door_Handler:
    def __init__(self, game):
        self.game = game       
        self.doors = []
        self.nearby_doors_cooldown = 0
        self.saved_data = {}

    def Initialise(self):
        # door initialisation
        for door in self.game.tilemap.extract([('DoorClosed', 0)].copy(), True):
            size = (self.game.assets[door['type']][0].get_width(), self.game.assets[door['type']][0].get_height())
            door = self.Spawn_Door(door['type'], door['pos'], size)
            self.doors.append(door)
            
    
    def Save_Door_Data(self):
        for door in self.doors:
            door.Save_Data()
            self.saved_data[door.ID] = door.saved_data

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            
            if not item_data:
                continue
            try:
                type = item_data['type']
                pos = item_data['pos']
                size = item_data['size']
                door = self.Spawn_Door(type, pos, size)
                door.Load_Data(item_data)
                self.doors.append(door)

            except Exception as e:
                pass
                print("DATA WRONG", item_data, e)

        for door in self.doors:
            if not door.is_open:
                continue
            door.Open(False)

    def Spawn_Door(self, type, pos, size):
        return Door(self.game, type, pos, size)


    def Find_Nearby_Doors(self, player_pos, max_distance):
        
        nearby_doors = []
        for door in self.doors:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - door.pos[0]) ** 2 + (player_pos[1] - door.pos[1]) ** 2)
            if distance < max_distance:
                nearby_doors.append(door)
        return nearby_doors
    
    def Open_Doors(self, doors):
        if not doors:
            return False
        for door in doors:
            door.Open()
            # self.doors.remove(door)
            # del(door)
        
        return True



    def Remove_Door(self, door):
        # TODO: Create raycaster function to detect door
        # self.game.ray_caster.Remove_Trap(door)
        if door in self.doors:
            self.doors.remove(door)
        del(door)

    def Add_Door(self, door):
        self.doors.append(door)
