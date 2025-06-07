from scripts.engine.assets.keys import keys
from scripts.entities.items.weapons.weapon_functions.damage_handler_weapon import Damage_Handler_Weapon

class Ranged_Damage_Handler_Weapon(Damage_Handler_Weapon):
    def __init__(self, weapon, effect, damage):
        super().__init__(weapon, effect, damage)
        self.nearby_enemies = []
        self.damage_multiplier = 1


    # Damage Entity
    def Entity_Hit_Ranged(self, entity):
        weapon_entity = self.weapon.entity
        if not weapon_entity:
            return
        for damage_type in self.damage:
            damage = self.Calculate_Ranged_Damage(damage_type)

            print(damage, self.damage_multiplier)
            entity.Damage_Taken(damage, weapon_entity.attack_direction)
            if entity.effects.thorns.effect:
                weapon_entity.Damage_Taken(entity.effects.thorns.effect, weapon_entity.attack_direction)

            self.Check_Effects(damage_type, entity)
        


    def Calculate_Ranged_Damage(self, damage_type):
        return self.damage[damage_type] * self.damage_multiplier
    
    def Find_Nearby_Enemies(self):
        weapon_entity = self.weapon.entity
        game = self.weapon.game

        self.nearby_enemies = game.enemy_handler.Find_Nearby_Enemies(weapon_entity, self.weapon.shoot_distance * self.weapon.shoot_speed)
        if weapon_entity.category == keys.enemy:
            self.nearby_enemies.append(game.player)


    # Check for collision on attack
    def Attack_Collision_Check_Projectile(self):
        for entity in self.nearby_enemies:
            # Check if the enemy is on damage cooldown
            if entity.damage_cooldown:
                continue

            # Check for collision with enemy
            if self.weapon.rect().colliderect(entity.rect()):
                self.Entity_Hit_Ranged(entity)
                # Return enemy in case further effects need to be added such as knockback
                return entity
            
        return None
    
    # Bows, crossbow and other shooting weapons can impart a multiplier onto the projectile
    def Reset_Damage_Multiplier(self):
        self.damage_multiplier = 1

    def Set_Damage_Multiplier(self, multiplier):
        self.damage_multiplier = max(0, min(100, multiplier))
