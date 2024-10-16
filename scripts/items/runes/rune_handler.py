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
        self.Initialise_Runes()
        self.Add_Runes_To_Inventory_TEST()

    def Initialise_Runes(self):
        self.Init_Healing_Rune()
        self.Init_Dash_Rune()
        self.Init_Fire_Resistance_Rune()
        self.Init_Key_Rune()
        
    def Rune_Spawner(self, name):
        if 'healing' in name:
            self.Init_Healing_Rune()
        elif 'dash' in name:
            self.Init_Dash_Rune()
        elif 'fire_resistance' in name:
            self.Init_Fire_Resistance_Rune()
        elif 'key' in name:
            self.Init_Key_Rune()


    def Init_Healing_Rune(self):
        healing_rune = Healing_Rune(self.game, (9999, 9999))
        self.Initiailise_Rune(healing_rune)
    
    def Init_Dash_Rune(self):
        dash_rune = Dash_Rune(self.game, (9999, 9999))
        self.Initiailise_Rune(dash_rune)

    def Init_Fire_Resistance_Rune(self):
        fire_resistance_rune = Fire_Resistance_Rune(self.game, (9999, 9999))
        self.Initiailise_Rune(fire_resistance_rune)

    def Init_Key_Rune(self):
        key_rune = Key_Rune(self.game, (9999, 9999))
        self.Initiailise_Rune(key_rune)

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