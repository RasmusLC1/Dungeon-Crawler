from scripts.entities.items.weapons.weapon import Weapon

class Bell(Weapon):
    def __init__(self, game, pos, damage_type = 'blunt'):
        super().__init__(game, pos, 'bell', 4, 2, 3, 50, 'one_handed_melee', damage_type)
        self.max_animation = 7
        self.attack_animation_max = 8

    def Set_Attack(self):
        self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies
        super().Set_Attack()


    # Handle special attack charge
    def Special_Attack(self):
        if not self.entity:
            return
        
        if self.special_attack <= 0 or not self.equipped:
            # self.Reset_Special_Attack()
            return
        self.Ring_Bell()
        

    def Update_Heal_Cooldown(self):
        if not self.heal_cooldown:
            return
        self.heal_cooldown = max(0, self.heal_cooldown - 1)
    
    # Initialise the charge logic
    def Ring_Bell(self):
        self.game.clatter.Generate_Clatter(self.pos, 1000) # Generate clatter to alert nearby enemies
        self.special_attack = 0
