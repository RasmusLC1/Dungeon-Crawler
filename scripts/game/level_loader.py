
from scripts.entities.moving_entities.player.player import Player
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.entities.items.item_handler import Item_Handler

from scripts.entities.decoration.decoration_handler import Decoration_Handler
from scripts.entities.moving_entities.enemies.enemy_handler import Enemy_Handler
from scripts.engine.lights.light_handler import Light_Handler
from scripts.inventory.inventory_handler import Inventory_Handler


from scripts.entities.items.runes.rune_handler import Rune_Handler

import os


class Level_Loader():
    def __init__(self, game) -> None:
        self.game = game
        self.initialised = False

    def load_level_From_Save(self, map_id):
        # Initialise the engine again upon load to prevent memory leaks
        self.game.game_initialiser.initialise_Engine()

        self.load_level(map_id)
        self.game.save_load_manager.Load_Data_Structure() # Load data from save file


    def Initialise_Level(self):
        self.game.item_handler.Initialise()
        self.game.enemy_handler.Initialise()
        self.game.rune_handler.Initialise_Runes()
        self.game.decoration_handler.Initialise(3)
        self.game.trap_handler.Initialise()

    def Load_Level_New_Map(self, map_id, clear_inventory = True):
        self.game.game_initialiser.initialise_Engine()
        self.game.dungeon_generator.Generate_Map(map_id)
        self.load_level(map_id, clear_inventory)
        self.Initialise_Level()


        
    def Clear_Level(self, clear_inventory = True):
        if not self.initialised:
            return
        self.game.entities_render.Clear_Entities()
        self.game.enemy_handler.Clear_Enemies()
        self.game.item_handler.Clear_Items()
        # self.game.particle_handler.
        self.game.rune_handler.Clear_Runes()
        self.game.trap_handler.Clear_Traps()
        self.game.light_handler.Clear_Lights()
        self.game.decoration_handler.Clear_Decorations()
        if clear_inventory:
            self.game.inventory.Clear_Inventory()
        self.game.a_star.Clear_Maps()
        
        self.game.tilemap.Clear_Tilemap()


    def load_level(self, map_id, clear_inventory = True):
        self.Clear_Level(clear_inventory)

        self.game.tilemap.Load('data/maps/' + str(map_id) + '.json')
        if not self.initialised:
            self.Initial_Setup()
        else:
            self.Spawn_Player()


        self.game.a_star.Setup_Map_From_Game(self.game)


    def Initial_Setup(self):
        # Setup handlers
        self.game.light_handler = Light_Handler(self.game)
        
        
        self.game.sparks = []
        self.game.scroll = [0, 0]
        # Spawn Player
        self.Spawn_Player()
 
 
        self.game.inventory = Inventory_Handler(self.game)
        self.game.enemy_handler = Enemy_Handler(self.game)
        self.game.item_handler = Item_Handler(self.game)
        self.game.particle_handler = Particle_Handler(self.game)
        self.game.trap_handler = Trap_Handler(self.game)
        self.game.decoration_handler = Decoration_Handler(self.game)
        self.game.rune_handler = Rune_Handler(self.game)
        self.initialised = True

    def Spawn_Player(self):
        for spawner in self.game.tilemap.extract([('spawners', 0)]):
            if spawner.variant == 0:
                self.game.player = Player(self.game, spawner.pos, (28, 28), 100, 5, 5, 5, 5, 5)
                return