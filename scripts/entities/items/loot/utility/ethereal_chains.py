from scripts.entities.items.loot.radius_effect_loot import Radius_Effect_Loot
import random
import pygame

class Ethereal_Chains(Radius_Effect_Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'ethereal_chains', pos, 150, 'utility', 3)
        self.activations = random.randint(2, 4)
        self.Set_Description()
        
   

    def Set_Description(self):
        self.description = 'Snares nearby\n enemies' + str(self.activations) + 'times'

    def Update(self):
        return super().Update()

    # If out of activations, reset the hourglass
    def Reset_Chains(self):
        self.activations -= 1

        if self.activations:
            self.clicked = False
            self.Set_Description() # Update description
            return
        
        self.game.item_handler.Remove_Item(self, True)
        self.game.inventory.Remove_Item(self)
    
    # The update function in the inventory
    def Update_In_Inventory(self):
        if not super().Update_In_Inventory():
            return False

        if self.game.mouse.left_click:
            self.Snare_Enemies()

        return True


    def Render_Line(self, surf, offset, alpha):
        pass

    # Effect of opening door on key
    def Snare_Enemies(self):
        self.Find_Nearby_Entities_Mouse()
        for enemy in self.nearby_entities:
            enemy.effects.Set_Effect("snare", 3)
        self.Reset_Chains()
    

    