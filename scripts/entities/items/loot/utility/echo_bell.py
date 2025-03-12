from scripts.entities.items.loot.utility.utility_loot import Utility_Loot
import random

class Echo_Bell(Utility_Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'echo_bell', pos, 320)
        self.activations = random.randint(2, 4)
        self.Set_Description()
    
    

    def Update(self):
        super().Update()

    def Set_Description(self):
        self.description = 'Lure enemies\nto a location\n' + str(self.activations) + 'times'


    def Reset_Bell(self):
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
            self.Toll_Bell()

    

    # Effect of opening door on key
    def Toll_Bell(self):
        self.game.clatter.Generate_Clatter(self.game.mouse.mpos, 1000) # Generate clatter to alert enemies
        self.Reset_Bell()
