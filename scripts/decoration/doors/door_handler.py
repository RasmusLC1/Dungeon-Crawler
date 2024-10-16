
import math
from scripts.decoration.doors.door import Door



class Door_Handler:
    def __init__(self, game):
        self.doors = []
        self.nearby_doors_cooldown = 0
        self.game = game

        
        

    def Initialise(self):
        # door initialisation
        for door in self.game.tilemap.extract([('DoorClosed', 0)].copy(), True):
            self.doors.append(Door(self.game, door['type'], door['pos'], (self.game.assets[door['type']][0].get_width(), self.game.assets[door['type']][0].get_height())))


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
        print(doors)
        for door in doors:
            door.Open()
            self.doors.remove(door)
            del(door)
        
        return True



    def Remove_Door(self, door):
        # TODO: Create raycaster function to detect door
        # self.game.ray_caster.Remove_Trap(door)
        if door in self.doors:
            self.doors.remove(door)
        del(door)

    def Add_Door(self, door):
        self.doors.append(door)
