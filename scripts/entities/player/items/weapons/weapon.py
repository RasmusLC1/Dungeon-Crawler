import pygame
from scripts.entities.player.items.item import Item
from scripts.entities.entities import PhysicsEntity

class Weapon(Item):
    def __init__(self, game, pos, size, type, damage, speed, range, weapon_class):
        super().__init__(game, type, 'weapon', pos, size, 1)
        self.damage = damage
        self.speed = speed
        self.range = range
        self.in_inventory = False
        self.equipped = False
        # Can be expanded to damaged or dirty versions of weapons later
        self.sub_type = self.type
        self.weapon_class = weapon_class

    def Attack(self):
        print(self.inventory_type)

    

    # Inventory Logic below
    #######################################################

    def Handle_Double_Click(self, sending_inventory, receiving_inventory):
        recieving_inventory_slot = receiving_inventory.Find_Available_Inventory_Slot()
        if not recieving_inventory_slot:
            return False
        if self.Send_To_Inventory(recieving_inventory_slot, sending_inventory, receiving_inventory):
            return True     

    
    # Attempt to move the item to the receiving inventory slot by double clicking
    def Send_To_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):

        move_successful = receiving_inventory.Move_Item(self, inventory_slot)       
        # If the move was successful, remove it from the sending inventory
        if move_successful:

            # Remove item from old inventory and save the inventory type
            inventory_type_holder = self.inventory_type
            sending_inventory.Remove_Item(self, move_successful)
            # send weapon into weapon inventory, checked by seeing if it has an inventory_type
            if self.inventory_type:
                # If weapon is already equipped in the other hand, remove it before adding to new hand
                if self.equipped:
                    self.game.player.Remove_Active_Weapon(inventory_type_holder)                    
                self.equipped = True
                self.game.player.Set_Active_Weapon(self, self.inventory_type)
            else: # Drag weapon back into item inventory
                self.equipped = False
                self.game.player.Remove_Active_Weapon(inventory_type_holder)
            return True
        
        return False
    
    # Add weapons from a sending inventory to a receiving inventory
    # Example: weapon_inventory (sending) -> inventory (receiving) 
    def Move_To_Other_Inventory(self, sending_inventory, receiving_inventory, offset = (0,0)):
        if self.game.mouse.left_click:
            return
        
        for receiving_inventory_slot in receiving_inventory:
            if receiving_inventory_slot.rect().colliderect(self.game.mouse.rect_pos(offset)):
                if self.Send_To_Inventory(receiving_inventory_slot, sending_inventory, receiving_inventory):
                    return True             
        return False

    # Check if the weapon can be moved to the weapon inventory
    def Move_Inventory_Check(self, offset = (0,0)):
        if self.picked_up:
            active_inventory = self.game.weapon_inventory.active_inventory
            weapon_inventory = self.game.weapon_inventory.inventories[active_inventory]
            if self.equipped: # Move to normal inventory
                if self.Move_To_Other_Inventory(weapon_inventory, self.game.item_inventory, offset):
                    self.equipped = False
                    self.game.player.Remove_Active_Weapon(self.inventory_type)
                    return True
                
                
            else: # Move to weapon inventory
                if self.Move_To_Other_Inventory(self.game.item_inventory, weapon_inventory, offset):
                    self.equipped = True
                    self.game.player.Set_Active_Weapon(self, self.inventory_type)
                    return True
                
        return False

    # Check for out of bounds, return true if valid, else false
    def Move_Legal(self, mouse_pos, player_pos, tilemap, offset = (0,0)):

        # Check if the weapon can be moved to the weapon inventory
        if self.Move_Inventory_Check(offset):
            self.picked_up = False
            self.move_inventory = True
            return False
        if super().Move_Legal(mouse_pos, player_pos, tilemap, offset):
            return True
        
        
        
        else:
            return False

    def Update_Player_Hand(self, prev_hand):
        # print("TEST")
        # # Check if the weapon has changed hands
        # print(self.inventory_type)
        print(prev_hand)
        if self.inventory_type != prev_hand:
            self.equipped = True
            if prev_hand == 'left_hand':
                self.game.player.Remove_Active_Weapon(prev_hand)
                self.game.player.Set_Active_Weapon(self, self.inventory_type)
            elif prev_hand == 'right_hand':
                self.game.player.Remove_Active_Weapon(prev_hand)
                self.game.player.Set_Active_Weapon(self, self.inventory_type)


    def Place_Down(self):
        super().Place_Down()
        self.equipped = False
        return False

    def Set_In_Inventory(self, state):
        self.in_inventory = state
    ####################################################### 
    
    def Render_In_Inventory(self, surf, offset=(0, 0)):
        
        item_image = pygame.transform.scale(self.game.assets[self.sub_type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    def Render_Equipped(self, surf, offset = (0,0)):
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        return

    def Render(self, surf, offset=(0, 0)):

        # Check if item is in inventory. If yes we don't need offset, except if
        # the weapon has been picked up
        if self.in_inventory:
            if self.picked_up:
                self.Render_In_Inventory(surf, offset)
            else:
                self.Render_In_Inventory(surf)
        
        if not self.Update_Light_Level():
            return
        
        # Set image
        weapon_image = self.game.assets[self.sub_type][self.animation].convert_alpha()

        # Set alpha value to make chest fade out
        alpha_value = max(0, min(255, self.active))
        weapon_image.set_alpha(alpha_value)

        # Blit the dark layer
        dark_surface_head = pygame.Surface(weapon_image.get_size(), pygame.SRCALPHA).convert_alpha()
        dark_surface_head.fill((self.light_level, self.light_level, self.light_level, 255))

        # Blit the chest layer on top the dark layer
        weapon_image.blit(dark_surface_head, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        # Render the chest
        surf.blit(weapon_image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
