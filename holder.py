
from scripts.entities.player.player import Player
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.items.item_handler import Item_Handler

from scripts.decoration.decoration_handler import Decoration_Handler
from scripts.entities.enemies.enemy_handler import Enemy_Handler
from scripts.engine.lights.light_handler import Light_Handler
from scripts.inventory.item_inventory import Item_Inventory
from scripts.inventory.weapon_inventory_handler import Weapon_Inventory_Handler
from scripts.inventory.rune_inventory import Rune_Inventory


from scripts.items.runes.rune_handler import Rune_Handler


import pygame


class Level_Loader():
    def __init__(self, game) -> None:
        self.game = game
        self.initialised = False

    def load_level_From_Save(self, map_id):
        self.load_level(map_id)
        self.game.save_load_manager.Load_Data_Structure() # Load data from save file


    def Initialise_Level(self):
        self.game.dungeon_generator.Generate_Map()
        self.game.item_handler.Initialise()
        self.game.enemy_handler.Initialise()
        self.game.decoration_handler.Initialise(3)
        self.game.trap_handler.Initialise()
        self.game.rune_handler.Initialise_Runes()

    def Load_Level_New_Map(self, map_id):
        self.game.dungeon_generator.Generate_Map()
        self.load_level(map_id)
        self.Initialise_Level()


    def Clear_Level(self):
        if not self.initialised:
            return
        del(self.game.enemy_handler)
        del(self.game.item_handler)
        del(self.game.particle_handler)
        del(self.game.trap_handler)
        del(self.game.projectiles)
        del(self.game.particles)
        del(self.game.light_handler)
        del(self.game.item_inventory) 
        del(self.game.weapon_inventory)
        del(self.game.rune_inventory) 

        self.game.tilemap.Clear_Tilemap()


    def load_level(self, map_id):
        # self.Clear_Level()
        self.game.tilemap.Clear_Tilemap()

        self.game.tilemap.Load('data/maps/' + str(map_id) + '.json')
        
         # Setup handlers
        self.game.light_handler = Light_Handler(self.game)
        
        
        self.game.particles = []
        self.game.sparks = []
        self.game.scroll = [0, 0]
        self.game.projectiles = []
        # Spawn Player
        if not self.initialised:
            self.initialised = True

            for spawner in self.game.tilemap.extract([('spawners', 0)]):
                if spawner['variant'] == 0:
                    print("PLAYER SPAWN")
                    self.game.player = Player(self.game, spawner['pos'], (8, 16), 100, 5, 7, 10, 5, 5)
                    break
                
        self.game.item_inventory = Item_Inventory(self.game)
        self.game.weapon_inventory = Weapon_Inventory_Handler(self.game, 'warrior', self.game.proffeciency)
        self.game.rune_inventory = Rune_Inventory(self.game)
        self.game.enemy_handler = Enemy_Handler(self.game)
        self.game.item_handler = Item_Handler(self.game)
        self.game.particle_handler = Particle_Handler(self.game)
        self.game.trap_handler = Trap_Handler(self.game)
        self.game.decoration_handler = Decoration_Handler(self.game)
        self.game.rune_handler = Rune_Handler(self.game)

        self.game.a_star.Setup_Map(self.game)


