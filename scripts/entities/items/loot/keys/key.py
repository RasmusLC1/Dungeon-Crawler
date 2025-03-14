from scripts.entities.items.loot.interactive_loot import Interactive_Loot

class Key(Interactive_Loot):
    def __init__(self, game, type, pos):
        super().__init__(game, type, pos, 64, (16, 16), 'key')


    # The update function in the inventory
    def Update_In_Inventory(self):
        if not super().Update_In_Inventory():
            return False
        
        nearby_decorations = self.game.decoration_handler.Find_Nearby_Decorations(self.game.player.pos, 4)

        # Filter for doors
        doors = [decoration for decoration in nearby_decorations if 'door' in decoration.type]
        mouse = self.game.mouse

        # Iterate over doors and check for collision
        for door in doors:
            if not door.rect().colliderect(mouse.rect_pos()):
                continue
            
            door.Set_Highlight()
            if not mouse.left_click:
                continue
            door.Open()
            self.Open_Door()

    # Effect of opening door on key
    def Open_Door(self):
        pass

