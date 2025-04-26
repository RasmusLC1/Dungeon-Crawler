from scripts.entities.items.loot.utility.utility_loot import Utility_Loot
import random

class Faded_Hourglass(Utility_Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'faded_hourglass', pos, 320)
        self.activations = random.randint(2, 4)
        self.Set_Description()
        self.slowdown_triggered = 0
        self.animation_cooldown = 20
        self.max_animation = 4
   

    def Set_Description(self):
        self.description = 'Slow nearby\n enemies' + str(self.activations) + 'times'

    def Update(self):
        self.Handle_Slowdown()
        return super().Update()

    def Handle_Slowdown(self):
        if not self.slowdown_triggered:
            return
        
        self.slowdown_triggered -= 1

        for enemy in self.nearby_entities:
            enemy.Set_Effect("slow_down", 8)

        if not self.slowdown_triggered:
            self.nearby_entities = None

    # If out of animations, reset the hourglass
    def Reset_Hourglass(self):
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
            self.Slow_Enemies()

    def Render_Line(self, surf, offset, alpha):
        pass

    # Effect of opening door on key
    def Slow_Enemies(self):
        self.Find_Nearby_Entities(4)
        self.slowdown_triggered = 200
        
        self.Reset_Hourglass()
