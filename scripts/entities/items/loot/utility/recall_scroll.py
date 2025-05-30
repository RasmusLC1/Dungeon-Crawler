from scripts.entities.items.loot.utility.utility_loot import Utility_Loot
from scripts.engine.assets.keys import keys

class Recall_Scroll(Utility_Loot):
    def __init__(self, game, pos):
        super().__init__(game, keys.recall_scroll, pos, 320, 1)
        self.max_amount = 3
        self.Set_Description()


 
    def Update(self):
        super().Update()

    def Set_Description(self):
        self.description = 'Teleport back\nto latest shrine'

    # Handle reset normally in case item that increases use of other items
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
        
        self.Teleport_To_Shrine()

    
    # Effect of opening door on key
    def Teleport_To_Shrine(self):
        player = self.game.player
        if not player.last_shrine_visited:
            return False
        player.Set_Position(player.last_shrine_visited.pos.copy())
        self.Reset_Cloak()
        self.game.sound_handler.Play_Sound(self.type, 1)
        return True

    def Render_Line(self, surf, offset, alpha):
        pass