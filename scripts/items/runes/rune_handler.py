from scripts.items.runes.healing_rune import Healing_Rune
from scripts.items.runes.dash_rune import Dash_Rune
from scripts.items.runes.fire_resistance_rune import Fire_Resistance_Rune
from scripts.items.runes.freeze_resistance_rune import Freeze_Resistance_Rune
from scripts.items.runes.key_rune import Key_Rune
from scripts.items.runes.regen_rune import Regen_Rune
from scripts.items.runes.light_rune import Light_Rune

import math
import pygame

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = []
        self.active_runes = []
        self.saved_data = {}
        self.rune_types = ['healing_rune',
                    'dash_rune',
                    'fire_resistance_rune',
                    'key_rune',
                    'freeze_resistance_rune',
                    'regen_rune',
                    'light_rune'
                    ]              


    def Clear_Runes(self):
        self.runes.clear()
        self.active_runes.clear()
        self.saved_data.clear()


    def Initialise_Runes(self):
        for rune_type in self.rune_types:
            self.Rune_Spawner(rune_type)

        self.Add_Runes_To_Inventory_TEST()
        
        
    def Save_Rune_Data(self):
        for rune in self.runes:
            rune.Save_Data()
            self.saved_data[rune.type] = rune.saved_data

    def Load_Data(self, data):
        for ID, item_data in data.items():
            if not item_data:
                continue
            try:
                type = item_data['type']
                self.Rune_Spawner(type, item_data)
            except Exception as e:
                print("DATA WRONG RUNE HANDLER", item_data, e)


    def Update(self, offset = (0,0)):
        for rune in self.active_runes:
            rune.Update()
  

    def Rune_Spawner(self, name, data = None):
        rune = None
        if 'healing' in name:
            rune = self.Init_Healing_Rune()
        elif 'dash' in name:
            rune = self.Init_Dash_Rune()
        elif 'fire_resistance' in name:
            rune = self.Init_Fire_Resistance_Rune()
        elif 'freeze_resistance' in name:
            rune = self.Init_Freeze_Resistance_Rune()
        elif 'key' in name:
            rune = self.Init_Key_Rune()
        elif 'regen' in name:
            rune = self.Init_Regen_Rune()
        elif 'light_rune' in name:
            rune = self.Init_Light_Rune()
        if not rune:
            return False
        
        if data:
            rune.Load_Data(data)
            if rune.active:
                for active_rune in self.active_runes:
                    if rune.type == active_rune.type:
                        return
                self.active_runes.append(rune)
        self.Initiailise_Rune(rune)
        
        return True
        


    def Init_Healing_Rune(self):
        return Healing_Rune(self.game, (9999, 9999))
    
    def Init_Dash_Rune(self):
        return Dash_Rune(self.game, (9999, 9999))

    def Init_Fire_Resistance_Rune(self):
        return Fire_Resistance_Rune(self.game, (9999, 9999))

    def Init_Freeze_Resistance_Rune(self):
        return Freeze_Resistance_Rune(self.game, (9999, 9999))

    def Init_Key_Rune(self):
        return Key_Rune(self.game, (9999, 9999))

    def Init_Regen_Rune(self):
        return Regen_Rune(self.game, (9999, 9999))

    def Init_Light_Rune(self):
        return Light_Rune(self.game, (9999, 9999))

    def Initiailise_Rune(self, rune):
        if rune in self.runes:
            return
        self.runes.append(rune)
        self.game.item_handler.Add_Item(rune)
    

    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory('freeze_resistance_rune')
        self.Add_Rune_To_Rune_Inventory('key_rune')
        self.Add_Rune_To_Rune_Inventory('fire_resistance_rune')

    # Add runes to Active Inventory
    def Add_Rune_To_Rune_Inventory(self, rune_type):
        for rune in self.runes:
            if rune_type != rune.type:
                continue
            
            rune.active = True
            self.active_runes.append(rune)
            self.game.rune_inventory.Add_Item(rune)
            self.game.item_handler.Add_Item(rune)
            return

    def Remove_Rune_From_Inventory(self, rune_type):
        for rune in self.runes:
            if rune_type != rune.type:
                continue
            
            rune.active = False
            self.active_runes.remove(rune)
            self.game.rune_inventory.Remove_Item(rune, True)
            self.game.item_handler.Remove_Item(rune)

            return

    
    def Find_Nearby_Runes(self, entity_pos, max_distance):
        entity_pos = (entity_pos[0] - self.game.render_scroll[0], entity_pos[1] - self.game.render_scroll[1])
        nearby_runes = []
        for rune in self.active_runes:
            # Calculate the Euclidean distance
            distance = math.sqrt((entity_pos[0] - rune.pos[0]) ** 2 + (entity_pos[1] - rune.pos[1]) ** 2)
            if distance < max_distance:
                nearby_runes.append(rune)

        return nearby_runes


    def Render_Animation(self, surf, offset = (0, 0)):
        for rune in self.active_runes:
            rune.Render_Animation(surf, offset)