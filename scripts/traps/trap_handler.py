from scripts.traps.spike import Spike
from scripts.traps.spike_poisoned import Spike_Poisoned
from scripts.traps.bear_trap import Bear_Trap
from scripts.traps.spike_pit import Spike_Pit
from scripts.traps.top_push_trap import Top_Push_Trap
from scripts.environment.lava import Lava
from scripts.environment.water import Water
from scripts.environment.ice import Ice
from scripts.traps.fire_trap import Fire_Trap
import math



class Trap_Handler:
    def __init__(self, game):
        self.traps = []
        self.nearby_traps = []
        self.environment = []
        self.game = game

        # Spawner initialisation
        for spawner in game.tilemap.extract([('spawners', 0)]):
            game.player.pos = spawner['pos']

        

        # Spike initialisation
        for trap in self.game.tilemap.extract([('spike_trap', 0)].copy(), True):
            self.traps.append(Spike(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))
        
        # Spike initialisation
        for trap in self.game.tilemap.extract([('spike_poison_trap', 0)].copy(), True):
            self.traps.append(Spike_Poisoned(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))
       
        # top pusher initialisation
        for trap in self.game.tilemap.extract([('TopPush_trap', 0)].copy()):
            self.traps.append(Top_Push_Trap(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        # Bear Trap initialisation
        for trap in self.game.tilemap.extract([('Bear_trap', 0)].copy()):
            self.traps.append(Bear_Trap(self.game, trap['pos'], (16, 16), trap['type']))

        # Spike pit initialisation
        for trap in self.game.tilemap.extract([('Pit_trap', 0)].copy(), True):
            self.traps.append(Spike_Pit(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('Lava_env', 0)].copy(), True):
            self.traps.append(Lava(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('shallow_water_env', 0)].copy(), True):
            self.traps.append(Water(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('medium_water_env', 0)].copy(), True):
            self.traps.append(Water(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('deep_water_env', 0)].copy(), True):
            self.traps.append(Water(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('shallow_ice_env', 0)].copy(), True):
            self.traps.append(Ice(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('medium_ice_env', 0)].copy(), True):
            self.traps.append(Ice(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('deep_ice_env', 0)].copy(), True):
            self.traps.append(Ice(self.game, trap['pos'], (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.game.tilemap.extract([('Fire_trap', 0)].copy()):
            self.traps.append(Fire_Trap(self.game, trap['pos'], (16, 16), trap['type']))


    def find_nearby_traps(self, player_pos, max_distance):
        nearby_traps = []
        for trap in self.traps:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - trap.pos[0]) ** 2 + (player_pos[1] - trap.pos[1]) ** 2)
            if distance < max_distance:
                nearby_traps.append(trap)
        return nearby_traps
    
    def Update(self):
        self.nearby_traps = self.find_nearby_traps(self.game.player.pos, 200)
        for trap in self.nearby_traps:
            trap.Animation_Update()
            

    def Render(self, offset = (0,0)):
        for trap in self.nearby_traps:
            trap.Render(self.display, offset)

