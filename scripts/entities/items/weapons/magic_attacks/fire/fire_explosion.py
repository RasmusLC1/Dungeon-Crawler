from scripts.entities.items.weapons.magic_attacks.base_attacks.elemental_explosion import Elemental_Explosion

class Fire_Explosion(Elemental_Explosion):
    def __init__(self, game, pos, power, entity = None):
        super().__init__(game, 'fire_explosion', 'fire', pos, power, 3, 7, 5, entity)
        self.light_source = self.game.light_handler.Add_Light(self.pos, 8, self.tile)
        self.light_level = self.game.light_handler.Initialise_Light_Level(self.tile)


    def Update_Animation(self):
        if self.delete_countdown == 1:
            self.game.light_handler.Remove_Light(self.light_source)
            del(self.light_source)
            
        
        super().Update_Animation()
