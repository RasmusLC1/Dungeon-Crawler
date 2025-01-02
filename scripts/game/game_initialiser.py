from scripts.inventory.item_inventory import Item_Inventory
from scripts.inventory.weapon_inventory_handler import Weapon_Inventory_Handler
from scripts.inventory.rune_inventory import Rune_Inventory
from scripts.engine.ray_caster import Ray_Caster 
from scripts.entities.entity_renderer import Entity_Renderer
from scripts.engine.fonts.font import Font
from scripts.engine.fonts.symbols import Symbols
from scripts.engine.clatter import Clatter
from scripts.entities.textbox.text_box_handler import Text_Box_handler
from scripts.engine.sound.sound_handler import Sound_Handler
from scripts.level_generation.dungeon_generator import Dungeon_Generator
from scripts.interface.health_bar import Health_Bar
from scripts.interface.souls import Souls
from scripts.engine.tilemap.tilemap import Tilemap
from scripts.engine.assets.graphics_loader import Graphics_Loader
from scripts.engine.assets.audio_loader import Audio_Loader
from scripts.input.keyboard import Keyboard_Handler
from scripts.input.mouse import Mouse_Handler
from scripts.engine.a_star import A_Star
from scripts.menu.menu_handler import Menu_Handler





import pygame

class Game_Initialiser():
    def __init__(self, game) -> None:
        self.game = game

    def Initialise_Game(self):
        pygame.init()
        self.game.render_scale = 2
        
        self.game.screen_width = 1500
        self.game.screen_height = 1000
        self.game.screen = pygame.display.set_mode((self.game.screen_width, self.game.screen_height), pygame.RESIZABLE)
        self.game.display = pygame.Surface((self.game.screen_width/self.game.render_scale, self.game.screen_height/self.game.render_scale))
        self.game.render_scroll = (0,0)
        
        self.game.movement = [False, False, False, False]
        self.game.assets = {}
        Graphics_Loader.Run_All(self.game)
        Audio_Loader.Run_All(self.game)
        self.game.menu_handler = Menu_Handler(self.game)

        self.initialise_Engine()

        
        

        self.game.level = 0
        self.game.scroll = [0, 0]

    def initialise_Engine(self):
        self.game.mouse = Mouse_Handler(self.game)
        self.game.ray_caster = Ray_Caster(self.game)
        self.game.a_star = A_Star()
        self.game.entities_render = Entity_Renderer(self.game)
        self.game.default_font = Font(self.game)
        self.game.symbols = Symbols(self.game)
        self.game.clatter = Clatter(self.game)
        self.game.text_box_handler = Text_Box_handler(self.game)
        self.game.sound_handler = Sound_Handler(self.game)
        self.game.health_bar = Health_Bar(self.game)
        self.game.souls_interface = Souls(self.game)
        self.game.keyboard_handler = Keyboard_Handler(self.game)
        
        self.game.dungeon_generator = Dungeon_Generator(self.game)
        self.game.tilemap = Tilemap(self.game, tile_size=16)

        