from scripts.traps.traps.spike import Spike
from scripts.traps.traps.spike_poisoned import Spike_Poisoned
from scripts.traps.traps.bear_trap import Bear_Trap
from scripts.traps.traps.spike_pit import Spike_Pit
from scripts.traps.traps.top_push_trap import Top_Push_Trap
from scripts.traps.traps.fire_trap import Fire_Trap
from scripts.traps.environment.lava import Lava
from scripts.traps.environment.water import Water
from scripts.traps.environment.ice import Ice
from scripts.traps.traps.spider_web import Spider_Web
import math



class Trap_Handler:
    def __init__(self, game):
        self.traps = []
        self.nearby_traps = []
        self.environment = []
        self.game = game

        self.nearby_traps_cooldown = 0
        # TODO: Create seperate spawner class
        # Spawner initialisation
        for spawner in self.game.tilemap.extract([('spawners', 0)]):
            self.game.player.pos = spawner['pos']

        self.Initialise()
        

    def Initialise(self):
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

        for trap in self.game.tilemap.extract([('spider_web', 3)].copy()):
            self.traps.append(Spider_Web(self.game, trap['pos'], (16, 16), trap['type']))



    def Find_Nearby_Traps(self, player_pos, max_distance):
        
        nearby_traps = []
        for trap in self.traps:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - trap.pos[0]) ** 2 + (player_pos[1] - trap.pos[1]) ** 2)
            if distance < max_distance:
                nearby_traps.append(trap)
        return nearby_traps
    
    def Update(self):
        if self.nearby_traps_cooldown:
            self.nearby_traps_cooldown = max(0, self.nearby_traps_cooldown - 1)
            return
        else:
            self.nearby_traps_cooldown = 50
            self.nearby_traps.clear()
            self.nearby_traps = self.Find_Nearby_Traps(self.game.player.pos, 200)

        for trap in self.nearby_traps:
            if not trap:
                continue
            trap.Animation_Update()
            
    def Remove_Trap(self, trap):
        self.game.ray_caster.Remove_Trap(trap)
        if trap in self.traps:
            self.traps.remove(trap)
        if trap in self.nearby_traps:
            self.nearby_traps.remove(trap)
        del(trap)

    def Add_Trap(self, trap):
        self.traps.append(trap)

    def Render(self, traps, surf, offset = (0,0)):
        for trap in traps:
            if not trap:
                continue
            
            trap.Render(surf, offset)

