from scripts.entities.items.loot.utility.utility_loot import Utility_Loot

class Recall_Parchment(Utility_Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'recall_parchment', pos, 320)
        self.activations = 1
        self.Set_Description()

 
    def Update(self):
        super().Update()

    def Set_Description(self):
        self.description = 'Teleport back\nto latest shrine\n' + str(self.activations) + 'times'

    # Handle reset normally in case item that increases use of other items
    def Reset_Cloak(self):
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
        
        self.Teleport_To_Shrine()

    
    # Effect of opening door on key
    def Teleport_To_Shrine(self):
        player = self.game.player
        if not player.last_shrine_visited:
            return False
        player.Set_Position(player.last_shrine_visited.pos.copy())
        self.Reset_Cloak()
        return True

    def Render_Line(self, surf, offset, alpha):
        pass