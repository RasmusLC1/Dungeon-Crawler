from scripts.entities.decoration.chest.loot_container import Loot_Container
from scripts.engine.assets.keys import keys
import random

key_empty = 'empty'

class Bookshelf(Loot_Container):
    def __init__(self, game, pos) -> None:
        self.enemies = {}
        super().__init__(game, keys.bookshelf, pos, False, 99, (32, 32))
        self.tile.Set_Physics(True) # Bookshelf is impassible


    def Set_Loot_Types(self):
        self.loot_types = [keys.recipe_scroll,
                           keys.temptress_embrace,
                           keys.demonic_bargain,
                           keys.blood_tomb,
                           keys.recipe_scroll,
                           key_empty
                           ]
        
        self.loot_weights = {keys.recipe_scroll : 0.1,
                             keys.temptress_embrace: 0.1,
                             keys.demonic_bargain: 0.1,
                             keys.blood_tomb: 0.1,
                             keys.recipe_scroll: 0.1,
                             keys.rune: 0.2,
                             key_empty : 2
                             }
        
        self.loot_categories = {
            keys.recipe_scroll : keys.curse,
            keys.temptress_embrace : keys.curse,
            keys.demonic_bargain : keys.curse,
            keys.blood_tomb : keys.curse,
            keys.recipe_scroll : keys.passive,
        } 

    def Spawn_Loot(self, loot_type, pos):
        print(loot_type)
        if loot_type == key_empty:
            return
        elif loot_type == keys.rune:
            self.Open_Rune_Menu()
        else:
            loot_category = self.loot_categories[loot_type]
            self.game.item_handler.loot_handler.Spawn_Loot_Type(loot_category, pos, None, loot_type)
        return

    def Open_Rune_Menu(self):
        rune = self.Select_Available_Rune()
        if not rune:
            print("Rune not found, bookshelf")
            return False
        
        self.game.menu_handler.rune_bookshelf_menu.Initialise_Runes(self, rune)
        self.game.state_machine.Set_State('rune_bookshelf_menu')

        return True


    def Select_Available_Rune(self):
        # Convert the dictionary keys into a list
        rune_keys = list(self.game.rune_handler.runes.keys())

        # Pick a random key from the dictionary
        random_key = random.choice(rune_keys)

        # Get the rune object using the random key
        rune = self.game.rune_handler.runes[random_key]

        # Check if the rune is already active
        if rune in self.game.rune_handler.active_runes:
            return self.Select_Available_Rune()
        
        return rune