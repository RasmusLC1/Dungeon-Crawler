from scripts.entities.items.weapons.magic_attacks.base_attacks.elemental_explosion import Elemental_Explosion

class Fire_Explosion(Elemental_Explosion):
    def __init__(self, game, pos, power, entity = None):
        super().__init__(game, game.keys.fire_explosion, game.keys.fire, pos, power, 3, 7, 5, entity)
        