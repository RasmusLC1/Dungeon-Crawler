from scripts.entities.items.loot.bombs.bomb import Bomb
from scripts.entities.items.weapons.magic_attacks.fire.fire_explosion import Fire_Explosion


class Fire_Bomb(Bomb):
    def __init__(self, game, pos):
        super().__init__(game, 'fire_bomb', pos)

    def Explode(self):
        fire_explosion = Fire_Explosion(self.game, self.pos, self.damage)
        self.game.item_handler.Add_Item(fire_explosion)
        return super().Explode()

    
