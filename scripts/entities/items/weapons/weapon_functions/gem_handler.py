import pygame
from scripts.engine.assets.keys import keys


# TODO: Remove the entity effects when the weapon is not equipped and enable them when equipped
class Gem_Handler():
    def __init__(self, weapon):
        self.weapon = weapon
        self.gems = []
        self.max_gems = 3

        self.gem_entity_effects = [
            keys.arcane_hunger,
            keys.halo,
            keys.power,
            keys.strength,
        ]

    def Add_Gem(self, gem):
        if len(self.gems) >= self.max_gems:
            return False
        
        if not self.Set_Effect(gem):
            return False
        
        self.gems.append(gem)
        
        return True
    
    # Finds and calls the various effect functions
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
            keys.range : self.Increase_Range,
            keys.speed : self.Increase_Speed,
            keys.durability : self.Increase_Durability,
            keys.arcane_hunger : self.Set_Entity_Effect_Gem,
            keys.halo : self.Set_Entity_Effect_Gem,
            keys.power : self.Set_Entity_Effect_Gem,
            keys.strength : self.Set_Entity_Effect_Gem,
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
    
    # Set entity effect if player has weapon equipped. Only works for player
    def Set_Entity_Effect_Gem(self, gem):
        entity = self.weapon.entity

        if not entity:
            return False
        
        if not entity.type == keys.player:
            return False
        
        if not entity.weapon_handler.Check_If_Weapon_Is_Equipped(self.weapon):
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
    def Remove_Entity_Effect_Gems(self):
        for gem in self.gems:
            if not gem.effect in self.gem_entity_effects:
                continue
            
            self.weapon.entity.Remove_Effect(gem.effect, self.Get_Effect_Amount(gem))

    def Set_Entity_Effect_Gems(self):
        for gem in self.gems:
            if not gem.effect in self.gem_entity_effects:
                continue
            
            self.weapon.entity.Set_Effect(gem.effect, self.Get_Effect_Amount(gem), True)

    def Increase_Max_Gems(self):
        self.max_gems += 1

    def Render_Effects(self, surf, offset=(0, 0)):
        for gem in self.gems:
            gem.Render_Effect(surf, offset, self.weapon.pos)


    