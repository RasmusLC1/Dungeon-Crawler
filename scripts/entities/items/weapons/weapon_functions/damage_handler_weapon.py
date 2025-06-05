from scripts.engine.assets.keys import keys

class Damage_Handler_Weapon():
    def __init__(self, weapon, damage):
        self.weapon = weapon
        self.Set_Damage(damage) # The damage the wepaon does


    def Entity_Hit(self, entity):
        weapon_entity = self.weapon.entity
        if not weapon_entity or not entity:
            return
        damage = self.Calculate_Damage()
        entity.Damage_Taken(damage, weapon_entity.attack_direction)

        if entity.effects.thorns.effect:
            weapon_entity.Damage_Taken(entity.effects.thorns.effect, weapon_entity.attack_direction)

        if not weapon_entity:
            return
        
        self.Check_Effects(damage, entity)

    def Check_Effects(self, damage, entity):
        weapon_entity = self.weapon.entity
        weapon_effect = self.weapon.effect
        # Check if weapon is vampiric first, to avoid double healing
        if weapon_effect == keys.vampiric:
            weapon_entity.Set_Effect(keys.healing, damage // 2)
            return
        

        if weapon_entity.effects.vampiric:
            if weapon_entity.effects.vampiric.effect:
                weapon_entity.Set_Effect(keys.healing, damage // 2)


        # Set special status effect of weapon if weapon has one
        if weapon_effect:
            entity.Set_Effect(weapon_effect, 3)

    def Calculate_Damage(self):
        return self.weapon.entity.strength * self.damage
    
    def Set_Damage(self, damage):
        self.damage = damage
    
