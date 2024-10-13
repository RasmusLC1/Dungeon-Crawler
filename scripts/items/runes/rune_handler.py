from scripts.items.runes.healing_rune import Healing_Rune

import pygame

class Rune_Handler():
    def __init__(self, game):
        self.game = game
        self.runes = {}
        self.active_runes = []
        self.Initialise()

    def Initialise(self):
        healing_rune = Healing_Rune(self.game, (9999, 9999), 10, 5)
        self.Add_Rune_To_Dict(healing_rune)
        # self.game.item_handler.Add_Item(healing_rune)
    
    def Add_Rune_To_Dict(self, rune):
        type = rune.type
        if type not in self.runes:
            self.runes[type] = []
        self.runes[type].append(rune)

    def Add_Rune_To_Rune_Inventory(self, rune_type):
        if rune_type not in self.runes:
            return False
        rune = self.runes[rune_type][0]
        rune.active = True
        self.active_runes.append(rune)
        self.game.rune_inventory.Add_Item(rune)


    def Update(self, offset = (0,0)):
        pass

    def Render(self, surf, offset = (0, 0)):
        for rune in self.active_runes:
            item_image = pygame.transform.scale(self.game.assets[rune.type][rune.animation], rune.size)  
            surf.blit(item_image, (rune.pos[0] - 3, rune.pos[1] - 3))