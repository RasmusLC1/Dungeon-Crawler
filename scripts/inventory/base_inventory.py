from scripts.inventory.inventory_slot import Inventory_Slot


class Base_Inventory():
    def __init__(self, game, shared_inventory):
        self.game = game
        self.size = (34, 34)
        self.inventory = shared_inventory
        self.inventory_dic = {}

        self.Setup()
    
    # Return True or False depending on if the type is in the dictionary
    def Clear_Inventory_Dic_Slot(self, type):
        return self.inventory_dic.pop(type, None) is not None # Remove the index


    def Find_Type_In_Inventory_Dic(self, type):
        return type in self.inventory_dic    
        
    def Append_Inventory_Dic(self, inventory_slot):
        pass

    # Configure the inventory when Initialiased
    def Setup(self):
        pass

    def Set_Inventory_Slot_Pos(self, index):
        pass

    def Add_Item(self, item):
        pass