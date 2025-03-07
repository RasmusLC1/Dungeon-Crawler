from scripts.interface.inventory.base_inventory import Base_Inventory
from scripts.interface.inventory.inventory_slot import Inventory_Slot
from scripts.interface.inventory.weapon_inventory.weapon_inventory_slot import Weapon_Inventory_Slot



class Weapon_Inventory(Base_Inventory):
    def __init__(self, game, shared_inventory, shared_inventory_dic):
        self.active_inventory_slot = None
        self.current_active_index = None
        self.max_active_index = None
        super().__init__(game, shared_inventory, shared_inventory_dic)

    def Append_Inventory_Dic(self, inventory_slot):
        if not inventory_slot.item:
            return
        # Ensure the type exists in the dictionary before appending
        if inventory_slot.item.type not in self.inventory_dic:
            self.inventory_dic[inventory_slot.item.type] = []  # Initialize if not present
        
        self.inventory_dic[inventory_slot.item.type].append(inventory_slot)
        

    def Setup(self):
        for i in range(2):
            (x, y) = self.Set_Inventory_Slot_Pos(i)
            inventory_slot = Weapon_Inventory_Slot(self.game, (x, y), 'weapon', self.size, None, i + 12, str(10))
            inventory_slot.Set_White_List(['weapon'])
            self.Add_Inventory_Slot(inventory_slot)
            self.Initalise_Active_Inventory_Slot(inventory_slot)
    
    # Initialise the active inventory slot, so it's always the first inventory slot
    def Initalise_Active_Inventory_Slot(self, inventory_slot):
        if self.active_inventory_slot:
            return
        
        self.Set_Active_Inventory_Slot(inventory_slot)
        self.max_active_index = inventory_slot.index + 1 # Set the maximum index
        self.current_active_index = inventory_slot.index

    # Transition between active inventory slots by mouse scroll
    def Mouse_Scroll_Update_Active_Inventory(self):
        if self.current_active_index >= self.max_active_index:
            self.current_active_index -= 1
        else:
            self.current_active_index += 1 

        self.Set_Active_Inventory_Slot(self.shared_inventory_dic[self.current_active_index])

    # Set the new inventory slot and reset previous one
    def Set_Active_Inventory_Slot(self, inventory_slot):
        if self.active_inventory_slot:
            self.active_inventory_slot.Remove_Active_Inventory()
        self.active_inventory_slot = inventory_slot
        inventory_slot.Set_Active_Inventory()

    # Equip the weapon in the active inventory regardless of wether it's set or not
    # Worst case it just overrides existing, but it prevents the inventory from getting stuck
    def Equip_Weapon(self):
        if not self.active_inventory_slot.item:
            return
        
        self.active_inventory_slot.item.Reset_Weapon_Charge() # Prevents instant attack when equipped
        self.active_inventory_slot.item.Equip()
        

    def Set_Inventory_Slot_Pos(self, index):
        x = index * self.size[1] + self.game.screen_width / 2 / self.game.render_scale - 240
        y = self.game.screen_height / self.game.render_scale - 40
        return (x, y)
