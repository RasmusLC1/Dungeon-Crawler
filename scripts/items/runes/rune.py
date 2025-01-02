from scripts.items.item import Item
import pygame
import math
from scripts.entities.textbox.rune_textbox import Rune_Textbox



class Rune(Item):
    def __init__(self, game, type, pos, power, soul_cost):
        super().__init__(game,  type, 'rune', pos, (32, 32), 1, False)
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
        self.picked_up = True
        self.cost_to_buy = soul_cost // 2 * power // 2
        self.activate_cooldown = 0
        self.activate_cooldown_max = 200
        self.clicked = False # Used for projectiles
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
    
    
    def Activate(self):
        if self.activate_cooldown:
            return False
        if not super().Activate():
            return False
        if self.game.player.souls < self.current_soul_cost:
            return False
        self.Trigger_Effect()
        return True
    
    def Trigger_Effect(self):
        if self.game.player.Set_Effect(self.effect, self.current_power):
            self.Trigger_Rune()

    def Trigger_Rune(self):
        self.Compute_Souls_Cost()
        self.Set_Animation_Time()
        self.Reset_Animation_Size()
        self.Set_Activate_Cooldown(self.activate_cooldown_max)
    
    def Compute_Souls_Cost(self):
        if self.game.player.effects.arcane_conduit.effect:
            self.game.player.Decrease_Souls(max(1, self.current_soul_cost - self.game.rune_handler.arcane_conduit_rune.current_power))
        else:
            self.game.player.Decrease_Souls(self.current_soul_cost)

    def Set_Menu_Pos(self, pos):
        self.menu_pos = pos

    def Remove_Rune_From_Inventory(self):
        pass

    def Modify_Souls_Cost(self, change):
        if self.game.player.souls < self.upgrade_cost:
            return False
        if self.current_soul_cost + change < self.min_soul_cost:
            return False
        self.current_soul_cost += change
        return True

    def Modify_Upgrade_Cost(self, change):
        self.upgrade_cost += change
        return True
    
    def Modify_Power(self, change):
        if self.game.player.souls < self.upgrade_cost:
            return False
        self.current_power += change
        return True
    
    def Update_Activate_Cooldown(self):
        if self.activate_cooldown:
            self.activate_cooldown -= 1

    
    def Set_Activate_Cooldown(self, value):
        self.activate_cooldown = value

    def Set_Animation_Time(self):
        self.animation_time = self.animation_time_max

    def Reset_Animation_Size(self):
        self.animation_size = 0

    def Increase_Animation_Size(self):
        self.animation_size = min(self.animation_size + 1, self.animation_size_max)

    # Always return False as runes cannot be placed down
    def Move_Legal(self, mouse_pos, player_pos, tilemap, offset=...):
        return False
    

    def Update_Animation(self):
        if self.animation_time:
            self.animation_time = max(0, self.animation_time - 1)
            self.Increase_Animation_Size()
    
    # Defualt the Render function to render in inventory
    def Render(self, surf, offset=(0, 0)):
        item_image = pygame.transform.scale(self.game.assets[self.type][self.animation], self.size)  
        surf.blit(item_image, (self.pos[0] - 3, self.pos[1] - 3))

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
        
        self.game.symbols.Render_Symbol(surf, self.effect,  (self.game.player.pos[0] - offset[0] + 8 - inversed_animation_size, self.game.player.pos[1] - offset[1] - inversed_animation_size), inversed_animation_size)
        


    def Menu_Rect(self):
        return pygame.Rect(self.menu_pos[0], self.menu_pos[1], (self.size[0] * 1.5), (self.size[1] * 1.5))
