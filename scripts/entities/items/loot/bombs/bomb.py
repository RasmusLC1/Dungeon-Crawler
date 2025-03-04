from scripts.entities.items.loot.interactive_loot import Interactive_Loot
import pygame
import math

class Bomb(Interactive_Loot):
    def __init__(self, game, type, pos):
        super().__init__(game, type, pos, 128, (20, 20))
 
    def Update(self):
        super().Update()

        if not self.target:
            return

    def Reset_Bomb(self):
        self.game.item_handler.Remove_Item(self, True)
        self.game.inventory.Remove_Item(self)
    
    # The update function in the inventory
    def Update_In_Inventory(self):
        if not super().Update_In_Inventory():
            return False
        
        if self.game.mouse.left_click:
            self.Initalise_Throw()

    

    # Effect of opening door on key
    def Initalise_Throw(self):
        # SPAWN ACTUAL BOMB PROJECTILE HERE, same sprite

        self.Reset_Bomb()
