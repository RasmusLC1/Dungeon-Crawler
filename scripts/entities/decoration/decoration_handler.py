from scripts.entities.decoration.bones.bones import Bones
from scripts.entities.decoration.chest.chest import Chest
from scripts.entities.decoration.doors.door import Door
from scripts.entities.decoration.shrine.rune_shrine import Rune_Shrine
from scripts.entities.decoration.shrine.portal_shrine import Portal_Shrine
from scripts.entities.decoration.boss_room.boss_room import Boss_Room
import random
import math

class Decoration_Handler():
    def __init__(self, game) -> None:
        self.game = game       
        self.decorations = []
        self.bones = []
        self.nearby_decoration_cooldown = 0
        self.saved_data = {}

        self.spawn_methods = {
            'door': self.Spawn_Door,
            'chest': self.Spawn_Chest,
            'rune_shrine': self.Spawn_Rune_Shrine,
            'portal_shrine': self.Spawn_Portal_Shrine,
            'bones': self.Spawn_Bones,
            'boss_room': self.Spawn_Boss_Room
        }

        self.opening_methods = {
            'chest': self.Open_Chest,
            'rune_shrine': self.Open_Shrine,
            'portal_shrine': self.Open_Shrine,
        }



    def Clear_Decorations(self):
        self.decorations.clear()
        self.saved_data.clear()

    def Initialise(self, depth=0):
        # door initialisation
        for door in self.game.tilemap.extract([('door_basic', 0)].copy(), True):
            size = (self.game.assets[door.type][0].get_width(), self.game.assets[door.type][0].get_height())
            self.Decoration_Spawner('door', door.pos, size=size)

        for chest in self.game.tilemap.extract([('chest', 0)]):
            version = self.Set_Chest_Version(depth)
            self.Decoration_Spawner('chest', chest.pos, version=version)

        for shrine in self.game.tilemap.extract([('rune_shrine', 0)]):
            self.Decoration_Spawner('rune_shrine', shrine.pos)

        for shrine in self.game.tilemap.extract([('portal_shrine', 0)]):
            self.Decoration_Spawner('portal_shrine', shrine.pos)

        for bones in self.game.tilemap.extract([('Bones', 0)]):
            self.Decoration_Spawner('bones', bones.pos)

        for boss_room in self.game.tilemap.extract([('Boss_Room', 0)]):
            temp_level = 3
            radius = random.randint(5, 7)
            self.Decoration_Spawner('boss_room', boss_room.pos, radius=radius, level=temp_level)

        for weapon in self.game.tilemap.extract([('Weapon', 0)]):
            self.game.item_handler.weapon_handler.Spawn_Random_Weapon(weapon.pos)

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
                size = item_data.get('size')
                version = item_data.get('version')
                radius = item_data.get('radius')
                level = item_data.get('level')
                self.Decoration_Spawner(type, pos, size=size, version=version, radius=radius, level=level, data=item_data)
            except Exception as e:
                print("DATA WRONG DECORATION HANDLER", item_data, e)

    def Decoration_Spawner(self, type, pos, size=None, version=None, radius=None, level=None, data=None):
        spawn_function = self.spawn_methods.get(type)
        if not spawn_function:
            print(f"Warning: Decoration type '{type}' not recognized. Decoration_Handler Decoration_Spawner")
            return None

        decoration = spawn_function(pos, size, version, radius, level)
        if decoration:
            if data:
                decoration.Load_Data(data)
        return decoration

    def Spawn_Door(self, pos, size, version=None, radius=None, level=None):
        door = Door(self.game, 'door_basic', pos, size)
        self.decorations.append(door)
        return door

    def Spawn_Chest(self, pos, size=None, version=None, radius=None, level=None):
        chest = Chest(self.game, pos, version)  
        self.decorations.append(chest)
        return chest

    def Spawn_Rune_Shrine(self, pos, size=None, version=None, radius=None, level=None):
        shrine = Rune_Shrine(self.game, pos)
        self.decorations.append(shrine)
        return shrine
    
    def Spawn_Portal_Shrine(self, pos, size=None, version=None, radius=None, level=None):
        shrine = Portal_Shrine(self.game, pos)
        self.decorations.append(shrine)
        return shrine

    def Spawn_Bones(self, pos, size=None, version=None, radius=None, level=None):
        bones = Bones(self.game, pos, None)  
        self.bones.append(bones)
        return bones

    def Spawn_Boss_Room(self, pos, size=None, version=None, radius=None, level=None):
        boss_room = Boss_Room(self.game, pos, radius, level)
        self.decorations.append(boss_room)
        return boss_room

    def Update(self):
        self.Check_Keyboard_Input()
        for decoration in self.decorations:
            decoration.Update()

    def Check_Keyboard_Input(self):
        if self.game.keyboard_handler.e_pressed:
            if not self.Check_Decorations():
                return
            self.game.keyboard_handler.Set_E_Key(False)

    def Check_Decorations(self):
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
            distance = math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2)
            if distance < max_distance:
                nearby_decorations.append(decoration)
        return nearby_decorations

    def Open_Decoration(self, decorations):      
        for decoration in decorations:
            if decoration.type == 'bones':
                decorations.remove(decoration)
        if not decorations:
            return False
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
        decoration = decorations[0]
        decoration_opener = self.opening_methods.get(decoration.type)
        if not decoration_opener:
            return
        decoration_opener(decoration)

    def Open_Chest(self, decoration):
        decoration.Open()

    def Open_Door(self, decoration, key=True):
        if key:
            if not self.Open_Door_With_Key(decoration):
                return
        else:
            decoration.Open()
            

    def Open_Shrine(self, decoration):
        decoration.Open()

    def Sort_Decorations(self, decorations):
        player_pos = self.game.player.pos
        decorations.sort(key=lambda decoration: math.sqrt((player_pos[0] - decoration.pos[0]) ** 2 + (player_pos[1] - decoration.pos[1]) ** 2))
        return decorations


    def Add_Decoration(self, decoration):
        if decoration in self.decorations:
            return
        self.decorations.append(decoration)

    def Remove_Decoration(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            self.game.item_handler.Remove_Item(decoration)
            self.game.tilemap.Remove_Entity_From_Tile(decoration.tile, decoration.ID)

    def Remove_Bones(self, bones):
        self.bones.remove(bones)
        return