from scripts.items.weapons.weapon import Weapon
from scripts.items.weapons.projectiles.arrow import Arrow
import math
import pygame


class Crossbow(Weapon):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'crossbow', 3, 8, 10, 'ranged')
        self.max_animation = 0
        self.attack_animation_max = 2
        self.distance_from_player = 0
        self.attack_animation_counter = 0
        self.max_special_attack = 50
        self.ready_to_shoot = False
        self.arrow = None


    def Update(self, offset = (0,0)):
        if self.arrow:
            # self.arrow.Set_Equipped_Position()
            self.arrow.Set_Active(self.active)
            self.arrow.Set_Light_Level(self.light_level)
        return super().Update(offset)
    

    
    def Update_Animation(self):
        if self.is_charging:
            return
        super().Update_Animation()


    # Set the position of the bow when not drawn
    def Set_Equipped_Position(self, direction_y):
        self.Move((self.entity.pos[0] + 2, self.entity.pos[1]))
        self.rotate = -30

    def Update_Attack_Animation(self):
        self.sub_type = self.type + '_attack'
        self.animation = self.attack_animation
        self.Set_Block_Direction()
        self.Set_Rotation()
        self.Set_Attack_Position()


    # Determine the position of the bow when being drawn
    def Set_Attack_Position(self):
        new_x_pos = 0
        new_y_pos = 0
        new_y_pos = self.entity.rect().center[1] + self.entity.attack_direction[1] - 5
        if self.entity.attack_direction[0] < 0:
            self.flip_image = False
            new_x_pos = self.entity.rect().midleft[0] - 4
        else:
            self.flip_image = False
            new_x_pos = self.entity.rect().midright[0] - 4

        self.Move((new_x_pos, new_y_pos))


    # Charging the crossbow
    def Set_Weapon_Charge(self, offset):
        self.is_charging = self.game.mouse.hold_down_left
        if not self.is_charging or self.is_charging > self.max_special_attack:
            return
        if self.ready_to_shoot:
            self.Set_Attack()
            return
        
        if not self.arrow:
            if not self.Find_Arrow():
                self.Reset_Bow()
                self.game.entities_render.Remove_Entity(self.arrow) # Remove the arrow
                return
        self.game.sound_handler.Play_Sound('bow_draw', 1)
        if self.is_charging < self.max_special_attack:
            return
        self.ready_to_shoot = True

        

    
    def Set_Attack(self):
        if not self.ready_to_shoot:
            return
        print("TEST")
        self.game.sound_handler.Play_Sound('arrow_shot', 1)
        self.ready_to_shoot = False
        self.Shoot_Arrow()
        self.Reset_Bow()
        self.Set_Rotation()



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
        arrow_damage = 30
        arrow_speed = 1
        self.arrow.shoot_speed = 4
        self.arrow.Set_Damage(arrow_damage)
        self.arrow.Set_Speed(arrow_speed)
        self.game.item_handler.Add_Item(self.arrow)


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


    def Spawn_Arrow(self):
        if not self.arrow:  # Check if arrow already exists to prevent duplication
            arrow = Arrow(self.game, (self.pos[0] + 2, self.pos[1]), (16, 16))
            self.arrow = arrow
            self.entity.Attack_Direction_Handler(self.game.render_scroll)

            self.arrow.Shooting_Setup(self.entity, self.entity.attack_direction)


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
        if self.entity.type == 'player' and self.arrow or self.entity.active > 20 and self.arrow:
                self.arrow.Render_Equipped(surf, offset)