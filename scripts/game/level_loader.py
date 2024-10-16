
from scripts.entities.player.player import Player
from scripts.engine.particles.particle_handler import Particle_Handler
from scripts.traps.trap_handler import Trap_Handler
from scripts.decoration.decoration_handler import Decoration_Handler
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
        
    def load_level(self, map_id):
        self.game.dungeon_generator.Generate_Map()
        self.game.tilemap.load('data/maps/' + str(map_id) + '.json')
         # Setup handlers
        self.game.light_handler = Light_Handler(self.game)
        
        
        self.game.particles = []
        self.game.sparks = []
        self.game.scroll = [0, 0]
        self.game.projectiles = []
        for spawner in self.game.tilemap.extract([('spawners', 0)]):
            if spawner['variant'] == 0:
                print(spawner['pos'])
                self.game.player = Player(self.game, spawner['pos'], (8, 16), 100, 5, 7, 10, 5, 5)

        self.game.particle_handler = Particle_Handler(self.game)
        self.game.enemy_handler = Enemy_Handler(self.game)
        self.game.trap_handler = Trap_Handler(self.game)
        self.game.decoration_handler = Decoration_Handler(self.game)
        self.game.chest_handler = Chest_Handler(self.game)
        self.game.door_handler = Door_Handler(self.game)
        self.game.item_handler = Item_Handler(self.game)
        self.game.item_handler.Initialise()
        self.game.rune_handler = Rune_Handler(self.game)

           

        self.game.a_star.Setup_Map(self.game)

