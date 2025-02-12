from copy import copy
import pygame


class Player_Weapon_Handler():
    def __init__(self, game, player) -> None:
        self.game = game
        self.player = player
        self.active_weapon_left = None
        self.left_weapon_cooldown = 0
        self.active_weapon_right = None
        self.right_weapon_cooldown = 0
        self.active_bow = None
        self.bow_cooldown = 0
        self.inventory_interaction = 0
        self.attack_lock = False



    def Update(self, offset = (0, 0)):
        if self.game.weapon_inventory.active_inventory == 0:
            self.Update_Left_Weapon(offset)
            self.Update_Right_Weapon(offset)
        elif self.game.weapon_inventory.active_inventory == 1:
            self.Update_Bow(offset)
        else:
            print("INVENTORY MISSING")

    def Set_Active_Weapon(self, weapon, hand):  
        
        if not weapon or not hand:
            return False    
        equipped_weapon = weapon
        if hand == 'left_hand':
            equipped_weapon.Move(self.player.pos)
            self.active_weapon_left = equipped_weapon
            return
        if hand == 'right_hand':
            equipped_weapon.Move(self.player.pos)
            self.active_weapon_right = equipped_weapon
            return
        if 'bow' in hand:
            equipped_weapon.Move(self.player.pos)
            self.active_bow = equipped_weapon

    

    # Function to update the player's weapons
    # Each weapon needs it own method to handle it's cooldown
    def Update_Left_Weapon(self, offset=(0, 0)):

        if not self.active_weapon_left:
            return
        
        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_weapon_left.Reset_Charge()
            return
        
        self.active_weapon_left.Set_Equipped_Position(self.player.direction_y_holder)

        self.active_weapon_left.Update(offset)
        if not self.active_weapon_left:
            return

        self.active_weapon_left.Update_Attack()
        self.Attacking(self.active_weapon_left, offset)

        
        if self.left_weapon_cooldown:
            self.left_weapon_cooldown -= 1
            return

        if not self.game.mouse.left_click:
            return
        
        cooldown = self.Weapon_Attack(self.active_weapon_left)
        
        self.left_weapon_cooldown = max(self.left_weapon_cooldown, cooldown)

        return
    
    def Update_Right_Weapon(self, offset=(0, 0)):
        # Return if there's no weapon
        if not self.active_weapon_right:
            return
        # Update the weapon position and logic

        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_weapon_right.Reset_Charge()
            return

        self.active_weapon_right.Set_Equipped_Position(self.player.direction_y_holder)
        
        self.active_weapon_right.Update(offset)
        if not self.active_weapon_right:
            return

        self.active_weapon_right.Update_Attack()
        self.Attacking(self.active_weapon_right, offset)
        
        # Handle weapon cooldown
        if self.right_weapon_cooldown:
            self.right_weapon_cooldown -= 1
            return
        
        # Return if mouse has not been clicked
        if not self.game.mouse.right_click:
            return
        # Attack with weapon
        cooldown = self.Weapon_Attack(self.active_weapon_right)
        
        self.right_weapon_cooldown = max(self.right_weapon_cooldown, cooldown)

    
    def Update_Bow(self, offset=(0, 0)):
        # Return if there's no weapon
        if not self.active_bow:
            return
        # Update the weapon position and logic

        if self.inventory_interaction:
            self.Set_Inventory_Interaction(self.inventory_interaction - 1)
            self.active_bow.Reset_Charge()
            return

        self.active_bow.Set_Equipped_Position(self.player.direction_y_holder)
        
        self.active_bow.Update(offset)
        if not self.active_bow:
            return
        
        self.active_bow.Update_Attack()
        self.Attacking(self.active_bow, offset)
        
        # Handle weapon cooldown
        if self.bow_cooldown:
            self.bow_cooldown -= 1
            return
        
        # Return if mouse has not been clicked
        if not self.game.mouse.right_click:
            return
        # Attack with weapon
        cooldown = self.Weapon_Attack(self.active_bow)
        
        self.bow_cooldown = max(self.bow_cooldown, cooldown)

    
    # Activate weapon attack, return cooldown time
    def Weapon_Attack(self, weapon):
        if self.attack_lock:
            return 0
        # Return if inventory has not been clicked
        if self.game.mouse.inventory_clicked:
            return 0
        # weapon.Set_Attack()
        if weapon.attacking:
            cooldown = max(5 + weapon.attacking, 100/self.player.agility + weapon.attacking)
            return cooldown
        return 0
    
    def Attacking(self, weapon, offset=(0, 0)):
        if self.attack_lock:
            return
        if weapon.attacking and not self.player.attacking:
            self.player.Attack_Direction_Handler(offset)


            direction_x = 5 * self.player.attack_direction[0]
            direction_y = 5 * self.player.attack_direction[1]
            self.player.Set_Frame_movement((direction_x, direction_y))
            self.player.Tile_Map_Collision_Detection(self.game.tilemap)
            self.player.attacking = weapon.attacking


        if self.player.attacking == 1:
            direction_x = - 5 * self.player.attack_direction[0]
            direction_y = - 5 * self.player.attack_direction[1]
            self.player.Set_Frame_movement((direction_x, direction_y))
            self.player.Tile_Map_Collision_Detection(self.game.tilemap)

        if self.player.attacking:
            self.player.attacking -= 1
    
    def Set_Inventory_Interaction(self, state):
        self.inventory_interaction = state

    def Remove_Active_Weapon(self, hand):
        if hand == 'left_hand' and self.active_weapon_left:
            self.active_weapon_left = None
            self.left_weapon_cooldown = 0
            self.Attacking = 0

        if hand == 'right_hand' and self.active_weapon_right:
            self.active_weapon_right = None
            self.right_weapon_cooldown = 0
            self.Attacking = 0

    def Set_Attack_Lock(self, state):
        self.attack_lock = state


    def Render_Weapons(self, surf, offset):

        if self.game.weapon_inventory.active_inventory == 0:
            if self.active_weapon_left:
                self.active_weapon_left.Render_Equipped(surf, offset)
            if self.active_weapon_right:
                self.active_weapon_right.Render_Equipped(surf, offset)
        elif self.game.weapon_inventory.active_inventory == 1:
            if self.active_bow:
                self.active_bow.Render_Equipped(surf, offset)
        else:
            print("INVENTORY MISSING")