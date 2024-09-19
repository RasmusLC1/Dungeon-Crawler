from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.arrow import Arrow
import math
import pygame


class Bow(Weapon):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size, 'bow', 3, 8, 10, 'ranged')
        self.max_animation = 0
        self.attack_animation_max = 2
        self.distance_from_player = 0
        self.attack_animation_counter = 0
        self.arrow = None


    def Update(self, offset = (0,0)):
        if self.arrow:
            self.arrow.Set_Equipped_Position()
            self.arrow.Set_Active(self.active)
            self.arrow.Set_Light_Level(self.light_level)
        return super().Update(offset)
    

    def Set_Speed(self, speed):
        self.speed = speed

    def Set_Attack(self):
        pass
    
    def Update_Animation(self):
        if self.is_charging:
            return
        super().Update_Animation()


    def Update_Attack_Animation(self):
        self.sub_type = self.type + '_attack'
        self.animation = self.attack_animation
        self.Set_Attack_Direction()
        self.Point_Towards_Mouse()
        self.Set_Attack_Position()


    # Determine the position of the bow when being drawn
    def Set_Attack_Position(self):
        new_x_pos = 0
        new_y_pos = 0
        new_y_pos = self.entity.rect().center[1] + self.entity.attack_direction[1] * 2 - 12
        if self.entity.attack_direction[0] < 0:
            self.flip_image = False
            new_x_pos = self.entity.rect().midleft[0] - 4
        else:
            self.flip_image = False
            new_x_pos = self.entity.rect().midright[0] - 4

        self.Move((new_x_pos, new_y_pos))

    # Set the position of the bow when not drawn
    def Set_Equipped_Position(self, direction_y):
        self.Move((self.entity.pos[0] + 2, self.entity.pos[1] - 6))
        self.rotate = -30
    

    def Charge_Attack(self, offset = (0, 0)):
        try:
            if 'player' == self.entity.type:
                if not self.inventory_type:
                    return
                self.Set_Charging_Player()
                self.Player_Shooting()
            elif 'enemy' == self.entity.subtype:
                self.Set_Charging_Enemy()
        except TypeError as e:
            print(f"Entity neither enemy nor player: {e}")
        
        if not self.inventory_type:
            return

        self.Set_Charging_Player()
    
    def Player_Shooting(self):
        if self.is_charging:
            self.Update_Attack_Animation()
            if not self.charge_time:
                self.attack_animation_time = self.max_charge_time // (self.attack_animation_max + 1)
            # Increase charge time while holding the button
            self.charge_time += 1
            if self.charge_time >= self.max_charge_time:
                self.charge_time = self.max_charge_time  # Cap the charge time
                self.charged_attack = True  # Mark the attack as charged
            else:
                self.attack_animation_counter += 1
                if not self.arrow:
                    if not self.Find_Arrow():
                        self.Reset_Bow()
                        return
                    self.game.entities_render.Remove_Entity(self.arrow) # Remove the arrow
                    
                    self.game.sfx['bow_draw'].play()
                if self.attack_animation_time <= self.attack_animation_counter:
                    self.attack_animation_counter = 0
                    self.attack_animation = min(self.attack_animation_max, self.attack_animation + 1)

        elif self.charge_time > 0:
            self.game.sfx['arrow_shot'].play()
            self.Shoot_Arrow()
            self.Reset_Bow()

    def Enemy_Shooting(self):
        if not self.entity.charge:
            return False

        if self.is_charging > 70:
            # print(vars(self.arrow))
            self.charge_time = 120
            self.arrow.Set_Special_Attack(self.is_charging)
            self.arrow.Set_Delete_Countdown(50)
            self.Shoot_Arrow()
            self.Reset_Bow()
            return True
        
        # self.charge_time = self.entity.charge
        if self.is_charging >= self.max_charge_time:
            self.is_charging = self.max_charge_time  # Cap the charge time
            self.charged_attack = True  # Mark the attack as charged
        else:
            self.attack_animation_counter += 1
            self.Spawn_Arrow()
            self.game.item_handler.Add_Item(self.arrow)

            if self.attack_animation_time <= self.attack_animation_counter:
                self.attack_animation_counter = 0
                self.attack_animation = min(self.attack_animation_max, self.attack_animation + 1)
        return False

   


    def Shoot_Arrow(self):
        arrow_damage = min(2, self.charge_time // 10)
        arrow_speed = max(3, self.charge_time // 10)
        self.arrow.Set_Damage(arrow_damage)
        self.arrow.Set_Speed(arrow_speed)
        self.arrow.Set_Special_Attack(self.charge_time, self.game.render_scroll)
        self.arrow.Special_Attack()

    def Reset_Bow(self):
        # Reset only if necessary to avoid redundant calls
        if self.arrow or self.charge_time > 0:
            self.charge_time = 0
            self.charged_attack = False
            self.animation = 0
            self.attack_animation_counter = 0
            self.attack_animation = 0
            self.arrow = None

    def Find_Arrow(self):
        weapon_inventory = self.game.weapon_inventory.inventories[1]
        inventory_slot = weapon_inventory.inventory[1]
        if not inventory_slot.item:
            return False
        # print(inventory_slot.item.type)
        
        if not inventory_slot.item.type == 'arrow':
            return False
        
        if not inventory_slot.item.amount > 0:
            return False
        
        self.Spawn_Arrow()
        inventory_slot.item.Decrease_Amount(1)
        inventory_slot.Remove_Item_On_Amount()
        

        return True


    def Shoot_Arrow(self):
        if not self.arrow:
            return
        arrow_damage = max(8, self.charge_time // 10)
        arrow_speed = max(10, self.charge_time // 10)
        self.arrow.Set_Damage(arrow_damage)
        self.arrow.Set_Speed(arrow_speed)
        self.arrow.Set_Special_Attack(self.charge_time, self.game.render_scroll)
        self.arrow.Special_Attack()
        self.arrow = None


    def Spawn_Arrow(self):
        if not self.arrow:  # Check if arrow already exists to prevent duplication
            arrow = Arrow(self.game, (self.pos[0] + 2, self.pos[1]), (16, 16))
            self.arrow = arrow
            self.arrow.Shooting_Setup(self.entity)



    # Point the weapon towards the mouse
    def Point_Towards_Mouse(self):
        self.rotate = 0
        
        # Get the direction
        dx = self.game.mouse.mpos[0] - self.entity.pos[0]
        dy = self.game.mouse.mpos[1] - self.entity.pos[1]

        # Calculate the angle in degrees
        self.rotate = math.degrees(math.atan2(dy, dx))
        self.rotate *= -1



    def Modify_Offset(self, rotate):
        self.rotate += rotate
        print(self.rotate)

    def Send_To_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):
        if not self.Bow_Inventory_Check(inventory_slot):
            return False
        return super().Send_To_Inventory(inventory_slot, sending_inventory, receiving_inventory)

    def Bow_Inventory_Check(self, inventory_slot):
        print(inventory_slot.inventory_type)

        if not 'bow' in self.type:
            return True

        if not inventory_slot.inventory_type:
            return True
        if 'bow' in inventory_slot.inventory_type:
            return True
        else:
            return False
        
    def Render_Equipped(self, surf, offset=(0, 0)):
        super().Render_Equipped(surf, offset)
        if not self.entity:
            return
        if self.entity.active > 20 and self.arrow:
                self.arrow.Render_Equipped(surf, offset)