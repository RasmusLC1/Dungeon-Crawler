import pygame
from scripts.entities.entities import PhysicsEntity
from scripts.decoration.chest.chest import Chest
from scripts.decoration.doors.door import Door
import random
import math


class Decoration_Handler():
    def __init__(self, game) -> None:
        self.game = game       
        self.decorations = []
        self.nearby_decoration_cooldown = 0
        self.saved_data = {}

    def Clear_Decorations(self):
        self.decorations.clear()
        self.saved_data.clear()


    def Initialise(self, depth = 0):
        # door initialisation
        for door in self.game.tilemap.extract([('DoorClosed', 0)].copy(), True):
            size = (self.game.assets[door['type']][0].get_width(), self.game.assets[door['type']][0].get_height())
            door = self.Spawn_Door(door['pos'], size)
            self.decorations.append(door)

        for chest in self.game.tilemap.extract([('Chest', 0)]):
            version = self.Set_Chest_Version(depth)
            spawn_chest = self.Spawn_Chest(chest['pos'], version)
            self.decorations.append(spawn_chest)

    def Set_Chest_Version(self, depth):
        i = 0
        while i < 9:
            version = i
            if random.randint(depth, max(depth + 5, 10)) < max(depth + 2, 5):
                break
            i += 1
        return version  
        

    def Save_Decoration_Data(self):
        for decoration in self.decorations:
            decoration.Save_Data()
            self.saved_data[decoration.ID] = decoration.saved_data

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            
            if not item_data:
                continue
            try:
                type = item_data['type']
                pos = item_data['pos']
                size = item_data['size']
                decoration = None
                if type == 'door':
                    decoration = self.Spawn_Door(pos, size)
                elif type == 'chest':
                    version = item_data['version']
                    decoration = self.Spawn_Chest(pos, version)
                decoration.Load_Data(item_data)
                self.decorations.append(decoration)

            except Exception as e:
                pass
                print("DATA WRONG", item_data, e)

    def Update(self):
        self.Check_Keyboard_Input()


    def Spawn_Door(self, pos, size):
        return Door(self.game, 'door', pos, size)
    
    def Spawn_Chest(self, pos, version):
        return Chest(self.game, pos, version)  
    
    def Check_Keyboard_Input(self):
        if self.game.keyboard_handler.e_pressed:

            if not self.Check_Decorations():
                return
            self.game.keyboard_handler.Set_E_Key(False)


    def Check_Decorations(self):      
        nearby_decorations = self.Find_Nearby_Decorations(self.game.player.pos, 20)
        if not nearby_decorations:
            return False
        
        self.Open_Decoration(nearby_decorations)
        return True

    def Find_Nearby_Decorations(self, player_pos, max_distance):
        
        nearby_decorations = []
        for decoration in self.decorations:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
            if distance < max_distance:
                nearby_decorations.append(decoration)
        
        return nearby_decorations
    
    def Open_Decoration(self, decorations):
        if not decorations:
            return False
        
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
        decoration = decorations[0]
        if decoration.type == 'chest':
            decoration.Open()
        elif decoration.type == 'door':
            if not self.Open_Door_With_Key(decoration):
                return False
        else:
            return False
        
        self.decorations.remove(decoration)
        del(decoration)
        
        return True
    
    def Sort_Decorations(self, decorations):
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
        print(decorations[0])
        return decorations


    def Open_Door_With_Key(self, door):
        key_found = False
        for inventory_slot in self.game.item_inventory.inventory:
                if not inventory_slot.item:
                    continue
                
                if inventory_slot.item.type == 'key':
                    inventory_slot.Remove_Item()
                    key_found = True
                    break

        if not key_found:
            return False
            
        door.Open()
        return True
    
    def Open_Door_Without_Key(self, decorations):
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))

        for decoration in self.decorations:
            if decoration.type != 'door':
                continue

            decoration.Open()
            self.decorations.remove(decoration)
            del(decoration)
            return True
        
        return False

    def Add_Decoration(self, decoration):
        if decoration in self.decorations:
            return
        self.decorations.append(decoration)

    def Remove_Decoration(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
        del(decoration)