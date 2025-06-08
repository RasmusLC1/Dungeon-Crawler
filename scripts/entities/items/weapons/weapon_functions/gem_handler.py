import pygame
from scripts.engine.assets.keys import keys


# TODO: Remove the entity effects when the weapon is not equipped and enable them when equipped
class Gem_Handler():
    def __init__(self, weapon):
        self.weapon = weapon
        self.gems = []
        self.max_gems = 3

    def Add_Gems(self, gem):
        if self.gems.count() > self.max_gems:
            return False
        
        if not self.Set_Effect(gem):
            return False
        
        self.gems.append(gem)
        
        self.weapon.Set_Damage(gem.effect, gem.amount)
        return True
    
    def Set_Effect(self, gem):
        gem_effects = {
            keys.fire : self.Set_Damage_Effect,
            keys.frozen : self.Set_Damage_Effect,
            keys.electric : self.Set_Damage_Effect,
            keys.poison : self.Set_Damage_Effect,
            keys.electric : self.Set_Damage_Effect,
            keys.vampiric : self.Set_Damage_Effect,
            keys.blunt : self.Set_Damage_Effect,
            keys.slash : self.Set_Damage_Effect,
            keys.wet : self.Set_Damage_Effect,
            keys.terror : self.Set_Damage_Effect,
            keys.vulnerable : self.Set_Damage_Effect,
            keys.weakness : self.Set_Damage_Effect,
            keys.arcane_hunger : self.Set_Entity_Effect,
            keys.halo : self.Set_Entity_Effect,
            keys.power : self.Set_Entity_Effect,
            keys.strength : self.Set_Entity_Effect,
            keys.range : self.Increase_Range,
            keys.speed : self.Increase_Speed,
            keys.durability : self.Increase_Durability,
        }

        gem_function = gem_effects.get(gem.effect)

        if not gem_function:
            return False
        
        return gem_function(gem)
        
        


    def Set_Damage_Effect(self, gem):
        self.weapon.Set_Damage(gem.effect, gem.amount)
        return True
    
    def Get_Effect_Amount(self, gem):
        return round(gem.amount // 10)

    def Set_Entity_Effect(self, gem):
        if not self.weapon.entity.type == keys.player:
            return False
        
        self.weapon.entity.Set_Effect(gem.effect, self.Get_Effect_Amount(gem), True)
        return True
    

    def Increase_Durability(self, gem):
        self.weapon.Increase_Durability(gem.amount)

    def Increase_Range(self, gem):
        self.weapon.Increase_Range(gem.amount)
    
    def Increase_Speed(self, gem):
        self.weapon.Increase_Speed(gem.amount)

    # TODO: REMOVE THE EFFECT from SET_EFFECT
    def Remove_Gem(self, gem_id):
        for gem in self.gems:
            if gem.ID == gem_id:
                self.gems.remove(gem)
                return True
            
        return False
    
    # TODO: REMOVE THE EFFECT from SET_EFFECT
    def Remove_Entity_Effect_Gems(self):
        remove_entity_effects = [
            keys.arcane_hunger,
            keys.halo,
            keys.power,
            keys.strength,
        ]

        for gem in self.gems:
            if not gem.effect in remove_entity_effects:
                continue
            
            self.weapon.entity.Remove_Effect(gem.effect, self.Get_Effect_Amount(gem))




    def Increase_Max_Gems(self):
        self.max_gems += 1

    def Render_Effects(self, surf, offset=(0, 0)):
        for gem in self.gems:
            gem.Render_Effect(surf, offset, self.weapon.pos)


    