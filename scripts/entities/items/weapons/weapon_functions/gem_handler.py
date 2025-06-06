import pygame
from scripts.engine.assets.keys import keys

class Gem_Handler():
    def __init__(self, weapon):
        self.weapon = weapon
        self.gems = []
        self.max_gems = 3

    def Add_Gems(self, gem):
        if self.gems.count() > self.max_gems:
            return False
        self.gems.append(gem)
        
        self.weapon.Set_Damage(gem.effect, gem.damage)
        return True
    
    def Remove_Gem(self, gem_id):
        for gem in self.gems:
            if gem.ID == gem_id:
                self.gems.remove(gem)
                return True
            
        return False


    def Increase_Max_Gems(self):
        self.max_gems += 1

    def Render_Effects(self, surf, offset=(0, 0)):
        for gem in self.gems:
            gem.Render_Effect(surf, offset, self.weapon.pos)