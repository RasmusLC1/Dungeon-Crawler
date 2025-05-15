from scripts.entities.items.loot.utility.utility_loot import Utility_Loot
import random
from scripts.engine.assets.keys import keys

class Shadow_Cloak(Utility_Loot):
    def __init__(self, game, pos):
        amount = random.randint(1, 2)
        super().__init__(game, keys.shadow_cloak, pos, 320, amount)
        self.max_amount = 3
        self.Set_Description()

 
    def Update(self):
        super().Update()

    def Set_Description(self):
        self.description = 'Become\ninvisibile'

    # When cloak runs out of charges it's deleted
    def Reset_Cloak(self):
        self.amount -= 1
        if self.amount:
            self.clicked = False
            self.Set_Description() # Update description
            return
        
        self.game.item_handler.Remove_Item(self, True)
        self.game.inventory.Remove_Item(self)
    
    # The update function in the inventory
    def Update_In_Inventory(self):
        if not super().Update_In_Inventory():
            return False
        
        self.Activate_Invisibility()

    
    # Effect of opening door on key
    def Activate_Invisibility(self):
        self.game.player.Set_Effect(keys.invisibility, 5)
        self.Reset_Cloak()

    def Render_Line(self, surf, offset, alpha):
        pass