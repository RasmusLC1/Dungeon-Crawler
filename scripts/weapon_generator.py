import random


upgrades = ['damage', 'shooting_rate', 'knockback', 'range', 'critical_chance', 'poison', 'fire', 'electric', 'blindness', 'lifesteal', 'stun', 'ice', 'bleeding']

class Weapon:
    def __init__(self, type: str, damage: int, shooting_rate: int, knockback: int, range: int, critical_chance: int, effects):
        self.type = type
        self.damage = damage
        self.shooting_rate = shooting_rate
        self.knockback = knockback
        self.range = range
        self.critical_chance = critical_chance
        self.effects = effects

    def __str__(self):
        return (f"Weapon Type: {self.type}, Damage: {self.damage}, Shooting Rate: {self.shooting_rate}, "
                f"Knockback: {self.knockback}, Range: {self.range}, Critical Chance: {self.critical_chance}, "
                f"Effects: {', '.join(self.effects)}")

class Weapon_Generator:
    
    def Generate_Weapon(self, loot_amount):
        damage = 1
        shooting_rate = 1
        critical_chance = 0
        knockback = 0
        range = 0
        upgrades = []
        weapon_tier = Weapon_Generator.Get_Weapon_Tier()
        weapon_type = Weapon_Generator.Get_Weapon_Type(weapon_tier)
        adjusted_weapon_tier = loot_amount * weapon_tier
        print("Weapon Tier" + str(adjusted_weapon_tier))
        # Get weapon effects, giving small chance to get extra values
        i = 0
        while i < adjusted_weapon_tier:
            i += 1
            effect = random.randint(0, 100)
            if effect <= 30:
                damage += 1
                if effect < 15:
                    damage += 1
                    if effect < 5:
                        damage += 1
                        i -= 1
            elif effect <= 60:
                shooting_rate += 1
                if effect < 45:
                    shooting_rate += 1
                    if effect < 35:
                        shooting_rate += 1
                        i -= 1
            elif effect <= 80:
                critical_chance += 1
                if effect < 70:
                    critical_chance += 1
                    if effect < 65:
                        critical_chance += 1
                        i -= 1
            elif effect <= 90:
                knockback += 1
                if effect < 85:
                    knockback += 1
                    i -= 1
            elif effect == 91 and not upgrades.__contains__('poision'):
                i += 5
                if i < loot_amount:
                    upgrades.append('poision')
                else:
                    i -= 5
            elif effect == 92 and not upgrades.__contains__('fire'):
                i += 5
                if i < loot_amount:
                    upgrades.append('fire')
                else:
                    i -= 5
                i += 5
            elif effect == 93 and not upgrades.__contains__('electric'):
                i += 5
                if i < loot_amount:
                    upgrades.append('electric')
                else:
                    i -= 5
            elif effect == 94 and not upgrades.__contains__('blindness'):
                i += 5
                if i < loot_amount:
                    upgrades.append('blindness')
                else:
                    i -= 5
            elif effect == 95 and not upgrades.__contains__('lifesteal'):
                i += 7
                if i < loot_amount:
                    upgrades.append('lifesteal')
                else:
                    i -= 7
            elif effect == 96 and not upgrades.__contains__('stun'):
                i += 5
                if i < loot_amount:
                    upgrades.append('stun')
                else:
                    i -= 5
            elif effect == 95 and not upgrades.__contains__('ice'):
                i += 5
                if i < loot_amount:
                    upgrades.append('ice')
                else:
                    i -= 5
            elif effect == 96 and not upgrades.__contains__('bleeding'):
                i += 5
                if i < loot_amount:
                    upgrades.append('bleeding')
                else:
                    i -= 5
            elif effect <= 120:
                range += 1
                if effect <= 110:
                    range += 1
                    if effect <= 100:
                        range += 1
                        i -= 1
        # Generate weapon with attributes just found
        weapon = Weapon(weapon_type, damage, shooting_rate, knockback, range, critical_chance, upgrades)
        # Assign weapon to player
        self.game.player.weapons.append(weapon)
        return weapon_type

    def Get_Weapon_Tier():
        i = 1
        while i < 5:
            if random.randint(0, 10) < 5:
                break
            i += 1
        return i
    
    def Get_Weapon_Type(weapon_tier):
        weapon_type_number = random.randint(5, 100) * weapon_tier
        weapon_type = ''
        if weapon_type_number <= 30:
            weapon_type = 'knife'
        elif weapon_type_number <= 50:
            weapon_type = 'pistol'
        elif weapon_type_number <= 70:
            weapon_type = 'sword'
        elif weapon_type_number <= 90:
            weapon_type = 'spear'
        elif weapon_type_number <= 110:
            weapon_type = 'rifle'
        elif weapon_type_number <= 130:
            weapon_type = 'hammer'
        elif weapon_type_number <= 150:
            weapon_type = 'axe'
        else:
            weapon_type = 'wand'
        print(weapon_tier)
        return weapon_type
            
