from scripts.entities.items.weapons.weapon import Weapon
from scripts.entities.items.weapons.projectiles.arrow import Arrow
from scripts.engine.assets.keys import keys


# Parent class for ranged weapons
class Ranged_Weapon(Weapon):
    def __init__(self, game, pos, type, damage, speed, range, max_charge_time):
        super().__init__(game, pos, type, damage, speed, range, max_charge_time, 'ranged')
        self.is_charging = 0
        self.ready_to_shoot = False
        self.arrow = None


    def Update(self, offset = (0,0)):
        if self.arrow:
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
        print("IMPLEMENT SET WEAPON CHARGE")
        return

        
    
    def Set_Attack(self):
        if not self.ready_to_shoot:
            return
        if not self.Find_Arrow():
            return
        self.game.sound_handler.Play_Sound('arrow_shot', 1)
        self.ready_to_shoot = False
        self.Shoot_Arrow()
        self.Reset_Bow()
        self.Set_Rotation()



    def Shoot_Arrow(self):
        if not self.arrow:
            return
        arrow_speed = 3
        self.arrow.Set_Damage(self.damage * 5)
        self.arrow.Set_Speed(arrow_speed)
        self.game.item_handler.Add_Item(self.arrow)


    def Reset_Bow(self):
        # Reset only if necessary to avoid redundant calls
        if self.arrow or self.is_charging <= 0:
            self.is_charging = 0
            self.animation = 0
            self.attack_animation_counter = 0
            self.attack_animation = 0
            self.arrow = None

    def Find_Arrow(self):
        if self.arrow:
            return True
        
        if not self.game.inventory.item_inventory.Find_Arrow():
            return False

        if not self.Spawn_Arrow():
            return False
        
        return True


    def Spawn_Arrow(self):
        if self.arrow:  # Check if arrow already exists to prevent duplication
            False

        arrow = Arrow(self.game, (self.pos[0] + 2, self.pos[1]), 1, (16, 16))
        self.arrow = arrow
        self.entity.Attack_Direction_Handler(self.game.render_scroll)

        self.arrow.Shooting_Setup(self.entity, self.entity.attack_direction)
        return True
        


    def Modify_Offset(self, rotate):
        self.rotate += rotate

    def Send_To_Inventory(self, inventory_slot, sending_inventory, receiving_inventory):
        if not self.Bow_Inventory_Check(inventory_slot):
            return False
        return super().Send_To_Inventory(inventory_slot, sending_inventory, receiving_inventory)

    def Bow_Inventory_Check(self, inventory_slot):

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