from scripts.items.runes.healing_rune import Healing_Rune
from scripts.items.runes.dash_rune import Dash_Rune
from scripts.items.runes.fire_resistance_rune import Fire_Resistance_Rune

import pygame

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = {}
        self.active_runes = []
        self.Initialise_Runes()
        self.Add_Runes_To_Inventory_TEST()

    def Initialise_Runes(self):
        healing_rune = Healing_Rune(self.game, (9999, 9999))
        self.Add_Rune_To_Dict(healing_rune)
        self.game.item_handler.Add_Item(healing_rune)


        dash_rune = Dash_Rune(self.game, (9999, 9999))
        self.Add_Rune_To_Dict(dash_rune)
        self.game.item_handler.Add_Item(dash_rune)


        fire_resistance_rune = Fire_Resistance_Rune(self.game, (9999, 9999))
        self.Add_Rune_To_Dict(fire_resistance_rune)
        self.game.item_handler.Add_Item(fire_resistance_rune)


    
    def Add_Rune_To_Dict(self, rune):
        type = rune.type
        if type not in self.runes:
            self.runes[type] = []
        self.runes[type].append(rune)
    
    def Add_Runes_To_Inventory_TEST(self):
        self.Add_Rune_To_Rune_Inventory('healing_rune')
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