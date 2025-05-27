from scripts.entities.decoration.decoration import Decoration
import random
from scripts.engine.assets.keys import keys
import math

activation_radius = 200

class Hunter_Shrine(Decoration):
    def __init__(self, game, pos) -> None:
        super().__init__(game, keys.hunter_shrine, pos, (64, 64))
        self.description = "Return the\ntreasure for\nreward"
        self.cooldown = 0
        self.distance_to_player = 0
        self.max_animation = 2
        self.treasures = []



    def Update(self):
        self.Check_For_Treasure_Collision()
        return super().Update()
    
    def Open(self, generate_clatter=False):
        if self.empty:
            return False
        self.empty = True
        self.animation = 1
        self.Set_Sprite()
        self.Spawn_Treasure()
        return True


    
    def Spawn_Treasure(self):
        tile_size = self.game.tilemap.tile_size
        for i in range(3):
            tile = self.game.tilemap.Get_Random_Tile_With_Path_To_Player()
            if not tile:
                print("TILE NOT FOUND, HUNTER SHRINE")
                continue
            tile_pos = tile.pos[0] * tile_size, tile.pos[1] * tile_size
            treasure = self.game.item_handler.loot_handler.Spawn_Hunter_Treasure(tile_pos)
            if not treasure:
                print("Treasure not spawned, HUNTER SHRINE")
                return
            
            self.treasures.append(treasure)


    def Cooldown_Handler(self):
        if self.cooldown <= 0:
            self.cooldown = random.randint(40, 60)
            return True
        
        self.cooldown -= 1
        return False

    def Check_Player_Dis(self):
        player_pos = self.game.player.pos
        self.distance_to_player = math.sqrt((player_pos[0] - self.pos[0]) ** 2 + (player_pos[1] - self.pos[1]) ** 2)
        if self.distance_to_player > activation_radius:
            self.cooldown = self.distance_to_player * 2
            return False
        
        return True

    def Check_For_Treasure_Collision(self):
        if self.animation != 1:
            return False
        
        if not self.Cooldown_Handler():
            return
        
        if not self.Check_Player_Dis():
            return
        
        nearby_items = self.game.item_handler.Find_Nearby_Item(self.pos, 3)

        for item in nearby_items:
            if not item.type == keys.hunter_treasure:
                continue
            self.game.item_handler.Remove_Item(item, True)
            self.game.particle_handler.Activate_Particles(random.randint(8, 12), keys.soul_particle, self.rect().center, frame=random.randint(50, 70))
            self.Spawn_Reward()
            self.game.clatter.Generate_Clatter(self.pos, 500) # Generate clatter to alert nearby enemies
            self.game.sound_handler.Play_Sound('soul_well', 0.6)
            self.animation = 2
            self.Set_Sprite()
            self.treasures.clear()
            return True


    def Spawn_Reward(self):
        print("SPAWN REWARD")
        pass