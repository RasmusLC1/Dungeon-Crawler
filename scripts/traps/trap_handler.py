from scripts.traps.spike import Spike
from scripts.traps.spike_poisoned import Spike_Poisoned
from scripts.traps.bear_trap import Bear_Trap
from scripts.traps.spike_pit import Spike_Pit
from scripts.traps.top_push_trap import Top_Push_Trap
from scripts.traps.lava import Lava
from scripts.traps.fire_trap import Fire_Trap



class Trap_Handler:
    def __init__(self):
        self.spikes = []
        self.spikes_poison = []
        self.bear_traps = []
        self.spike_pits = []
        self.top_pushers = []
        self.lava_tiles = []
        self.fire_traps = []
        # Spawner initialisation
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']

        # Spike initialisation
        for spike_tile in self.tilemap.extract([('spike', 0)], True):
            self.spikes.append(Spike(self, spike_tile['pos'], (self.assets[spike_tile['type']][0].get_width(), self.assets[spike_tile['type']][0].get_height())))
        
        # Spike initialisation
        for spike_tile in self.tilemap.extract([('spike_poison', 0)], True):
            self.spikes_poison.append(Spike_Poisoned(self, spike_tile['pos'], (self.assets[spike_tile['type']][0].get_width(), self.assets[spike_tile['type']][0].get_height())))
       
        # top pusher initialisation
        for top_push in self.tilemap.extract([('TopPush', 0)]):
            self.top_pushers.append(Top_Push_Trap(self, top_push['pos'], (self.assets[top_push['type']][0].get_width(), self.assets[top_push['type']][0].get_height())))

        # Bear Trap initialisation
        for trap in self.tilemap.extract([('BearTrap', 0)]):
            self.bear_traps.append(Bear_Trap(self, trap['pos'], (10, 5)))

        # Spike pit initialisation
        for spike_pit in self.tilemap.extract([('PitTrap', 0)], True):
            self.spike_pits.append(Spike_Pit(self, spike_pit['pos'], (self.assets[spike_pit['type']][0].get_width(), self.assets[spike_pit['type']][0].get_height())))

        for lava in self.tilemap.extract([('Lava', 0)], True):
            self.lava_tiles.append(Lava(self, lava['pos'], (self.assets[lava['type']][0].get_width(), self.assets[lava['type']][0].get_height())))

        for fire_trap in self.tilemap.extract([('Fire_Trap', 0)]):
            self.fire_traps.append(Fire_Trap(self, fire_trap['pos'], (29, 22)))

    def Update(self):
        for spike in self.spikes:
            spike.Update()

        for spike_poison in self.spikes_poison:
            spike_poison.Update()

        for bear_trap in self.bear_traps:
            bear_trap.Update()

        for spike_pit in self.spike_pits:
            spike_pit.Update()

        for top_pusher in self.top_pushers:
            top_pusher.Update()

        for lava in self.lava_tiles:
            lava.Update()

        for fire_trap in self.fire_traps:
            fire_trap.Update()

    def Render(self, offset = (0,0)):
        for spike in self.spikes:
            spike.Render(self.display, 'spike', offset)
        
        for spike_poison in self.spikes_poison:
            spike_poison.Render(self.display, 'spike_poison', offset)

        for bear_trap in self.bear_traps:
            bear_trap.Render(self.display, 'BearTrap', offset)

        for spike_pit in self.spike_pits:
            spike_pit.Render(self.display, 'PitTrap', offset)
        
        for top_pusher in self.top_pushers:
            top_pusher.Render(self.display, 'TopPush', offset)

        for lava in self.lava_tiles:
            lava.Render(self.display, 'Lava', offset)
        
        for fire_trap in self.fire_traps:
            fire_trap.Render(self.display, 'Fire_Trap', offset)
