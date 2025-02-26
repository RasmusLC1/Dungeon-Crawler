class Keyboard_Inventory():
    def __init__(self, game, shared_inventory):
        self.inventory = shared_inventory
        self.game = game
    
    def Key_Board_Input(self):
        keyboard = self.game.keyboard_handler
        index = None
        match True:
            case keyboard._1_pressed:
                index = 0
            case keyboard._2_pressed:
                index = 1
            case keyboard._3_pressed:
                index = 2
            case keyboard._4_pressed:
                index = 3
            case keyboard._5_pressed:
                index = 4
            case keyboard._6_pressed:
                index = 5
            case keyboard._7_pressed:
                index = 6
            case keyboard._8_pressed:
                index = 7
            case keyboard._9_pressed:
                index = 8
            case keyboard.z_pressed:
                index = 9
            case keyboard.x_pressed:
                index = 10
            case keyboard.c_pressed:
                index = 11
            case _:
                return  # No key pressed
        
        if not index:
            return
        
        self.Activate_Inventory_Slot(index)
        
    def Find_Inventory_Slot_Index(self, index):
        for inventory_slot in self.inventory:
            if inventory_slot.index == index:
                return inventory_slot

    def Activate_Inventory_Slot(self, index):
        inventory_slot = self.Find_Inventory_Slot_Index(index)
        if inventory_slot.item:
            inventory_slot.item.Activate()
            inventory_slot.Update()