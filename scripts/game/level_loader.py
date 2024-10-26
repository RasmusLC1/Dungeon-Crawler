
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

    def Load_Level_New_Map(self, map_id):
        self.game.game_initialiser.initialise_Engine()

        file_path = f'data/maps/{map_id}.json'
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("File not found")
        self.game.dungeon_generator.Generate_Map()
        self.load_level(map_id)
        self.Initialise_Level()

        


    def Clear_Level(self):
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
        self.game.item_inventory.Clear_Inventory()
        self.game.weapon_inventory.Clear_Inventory()
        self.game.rune_inventory.Clear_Inventory()
        self.game.a_star.Clear_Map()
        
        self.game.tilemap.Clear_Tilemap()


    def load_level(self, map_id):
        self.Clear_Level()

        self.game.tilemap.Load('data/maps/' + str(map_id) + '.json')

        if not self.initialised:
            self.Initial_Setup()
        else:
            for spawner in self.game.tilemap.extract([('spawners', 0)]):
                if spawner['variant'] == 0:
                    print("PLAYER SPAWN")
                    self.game.player = Player(self.game, spawner['pos'], (8, 16), 100, 5, 7, 10, 5, 5)
                    break


        self.game.a_star.Setup_Map(self.game)


    def Initial_Setup(self):
        # Setup handlers
        self.game.light_handler = Light_Handler(self.game)
        
        
        self.game.particles = []
        self.game.sparks = []
        self.game.scroll = [0, 0]
        # Spawn Player
        # if not self.initialised:

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
        self.initialised = True