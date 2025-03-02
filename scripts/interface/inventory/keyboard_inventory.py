class Keyboard_Inventory():
    def __init__(self, game, shared_inventory, shared_inventory_dic):
        self.inventory = shared_inventory
        self.shared_inventory_dic = shared_inventory_dic
        self.game = game
    
    def Key_Board_Input(self):
        index = self.Check_Keyboard_input()
        
        # negative index means it's not found
        if index < 0:
            return
        
        self.Activate_Inventory_Slot(index)

    # Return negative if not no keyboard input
    def Check_Keyboard_input(self):
        keyboard = self.game.keyboard_handler

        match True:
            case keyboard._1_pressed:
                return 0
            case keyboard._2_pressed:
                return 1
            case keyboard._3_pressed:
                return 2
            case keyboard._4_pressed:
                return 3
            case keyboard._5_pressed:
                return 4
            case keyboard._6_pressed:
                return 5
            case keyboard._7_pressed:
                return 6
            case keyboard._8_pressed:
                return 7
            case keyboard._9_pressed:
                return 8
            case keyboard.z_pressed:
                return 9
            case keyboard.x_pressed:
                return 10
            case keyboard.c_pressed:
                return 11
            case _:
                return -999


    def Activate_Inventory_Slot(self, index):
        inventory_slot = self.shared_inventory_dic[index]
        if inventory_slot.item:
            inventory_slot.item.Activate()
            inventory_slot.Update()