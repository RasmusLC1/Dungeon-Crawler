from scripts.entities.items.weapons.weapon import Weapon
from scripts.engine.assets.keys import keys

class Bell(Weapon):
    def __init__(self, game, pos, damage_type = 'blunt'):
        super().__init__(game, pos, keys.bell, 4, 2, 3, 50, 'one_handed_melee', damage_type)
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
            return
        self.Ring_Bell()
        

    # Initialise the charge logic
    def Ring_Bell(self):
        self.game.clatter.Generate_Clatter(self.pos, 1000) # Generate clatter to alert nearby enemies
        self.special_attack = 0
