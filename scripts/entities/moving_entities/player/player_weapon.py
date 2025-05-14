from scripts.engine.assets.keys import keys


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
        self.Update_Left_Weapon(offset)

    def Set_Active_Weapon(self, weapon):  
          
        equipped_weapon = weapon
        equipped_weapon.Move(self.player.pos)
        self.active_weapon_left = equipped_weapon
        return

    def Set_Attack_Lock(self, state):
        self.attack_lock = state
    

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
        # Set the attack lock above the update to prevent attacks
        if self.attack_lock:
            return

        self.active_weapon_left.Update(offset)
        if not self.active_weapon_left:
            return
        
        self.active_weapon_left.Update_Attack()
        self.player.Attacking(self.active_weapon_left, offset)

        
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
        
        if self.attack_lock:
            return
        self.active_weapon_right.Update(offset)
        if not self.active_weapon_right:
            return
        self.active_weapon_right.Update_Attack()
        self.player.Attacking(self.active_weapon_right, offset)
        
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

        if self.attack_lock:
            return
        self.active_bow.Update(offset)
        if not self.active_bow:
            return
        
        self.active_bow.Update_Attack()
        self.player.Attacking(self.active_bow, offset)
        
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
        # Return if inventory has not been clicked
        if self.game.mouse.inventory_clicked:
            return 0
        if weapon.attacking:
            cooldown = max(5 + weapon.attacking, 100/self.player.agility + weapon.attacking)
            return cooldown
        return 0
    
    def Set_Inventory_Interaction(self, state):
        self.inventory_interaction = state

    def Remove_Active_Weapon(self):
        if self.active_weapon_left:
            self.active_weapon_left.Unequip()
            self.active_weapon_left = None
            self.left_weapon_cooldown = 0
            self.player.attacking = 0


    def Render_Weapons(self, surf, offset):

        if self.active_weapon_left:
            self.active_weapon_left.Render_Equipped(surf, offset)