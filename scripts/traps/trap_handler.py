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
        self.game = game
        self.traps = []
        self.nearby_traps = []
        self.saved_data = {}


        self.nearby_traps_cooldown = 0
        
    
    def Save_Trap_Data(self):
        for trap in self.traps:
            trap.Save_Data()
            self.saved_data[trap.ID] = trap.saved_data

    def Load_Data(self, data):
        for item_id, item_data in data.items():
            if not item_data:
                continue

            type = item_data['type']
            pos = item_data['pos']
            size = item_data['size']
            try: 
                self.Trap_Spawner(pos, size, type, item_data)
            except Exception as e:
                print("DATA WRONG", item_data, e)

    def Initialise(self):
        # Spike initialisation
        for trap in self.game.tilemap.extract([('spike_trap', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])
            
        # Spike initialisation
        for trap in self.game.tilemap.extract([('spike_poison_trap', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])


        # top pusher initialisation
        for trap in self.game.tilemap.extract([('TopPush_trap', 0)].copy()):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])


        # Bear Trap initialisation
        for trap in self.game.tilemap.extract([('Bear_trap', 0)].copy()):
            self.Trap_Spawner(trap['pos'], (16, 16), trap['type'])

        # Spike pit initialisation
        for trap in self.game.tilemap.extract([('Pit_trap', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])

        for trap in self.game.tilemap.extract([('Lava_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])

        for trap in self.game.tilemap.extract([('shallow_water_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])


        for trap in self.game.tilemap.extract([('medium_water_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])

        for trap in self.game.tilemap.extract([('deep_water_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])


        for trap in self.game.tilemap.extract([('shallow_ice_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])



        for trap in self.game.tilemap.extract([('medium_ice_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])

        for trap in self.game.tilemap.extract([('deep_ice_env', 0)].copy(), True):
            size = (self.game.assets[trap['type']][0].get_width(), self.game.assets[trap['type']][0].get_height())
            self.Trap_Spawner(trap['pos'], size, trap['type'])

        for trap in self.game.tilemap.extract([('Fire_trap', 0)].copy()):
            self.Trap_Spawner(trap['pos'], (16, 16), trap['type'])

        for trap in self.game.tilemap.extract([('spider_web', 3)].copy()):
            self.Trap_Spawner(trap['pos'], (16, 16), trap['type'])

    def Trap_Spawner(self, pos, size, type, data = None):
        trap = None
        if 'spike_trap' == type:
            trap = self.Spawn_Spike_Trap(pos, size, type)

        elif type == 'spike_poison_trap':
            trap = self.Spawn_Spike_Poisoned(pos, size, type)

        elif type == 'TopPush_trap':
            trap = self.Spawn_Top_Push_Trap(pos, size, type)

        elif 'Bear_trap' == type:
            trap = self.Spawn_Bear_Trap(pos, size, type)

        elif 'Pit_trap' == type:
            trap = self.Spawn_Spike_Pit(pos, size, type)

        elif 'Lava_env' == type:
            trap = self.Spawn_Lava(pos, size, type)

        elif 'ice' in type:
            trap = self.Spawn_Ice(pos, size, type)

        elif 'water' in type:
            trap = self.Spawn_Water(pos, size, type)

        elif type == 'Fire_trap':
            trap = self.Spawn_Fire_Trap(pos, size, type)

        elif type == 'spider_web':
            trap = self.Spawn_Spider_Web(pos, size, type)
        else:
            print(type)
        if not trap:
            return False
        
        if data:
            trap.Load_Data(data)

        self.traps.append(trap)
        return True



    def Spawn_Fire_Trap(self, pos, size, type):
        return Fire_Trap(self.game, pos, size, type)
    
    def Spawn_Ice(self, pos, size, type):
        return Ice(self.game, pos, size, type)
    
    def Spawn_Water(self, pos, size, type):
        return Water(self.game, pos, size, type)
    
    def Spawn_Lava(self, pos, size, type):
        return Lava(self.game, pos, size, type)
    
    def Spawn_Spike_Pit(self, pos, size, type):
        return Spike_Pit(self.game, pos, size, type)
    
    def Spawn_Bear_Trap(self, pos, size, type):
        return Bear_Trap(self.game, pos, size, type)
    
    def Spawn_Top_Push_Trap(self, pos, size, type):
        return Top_Push_Trap(self.game, pos, size, type)
    
    def Spawn_Spike_Poisoned(self, pos, size, type):
        return Spike_Poisoned(self.game, pos, size, type)
    
    def Spawn_Spike_Trap(self, pos, size, type):
        return Spike(self.game, pos, size, type)
    
    def Spawn_Spider_Web(self, pos, size, type):
        return Spider_Web(self.game, pos, size, type)
    

    def Find_Nearby_Traps(self, player_pos, max_distance):
        
        nearby_traps = []
        for trap in self.traps:
            # Calculate the Euclidean distance
            distance = math.sqrt((player_pos[0] - trap.pos[0]) ** 2 + (player_pos[1] - trap.pos[1]) ** 2)
            if distance < max_distance:
                nearby_traps.append(trap)
        return nearby_traps
    
    def Update(self):
        if self.Update_Nearby_Traps_Cooldown():
            self.nearby_traps.clear()
            self.nearby_traps = self.Find_Nearby_Traps(self.game.player.pos, 200)

        for trap in self.nearby_traps:
            if not trap:
                continue
            trap.Animation_Update()
    
    def Reset_Nearby_Traps_Cooldown(self):
        self.nearby_traps_cooldown = 1

    def Update_Nearby_Traps_Cooldown(self):
        if self.nearby_traps_cooldown:
            self.nearby_traps_cooldown = max(0, self.nearby_traps_cooldown - 1)
            return False
        self.nearby_traps_cooldown = 50
        return True

    def Remove_Trap(self, trap):
        self.game.ray_caster.Remove_Trap(trap)
        if trap in self.traps:
            self.traps.remove(trap)
        if trap in self.nearby_traps:
            self.nearby_traps.remove(trap)
        del(trap)

    def Add_Trap(self, trap):
        self.traps.append(trap)

