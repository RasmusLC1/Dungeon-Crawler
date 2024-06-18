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
    def __init__(self):
        self.traps = []
        self.nearby_traps = []
        self.environment = []

        # Spawner initialisation
        for spawner in self.tilemap.extract([('spawners', 0)]):
            self.player.pos = spawner['pos']

        

        # Spike initialisation
        for trap in self.tilemap.extract([('spike', 0)], True):
            self.traps.append(Spike(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))
        
        # Spike initialisation
        for trap in self.tilemap.extract([('spike_poison', 0)], True):
            self.traps.append(Spike_Poisoned(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))
       
        # top pusher initialisation
        for trap in self.tilemap.extract([('TopPush', 0)]):
            self.traps.append(Top_Push_Trap(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        # Bear Trap initialisation
        for trap in self.tilemap.extract([('BearTrap', 0)]):
            self.traps.append(Bear_Trap(self, trap['pos'], (16, 16), trap['type']))

        # Spike pit initialisation
        for trap in self.tilemap.extract([('PitTrap', 0)], True):
            self.traps.append(Spike_Pit(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('Lava', 0)], True):
            self.traps.append(Lava(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('shallow_water', 0)], True):
            self.traps.append(Water(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('medium_water', 0)], True):
            self.traps.append(Water(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('deep_water', 0)], True):
            self.traps.append(Water(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('shallow_ice', 0)], True):
            self.traps.append(Ice(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('medium_ice', 0)], True):
            self.traps.append(Ice(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('deep_ice', 0)], True):
            self.traps.append(Ice(self, trap['pos'], (self.assets[trap['type']][0].get_width(), self.assets[trap['type']][0].get_height()), trap['type']))

        for trap in self.tilemap.extract([('Fire_Trap', 0)]):
            self.traps.append(Fire_Trap(self, trap['pos'], (16, 16), trap['type']))


    def find_nearby_traps(self, player_pos, max_distance):
        nearby_traps = []
        for trap in self.traps:  # Assuming self.traps is a list of traps
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - trap.pos[0]) ** 2 + (player_pos[1] - trap.pos[1]) ** 2)
            if distance < max_distance:
                nearby_traps.append(trap)
        return nearby_traps
    
    def Update(self):
        self.nearby_traps = Trap_Handler.find_nearby_traps(self, self.player.pos, self.screen_width)
        for trap in self.nearby_traps:
            trap.Animation_Update()
            

    def Render(self, offset = (0,0)):
        for trap in self.nearby_traps:
            trap.Render(self.display, offset)

