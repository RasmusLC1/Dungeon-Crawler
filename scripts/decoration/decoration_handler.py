from scripts.decoration.bones.bones import Bones
from scripts.decoration.chest.chest import Chest
from scripts.decoration.doors.door import Door
from scripts.decoration.shrine.shrine import Shrine
from scripts.decoration.boss_room.boss_room import Boss_Room
import random
import math


class Decoration_Handler():
    def __init__(self, game) -> None:
        self.game = game       
        self.decorations = []
        self.bones = []
        self.nearby_decoration_cooldown = 0
        self.saved_data = {}

    def Clear_Decorations(self):
        self.decorations.clear()
        self.saved_data.clear()


    # TODO: Implement Level depth for boss room, chest and Shrine
    def Initialise(self, depth = 0):
        # door initialisation
        for door in self.game.tilemap.extract([('Door_Basic', 0)].copy(), True):
            size = (self.game.assets[door.type][0].get_width(), self.game.assets[door.type][0].get_height())
            self.Spawn_Door(door.pos, size)

        for chest in self.game.tilemap.extract([('Chest', 0)]):
            version = self.Set_Chest_Version(depth)
            self.Spawn_Chest(chest.pos, version)

        for shrine in self.game.tilemap.extract([('Shrine', 0)]):
            self.Spawn_Shrine(shrine.pos)

        for bones in self.game.tilemap.extract([('Bones', 0)]):
            self.Spawn_Bones(bones.pos)

        for boss_room in self.game.tilemap.extract([('Boss_Room', 0)]):
            temp_level = 3
            radius = random.randint(5, 7)
            self.Spawn_Boss_Room(boss_room.pos, radius, temp_level)

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
        for ID, item_data in data.items():
            
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
                elif type == 'shrine':
                    decoration = self.Spawn_Shrine(pos)
                elif type == 'bones':
                    decoration = self.Spawn_Bones(pos)
                elif type == 'boss_room':
                    radius = item_data['radius']
                    level = item_data['level']
                    decoration = self.Spawn_Boss_Room(pos, radius, level)
                else:
                    print(type)
                decoration.Load_Data(item_data)
                self.decorations.append(decoration)

            except Exception as e:
                print("DATA WRONG DECORATION HANDLER", item_data, e)

    def Update(self):
        self.Check_Keyboard_Input()
        for decoration in self.decorations:
            decoration.Update()


    def Spawn_Door(self, pos, size):
        door = Door(self.game, 'door', pos, size)
        self.decorations.append(door)
        return door

    def Spawn_Chest(self, pos, version):
        chest = Chest(self.game, pos, version)  
        self.decorations.append(chest)
        return chest

    
    def Spawn_Shrine(self, pos):
        shrine = Shrine(self.game, pos)  
        self.decorations.append(shrine)
        return shrine
    
    def Spawn_Bones(self, pos):
        bones = Bones(self.game, pos, None)  
        self.decorations.append(bones)
        self.bones.append(bones)
        return bones
    
    def Spawn_Boss_Room(self, pos, radius, level):
        boss_room = Boss_Room(self.game, pos, radius, level)  
        self.decorations.append(boss_room)
        return boss_room

    def Check_Keyboard_Input(self):
        if self.game.keyboard_handler.e_pressed:
            if not self.Check_Decorations():
                return
            self.game.keyboard_handler.Set_E_Key(False)


    def Check_Decorations(self):
        # Check Shrine First since it's bigger
        if self.Nearby_Shrine():
            return True
        
        nearby_decorations = self.Find_Nearby_Decorations(self.game.player.pos, 2)
        if not nearby_decorations:
            return False
        
        self.Open_Decoration(nearby_decorations)
        return True

    def Find_Nearby_Decorations(self, player_pos, max_distance):
        

        nearby_decorations = []
        if max_distance <= 5:
            nearby_decorations = self.game.tilemap.Search_Nearby_Tiles(max_distance, player_pos, 'decoration')
            
        else:
            nearby_decorations = self.Find_Nearby_Decorations_Long_Distance(player_pos, max_distance)
        
        
        return nearby_decorations
    
    def Find_Nearby_Decorations_Long_Distance(self, player_pos, max_distance):
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
        
        if self.Nearby_Chest(decoration):
            return True
        
        if self.Nearby_Door(decoration):
            return True

        
        
        return False
    
    def Nearby_Chest(self, decoration):
        if decoration.type == 'chest':
            decoration.Open()
            if not decoration in self.decorations:
                return False
            
            self.decorations.remove(decoration)
            del(decoration)
            return True

    def Nearby_Door(self, decoration, key = True):
        if decoration.type == 'door':
            if key:
                if not self.Open_Door_With_Key(decoration):
                    return False
            else:
                decoration.Open()
            return True
        
        return False

    def Nearby_Shrine(self):
        nearby_decorations = self.Find_Nearby_Decorations(self.game.player.pos, 4)
        for decoration in nearby_decorations:
            if decoration.type == 'shrine':
                if not decoration.rect().colliderect(self.game.player.rect()):
                    continue
                decoration.Open()
                return True
            
        return False
    
    def Sort_Decorations(self, decorations):
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
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
    
    def Open_Door_Without_Key(self):
        decorations = self.Find_Nearby_Decorations(self.game.player.pos, 3)
        sorted_decorations = self.Sort_Decorations(decorations)
        for decoration in sorted_decorations:
            if decoration.type == 'door':
                return self.Nearby_Door(decoration, False)
        
        return False


    def Add_Decoration(self, decoration):
        if decoration in self.decorations:
            return
        self.decorations.append(decoration)

    def Remove_Decoration(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            self.game.tilemap.Remove_Entity_From_Tile(decoration.tile, decoration.ID)

    def Remove_Bones(self, bones):
        self.bones.remove(bones)
        return
