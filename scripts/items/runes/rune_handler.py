from scripts.items.runes.healing_rune import Healing_Rune
from scripts.items.runes.dash_rune import Dash_Rune
from scripts.items.runes.fire_resistance_rune import Fire_Resistance_Rune
from scripts.items.runes.key_rune import Key_Rune

import pygame

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = {}
        self.active_runes = []
        self.saved_data = {}
        self.rune_types = ['healing_rune',
                    'dash_rune',
                    'fire_resistance_rune',
                    'key_rune',
                    ]              



    def Initialise_Runes(self):
        for rune_type in self.rune_types:
            self.Rune_Spawner(rune_type)

        self.Add_Runes_To_Inventory_TEST()
        
        
    def Save_Item_Data(self):
        for rune in self.runes:
            rune.Save_Data()
            self.saved_data[rune.type] = rune.saved_data

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            if not item_data:
                continue
            try:
                type = item_data['type']
                self.Rune_Spawner(type, item_data)
            except Exception as e:
                print("DATA WRONG", item_data, e)

        # TODO: IMPLEMENT PROPER METHOD
        # self.Add_Runes_To_Inventory_TEST()
        

    def Rune_Spawner(self, name, data = None):
        rune = None
        if 'healing' in name:
            rune = self.Init_Healing_Rune()
        elif 'dash' in name:
            rune = self.Init_Dash_Rune()
        elif 'fire_resistance' in name:
            rune = self.Init_Fire_Resistance_Rune()
        elif 'key' in name:
            rune = self.Init_Key_Rune()

        if not rune:
            return False
        
        if data:
            rune.Load_Data(data)
        self.Initiailise_Rune(rune)
        
        return True
        


    def Init_Healing_Rune(self):
        return Healing_Rune(self.game, (9999, 9999))
    
    def Init_Dash_Rune(self):
        return Dash_Rune(self.game, (9999, 9999))

    def Init_Fire_Resistance_Rune(self):
        return Fire_Resistance_Rune(self.game, (9999, 9999))

    def Init_Key_Rune(self):
        return Key_Rune(self.game, (9999, 9999))

    def Initiailise_Rune(self, rune):
        self.Add_Rune_To_Dict(rune)
        self.game.item_handler.Add_Item(rune)
    
    def Add_Rune_To_Dict(self, rune):
        type = rune.type
        if type not in self.runes:
            self.runes[type] = []
        self.runes[type].append(rune)
    
    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory('key_rune')
        self.Add_Rune_To_Rune_Inventory('dash_rune')
        self.Add_Rune_To_Rune_Inventory('fire_resistance_rune')

    def Add_Rune_To_Rune_Inventory(self, rune_type):
        if rune_type not in self.runes:
            return False
        rune = self.runes[rune_type][0]
        rune.active = True
        self.active_runes.append(rune)
        self.game.rune_inventory.Add_Item(rune)


    def Update(self, offset = (0,0)):
        for rune in self.active_runes:
            rune.Update()


    def Render_Animation(self, surf, offset = (0, 0)):
        for rune in self.active_runes:
            rune.Render_Animation(surf, offset)