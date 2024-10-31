import math
import pygame
import random

class Boss_Room():
    def __init__(self, game, pos, radius, level) -> None:
        self.game = game
        self.type = 'boss_room'
        self.category = 'decoration'
        self.ID = random.randint(1, 100000)

        self.pos = pos
        self.boss = None
        self.radius = radius
        self.level = level
        self.shrine = None
        self.distance_cooldown = 0
        self.activated = False
        self.saved_data = {}
        self.boss_defeated = False


    def Save_Data(self):
        self.saved_data['category'] = self.category
        self.saved_data['type'] = self.type
        self.saved_data['ID'] = self.ID
        self.saved_data['pos'] = self.pos
        self.saved_data['radius'] = self.radius
        self.saved_data['level'] = self.level
        self.saved_data['activated'] = self.activated
        self.saved_data['boss_defeated'] = self.boss_defeated
        self.saved_data['size'] = (0, 0)
        self.saved_data['boss_ID'] = 0
        if self.boss:
            self.saved_data['boss_ID'] = self.boss.ID

        

    
    def Load_Data(self, data):
        self.category = data['category']
        self.type = data['type']
        self.ID = data['ID']
        self.pos = data['pos']
        self.radius = data['radius']
        self.level = data['level']
        self.activated = data['activated']
        self.boss_defeated = data['boss_defeated']
        if self.activated:
            self.Close_Room()

        boss_ID = data['boss_ID']
        if boss_ID > 0:
            self.boss = self.game.enemy_handler.Find_Enemy(boss_ID)

        if self.boss_defeated:
            self.Open_Room()



    def Update(self):
        if self.boss_defeated:
            return
        if self.Calculate_Distance():
            self.Spawn_Boss()
            self.activated = True

        if not self.activated:
            return
        
        if not self.boss:
            return

        if self.boss.health <= 0:
            self.boss = None
            self.Open_Room()
            self.boss_defeated = True
            self.activated = False
            self.game.decoration_handler.Spawn_Shrine(self.pos)
    
    # Spawn boss
    # Close Doors and replace with walls
    def Spawn_Boss(self):
        # Spawn Temp decrepit bones
        # TODO: REPLACE WITH BOSS MOB
        self.boss = self.game.enemy_handler.Enemy_Spawner(
            'decrepit_bones_melee',
            self.pos,
        )
        self.Close_Room()
        self.Spawn_Torches()
        # Replace Entrances with walls to lock in player
    
    # Replace doors with walls when player enters
    def Close_Room(self):
        x = self.pos[0] // 16
        y = self.pos[1] // 16
        self.game.tilemap.tilemap[str(x - self.radius) + ';' + str(y)] = {'type': 'LeftWall', 'variant': 0, 'pos': (x - self.radius, y), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x + self.radius) + ';' + str(y)] = {'type': 'RightWall', 'variant': 0, 'pos': (x + self.radius, y), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x) + ';' + str(y - self.radius)] = {'type': 'TopWall', 'variant': 0, 'pos': (x, y - self.radius), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x) + ';' + str(y + self.radius)] = {'type': 'BottomWall', 'variant': 0, 'pos': (x, y + self.radius), 'active': 0, 'light': 0}

    # Open room by removing walls after player defeats boss
    def Open_Room(self):
        x = self.pos[0] // 16
        y = self.pos[1] // 16
        self.game.tilemap.tilemap[str(x - self.radius) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x - self.radius, y), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x + self.radius) + ';' + str(y)] = {'type': 'Floor', 'variant': 0, 'pos': (x + self.radius, y), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x) + ';' + str(y - self.radius)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y - self.radius), 'active': 0, 'light': 0}
        self.game.tilemap.tilemap[str(x) + ';' + str(y + self.radius)] = {'type': 'Floor', 'variant': 0, 'pos': (x, y + self.radius), 'active': 0, 'light': 0}


    # Spawn torches around the doors when the player enters
    def Spawn_Torches(self):

        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] - self.radius * 16 + 16, self.pos[1] + 16)) # Left top
        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] - self.radius * 16 + 16, self.pos[1] - 16)) # Left bottom

        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] + self.radius * 16 - 16, self.pos[1] + 16)) # Right top
        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] + self.radius * 16 - 16, self.pos[1] - 16)) # Right bottom

        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] - 16, self.pos[1] - self.radius * 16 + 16)) # top Left
        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] + 16, self.pos[1] - self.radius * 16 + 16)) # top Right

        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] - 16, self.pos[1] + self.radius * 16 - 16)) # Bottom Left
        self.game.item_handler.Spawn_Weapon('torch', (self.pos[0] + 16, self.pos[1] + self.radius * 16 - 16)) # Bottom Right

    def Calculate_Distance(self):
        if self.activated:
            return
        
        if self.distance_cooldown > 0:
            self.distance_cooldown -= 1
            return False
        
        # Calculate distance and set the cooldown to the distance to avoid computation
        distance = math.sqrt((self.game.player.pos[0] - self.pos[0]) ** 2 + (self.game.player.pos[1] - self.pos[1]) ** 2)        
        self.distance_cooldown = distance // 10
        # print(distance)
        if distance < self.radius * 12:
            return True
        
        return False
    
    # rect function for compatability
    def rect(self):
        return pygame.Rect(999999, 999999, 1, 1)