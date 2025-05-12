from scripts.entities.items.loot.loot import Loot
import random


class Phoenix_Feather(Loot):
    def __init__(self, game, pos):
        super().__init__(game, self.game.dictionary.phoenix_feather, pos, (16, 16), 10, self.game.dictionary.revive)

    def Revive(self):
        self.game.particle_handler.Activate_Particles(20, 'gold', self.game.player.rect().center, frame=random.randint(40, 60))
        self.game.player.Set_Health(1)
        self.game.player.damage_cooldown = 500
        self.game.item_handler.Remove_Item(self, True)
        self.game.inventory.Remove_Item(self)
        
        return True