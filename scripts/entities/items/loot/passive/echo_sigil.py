from scripts.entities.items.loot.loot import Loot

class Echo_Sigil(Loot):
    def __init__(self, game, pos):
        super().__init__(game, 'echo_sigil', pos, (16, 16), 10, 'passive')
        self.update_cooldown = 0
        self.loot_IDs = []
        self.description = 'Grants\nextra use\nto items'


    def Update(self):
        if self.update_cooldown:
            self.update_cooldown -= 1
        else:
            self.update_cooldown = 100
            self.Check_Loot_In_Inventory()
            
            
        return super().Update()
    
    def Check_Loot_In_Inventory(self):
        inventory_loot = self.game.inventory.item_inventory.Find_Loot()

        for item in inventory_loot:
            if item.sub_category != 'loot':
                print("WRONG Item type added to Echo Sigil", item)
                continue
            if item.ID in self.loot_IDs:
                continue
            
            # Increase amount for multi use utility items by checking amount since
            # utility items shouldn't have more than 10 uses
            if item.max_amount > 1 and item.max_amount < 10:
                item.Increase_Amount(1)
            self.loot_IDs.append(item.ID)