from scripts.engine.assets.keys import keys

class Damage_Handler_Weapon():
    def __init__(self, weapon, effect, damage):
        self.weapon = weapon
        self.damage = {} # Damage dictionary allows many damage types on same weapon
        self.Set_Damage(effect, damage) # The damage the wepaon does

    
    def Entity_Hit(self, entity):
        weapon_entity = self.weapon.entity
        if not weapon_entity or not entity:
            return
        for damage_type in self.damage:
            damage = self.Calculate_Damage(damage_type)
            entity.Damage_Taken(damage, weapon_entity.attack_direction)

            if entity.effects.thorns.effect:
                weapon_entity.Damage_Taken(entity.effects.thorns.effect, weapon_entity.attack_direction)

            self.Check_Effects(damage_type, entity)

    def Decoration_Hit(self, decoration):
        weapon_entity = self.weapon.entity
        if not weapon_entity or not decoration:
            return
        
        for damage_type in self.damage:
            damage = self.Calculate_Damage(damage_type)
            decoration.Damage_Taken(damage, damage_type)


    def Check_Effects(self, damage_type, entity):
        damage = self.damage[damage_type]
        weapon_entity = self.weapon.entity
        # Check if weapon is vampiric first, to avoid double healing
        if damage_type == keys.vampiric or weapon_entity.effects.vampiric:
            weapon_entity.Set_Effect(keys.healing, damage // 2)
            return
        # Set special status effect of weapon if weapon has one
        entity.Set_Effect(damage_type, max(1, round(damage // 10)))

    def Calculate_Damage(self, damage_type):
        return self.weapon.entity.strength * self.damage[damage_type]
    
    def Get_Damage(self):
        return sum(self.damage.values())

    def Set_Damage(self, damage_type, damage):
        if damage_type in self.damage:
            self.damage[damage_type] += damage
        else:
            self.damage[damage_type] = damage

    # Iterate over the damage dictionary once and get the first key
    def Get_First_Effect(self):
        return next(iter(self.damage), None)
    
