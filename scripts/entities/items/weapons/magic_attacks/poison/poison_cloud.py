from scripts.entities.items.weapons.magic_attacks.base_attacks.elemental_explosion import Elemental_Explosion

class Poison_Cloud(Elemental_Explosion):
    def __init__(self, game, pos, power, entity):
        super().__init__(game, 'poison_cloud', 'poison', pos, power, 4, 3, 30, entity)
        self.poison_cooldown = 0
        self.poison_cooldown_max = 10
        self.delete_countdown = self.max_animation * self.animation_cooldown_max * max(self.power // 2, 1)
        print(self.animation_cooldown_max )


    def Poison_Entities(self):
        if self.poison_cooldown < self.poison_cooldown_max:
            self.poison_cooldown += 1
            return
        
        self.poison_cooldown = 0
        for entity in self.nearby_entities:
            entity.effects.Set_Effect("poison", 1)



    def Update(self):
        self.pos = self.entity.rect().center
        return super().Update()

    def Update_Animation(self):
        self.Poison_Entities()
        return super().Update_Animation()
    
    def Update_Animation(self):
        super().Update_Animation()

        if self.animation >= self.max_animation:
            self.animation = 0