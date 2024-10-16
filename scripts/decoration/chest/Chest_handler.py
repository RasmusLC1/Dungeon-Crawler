from scripts.decoration.chest.chest import Chest
import math
import random

class Chest_Handler:
    def __init__(self, game) -> None:
        self.game = game
        self.chests = []
        self.saved_data = {}

    
    def Initialise(self, depth):
        for chest in self.game.tilemap.extract([('Chest', 0)]):
            version = self.Set_Chest_Version(depth)
            spawn_chest = self.Spawn_Chest(chest['pos'], version)
            self.chests.append(spawn_chest)



    def Set_Chest_Version(self, depth):
        i = 0
        while i < 9:
            version = i
            if random.randint(depth, max(depth + 5, 10)) < max(depth + 2, 5):
                break
            i += 1
        return version
    
    def Spawn_Chest(self, pos, version):
            return Chest(self.game, pos, version)  

    def Save_Item_Data(self):
        for chest in self.chests:
            chest.Save_Data()
            self.saved_data[chest.chest_ID] = chest.saved_data

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            if not item_data:
                continue
            try:
                version = item_data['version']
                pos = item_data['pos']
                chest = self.Spawn_Chest(pos, version)
                chest.Load_Data(item_data)
                self.chests.append(chest)

            except Exception as e:
                print("DATA WRONG", item_data, e)


    def Open_Chests(self, chests):
        if not chests:
            return False

        for chest in chests:
            chest.Open()
            self.chests.remove(chest)
            del(chest)
        
        return True

    def Find_Nearby_Chests(self, pos, max_distance):
        nearby_chests = []
        for chest in self.chests:  # Assuming self.traps is a list of traps
            # Calculate the Euclidean distance
            distance = math.sqrt((pos[0] - chest.pos[0]) ** 2 + (pos[1] - chest.pos[1]) ** 2)
            if distance < max_distance:
                nearby_chests.append(chest)
        return nearby_chests

    def Render(self, active_chests, surf, render_scroll = (0, 0)):
         for chest in active_chests:
            if not chest.text_cooldown:
                chest.Render(surf, render_scroll)
            else:
                chest.Render_text(surf, render_scroll)
