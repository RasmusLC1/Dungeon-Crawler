
from scripts.entities.decoration.decoration import Decoration
from scripts.engine.assets.keys import keys


from scripts.entities.items.weapons.weapon_handler import Weapon_Handler



class Loot_Spawner(Decoration):
    def __init__(self, game, type, pos, size, destructable, health) -> None:
        super().__init__(game, type, pos, size, destructable, health)
        self.loot_type = 0
        self.empty = False
        self.loot_amount = 0
        self.text_cooldown = 0
        self.text_animation = 0
        self.text_color = (255, 255, 255)
        self.weapon_handler = Weapon_Handler(self.game)

        
