from scripts.entities.items.item import Item
import pygame
import math
from scripts.entities.textbox.rune_textbox import Rune_Textbox
from scripts.engine.assets.keys import keys



class Rune(Item):
    def __init__(self, game, type, pos, power, soul_cost):
        super().__init__(game,  type, keys.rune, pos, (24, 24), 1, False)
        self.player = self.game.player
        self.menu_pos = pos
        self.max_amount = 1
        self.upgrade_cost = max(10, math.ceil(soul_cost / 3))
        self.original_power = power
        self.current_power = power
        self.original_soul_cost = soul_cost
        self.current_soul_cost = soul_cost
        self.min_soul_cost = math.ceil(self.original_soul_cost / 10)
        self.animation_time_max = 1
        self.animation_time = 0
        self.animation_size = 0
        self.animation_size_max = 0
        self.active = False
        self.effect = self.type.replace('_rune', '')
        self.render = True
        # self.picked_up = True
        self.cost_to_buy = soul_cost // 2 * power // 2
        self.activate_cooldown = 0
        self.activate_cooldown_max = 200
        self.clicked = False # Used for projectiles
        self.Update_Description()
        self.text_box = Rune_Textbox(self)


    def Save_Data(self):
        super().Save_Data()
        self.saved_data['effect'] = self.effect
        self.saved_data['upgrade_cost'] = self.upgrade_cost
        self.saved_data['original_power'] = self.original_power
        self.saved_data['current_power'] = self.current_power
        self.saved_data['original_soul_cost'] = self.original_soul_cost
        self.saved_data['current_soul_cost'] = self.current_soul_cost
        self.saved_data['active'] = self.active
        self.saved_data['menu_pos'] = self.menu_pos

        return self.saved_data
    
    def Load_Data(self, data):
        super().Load_Data(data)
        self.effect = data['effect'] 
        self.upgrade_cost = data['upgrade_cost'] 
        self.original_power = data['original_power'] 
        self.current_power = data['current_power']
        self.original_soul_cost = data['original_soul_cost'] 
        self.current_soul_cost = data['current_soul_cost'] 
        self.active = data['active'] 
        self.menu_pos = data['menu_pos']

    
    def Update(self):
        self.Update_Activate_Cooldown()
        return super().Update()
    
    # Calls when the rune is activated, starts by checking for cooldown, then
    # Checks defauls activation is valid, then checks if the player can pay the souls
    # Then trigger the effect
    def Activate(self):
        if self.activate_cooldown:
            return False
        
        if not super().Activate():
            return False
        if self.player.Get_Total_Available_Souls() < self.current_soul_cost:
            return False
        self.Trigger_Effect()

        return True

    # Add the player's current power level to the runes power and checks if it is
    # Valid. If yes then it triggers the rune and subtract the cost
    def Trigger_Effect(self):
        if self.player.Set_Effect(self.effect, self.current_power + self.player.effects.power.effect):
            self.Trigger_Rune()

    # Trigger the rune, cost already verified as possible in activate
    def Trigger_Rune(self):
        self.Compute_Souls_Cost()
        self.Set_Animation_Time()
        self.Reset_Animation_Size()
        self.Set_Activate_Cooldown(self.activate_cooldown_max)
        self.player.weapon_handler.Set_Attack_Lock(True)
        self.clicked = False

    
    def Compute_Souls_Cost(self):
        if self.player.effects.arcane_conduit.effect:
            self.player.Decrease_Souls(max(1, self.current_soul_cost - self.game.rune_handler.arcane_conduit_rune.current_power))
        else:
            self.player.Decrease_Souls(self.current_soul_cost)

    def Set_Menu_Pos(self, pos):
        self.menu_pos = pos

    def Remove_Rune_From_Inventory(self):
        pass

    def Modify_Souls_Cost(self, change):
        if self.player.Get_Total_Available_Souls() < self.upgrade_cost:
            return False
        if self.current_soul_cost + change < self.min_soul_cost:
            return False
        self.current_soul_cost += change
        return True

    def Modify_Upgrade_Cost(self, change):
        self.upgrade_cost += change
        return True
    
    def Modify_Power(self, change):
        if self.player.Get_Total_Available_Souls() < self.upgrade_cost:
            return False
        self.current_power += change
        return True
    
    def Update_Activate_Cooldown(self):
        if self.activate_cooldown:
            self.activate_cooldown -= 1
            if self.activate_cooldown > 0:
                self.player.weapon_handler.Set_Attack_Lock(True)
            else:
                self.player.weapon_handler.Set_Attack_Lock(False)

            return

    # Updated in rune inventory when player's power is modified
    def Update_Description(self):
        self.description = (
                            f"soul {self.current_soul_cost}\n"
                            f"power {self.current_power + self.player.effects.power.effect}\n"
                        )  

    
    def Set_Activate_Cooldown(self, value):
        self.activate_cooldown = value

    def Set_Animation_Time(self):
        self.animation_time = self.animation_time_max

    def Reset_Animation_Size(self):
        self.animation_size = 0

    def Increase_Animation_Size(self):
        self.animation_size = min(self.animation_size + 1, self.animation_size_max)


    def Update_Animation(self):
        if self.animation_time:
            self.animation_time = max(0, self.animation_time - 1)
            self.Increase_Animation_Size()
    
    # Defualt the Render function to render in inventory
    def Render_Menu(self, surf, scale = 1.5):
        item_image = pygame.transform.scale(self.game.assets[self.type][self.animation], (self.size[0] * scale, self.size[1] * scale))  
        surf.blit(item_image, (self.menu_pos[0], self.menu_pos[1]))

    def Set_Clicked(self, state):
        self.clicked = state
    
    def Render_Animation(self, surf, offset=(0, 0)):
        if not self.animation_time:
            return
        inversed_animation_size = (20 - self.animation_size) / 10 + 1
        
        self.game.symbols.Render_Symbol(surf, self.effect,  (self.player.pos[0] - offset[0] + 8 - inversed_animation_size, self.player.pos[1] - offset[1] - inversed_animation_size), inversed_animation_size)

    def Place_Down(self):
        self.game.rune_handler.Remove_Rune_From_Active_Runes(self)
        self.Delete_Item()


    def Render_In_Bounds(self, player_pos, mouse_pos, surf, offset = (0,0)):
         # Copy image and set alpha
        entity_image =  pygame.transform.scale(self.entity_image.copy(), self.floor_size)

        # Create red overlay
        red_overlay = pygame.Surface(entity_image.get_size(), pygame.SRCALPHA)
        red_overlay.fill((255, 0, 0, 100))  # Red with transparency

        # Blit entity and red overlay
        pos = (mouse_pos[0] - offset[0], mouse_pos[1] - offset[1])
        surf.blit(entity_image, pos)
        surf.blit(red_overlay, pos)

    def Menu_Rect(self):
        return pygame.Rect(self.menu_pos[0], self.menu_pos[1], (self.size[0] * 1.5), (self.size[1] * 1.5))


    def Render_Floor(self, surf, offset=(0, 0)):
        
        if not self.Update_Light_Level():
            return
        
        self.Update_Dark_Surface()
        
        # Render the item
        if not self.rendered_image:
            self.Set_Sprite()
            if not self.rendered_image:
                print(self.type, vars(self))
                self.broken_rendering_counter += 1
                if self.broken_rendering_counter >= 10:
                      self.Delete_Item()
                return
        # Hack to render the runes above the plinth they're sitting on. Runes should
        # rarely be on floor, so it shouldn't affect other visuals
        surf.blit(self.rendered_image, (self.pos[0] - offset[0], self.pos[1] - offset[1] - 10)) 