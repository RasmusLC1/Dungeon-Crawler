from scripts.traps.spike import Spike
from scripts.traps.bear_trap import Bear_Trap
from scripts.traps.spike_pit import Spike_Pit
from scripts.traps.top_push_trap import Top_Push_Trap



class Trap_Handler:
    def __init__(self):
        self.spikes = []
        self.bear_traps = []
        self.spike_pits = []
        self.top_pushers = []
        # Spawner initialisation
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']

        # Spike initialisation
        for spike_tile in self.tilemap.extract([('spike', 0)], True):
            self.spikes.append(Spike(self, spike_tile['pos'], (self.assets[spike_tile['type']][0].get_width(), self.assets[spike_tile['type']][0].get_height())))
        
        # top pusher initialisation
        for top_push in self.tilemap.extract([('TopPush', 0)]):
            self.top_pushers.append(Top_Push_Trap(self, top_push['pos'], (self.assets[top_push['type']][0].get_width(), self.assets[top_push['type']][0].get_height())))

        # Bear Trap initialisation
        for trap in self.tilemap.extract([('BearTrap', 0)]):
            self.bear_traps.append(Bear_Trap(self, trap['pos'], (10, 5)))

        # Spike pit initialisation
        for spike_pit in self.tilemap.extract([('PitTrap', 0)], True):
            self.spike_pits.append(Spike_Pit(self, spike_pit['pos'], (self.assets[spike_pit['type']][0].get_width(), self.assets[spike_pit['type']][0].get_height())))

    def Update(self):
        for spike in self.spikes:
            spike.Update()

        for bear_trap in self.bear_traps:
            bear_trap.Update()

        for spike_pit in self.spike_pits:
            spike_pit.Update()

        for top_pusher in self.top_pushers:
            top_pusher.Update()

    def Render(self, offset = (0,0)):
        for spike in self.spikes:
            spike.Render(self.display, 'spike', offset)

        for bear_trap in self.bear_traps:
            bear_trap.Render(self.display, 'BearTrap', offset)

        for spike_pit in self.spike_pits:
            spike_pit.Render(self.display, 'PitTrap', offset)
        
        for top_pusher in self.top_pushers:
            top_pusher.Render(self.display, 'TopPush', offset)
