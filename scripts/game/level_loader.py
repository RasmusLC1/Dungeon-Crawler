
from scripts.entities.player.player import Player
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.items.item_handler import Item_Handler

from scripts.decoration.chest.Chest_handler import Chest_Handler
from scripts.decoration.doors.door_handler import Door_Handler
from scripts.entities.enemies.enemy_handler import Enemy_Handler
from scripts.engine.lights.light_handler import Light_Handler


from scripts.items.runes.rune_handler import Rune_Handler


import pygame


class Level_Loader():
    def __init__(self, game) -> None:
        self.game = game

    def load_level_From_Save(self, map_id):
        self.load_level(map_id)
        self.game.save_load_manager.Load_Data_Structure() # Load data from save file
        # self.game.item_handler.Initialise()


    def Load_Level_New_Map(self, map_id):
        self.game.dungeon_generator.Generate_Map()
        self.load_level(map_id)
        self.game.item_handler.Initialise()
        self.game.enemy_handler.Initialise()
        self.game.door_handler.Initialise()
        self.game.chest_handler.Initialise(3)
        self.game.trap_handler.Initialise()
        self.game.rune_handler.Initialise_Runes()


    def load_level(self, map_id):
        self.game.tilemap.Load('data/maps/' + str(map_id) + '.json')
        
         # Setup handlers
        self.game.light_handler = Light_Handler(self.game)
        
        
        self.game.particles = []
        self.game.sparks = []
        self.game.scroll = [0, 0]
        self.game.projectiles = []
        # Spawn Player
        for spawner in self.game.tilemap.extract([('spawners', 0)]):
            if spawner['variant'] == 0:
                self.game.player = Player(self.game, spawner['pos'], (8, 16), 100, 5, 7, 10, 5, 5)

        self.game.enemy_handler = Enemy_Handler(self.game)
        self.game.item_handler = Item_Handler(self.game)
        self.game.particle_handler = Particle_Handler(self.game)
        self.game.trap_handler = Trap_Handler(self.game)
        self.game.chest_handler = Chest_Handler(self.game)
        self.game.door_handler = Door_Handler(self.game)
        self.game.rune_handler = Rune_Handler(self.game)
        


           

        self.game.a_star.Setup_Map(self.game)

