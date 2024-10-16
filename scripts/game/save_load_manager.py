import pickle
import os
import pygame

class Save_Load_Manager():
    def __init__(self, game, file_extension, save_folder):
        self.game = game
        self.file_extension = file_extension
        self.save_folder = save_folder
        self.data_structures = []
        self.entities_to_load = []
        self.data_structure_names = []

    def save_data(self, data, name):
        data_file = open(self.save_folder+"/"+name+self.file_extension, "wb")
        pickle.dump(data, data_file)

    def Load_Data(self, name, entity):
        data_file = open(self.save_folder+"/"+name+self.file_extension, "rb")
        data = pickle.load(data_file)
        entity.Load_Data(data)

        

    def check_for_file(self, name):
        return os.path.exists(self.save_folder+"/"+name+self.file_extension)

    def Load_Game_Data(self):
        for index, entity in enumerate(self.entities_to_load):
            self.Load_Data(self.entities_to_load_names[index], entity)

    def Save_Game_Data(self):
        for index, file in enumerate(self.data_structures):
            self.save_data(file, self.data_structure_names[index])

    # Initialise the data that needs to be saved
    def Save_Data(self):
        self.game.player.Save_Data()
        self.game.item_handler.Save_Item_Data()
        self.game.chest_handler.Save_Chest_Data()
        self.game.door_handler.Save_Door_Data()
        self.game.trap_handler.Save_Trap_Data()
        self.game.enemy_handler.Save_Enemy_Data()
        self.Inventory_Save_Data()

    

    def Inventory_Save_Data(self):
        self.game.item_inventory.Save_Inventory_Data()
        self.game.rune_inventory.Save_Inventory_Data()
        self.game.weapon_inventory.Save_Inventory_Data()

    def Save_Data_Structure(self):
        self.Save_Data()

        self.data_structures = [self.game.player.saved_data,
                                self.game.item_handler.saved_data,
                                self.game.rune_handler.saved_data,
                                self.game.chest_handler.saved_data,
                                self.game.door_handler.saved_data,
                                self.game.trap_handler.saved_data,
                                self.game.enemy_handler.saved_data,
                                self.game.item_inventory.saved_data,
                                self.game.rune_inventory.saved_data,
                                self.game.weapon_inventory.saved_data,
                                ]
        
        self.data_structure_names = ['player',
                                    'item_handler',
                                    'rune_handler',
                                    'chest_handler',
                                    'door_handler',
                                    'trap_handler',
                                     'enemy_handler',
                                    'item_inventory',
                                    'rune_inventory',
                                    'weapon_inventory',
                                    ]

        self.Save_Game_Data()


    def Load_Data_Structure(self):
        self.entities_to_load = [self.game.player,
                                self.game.item_handler,
                                self.game.rune_handler,
                                self.game.chest_handler,
                                self.game.door_handler,
                                self.game.trap_handler,
                                self.game.enemy_handler,
                                self.game.item_inventory,
                                self.game.rune_inventory,
                                self.game.weapon_inventory,
                                ]
        
        self.entities_to_load_names = ['player',
                                    'item_handler',
                                    'rune_handler',
                                    'chest_handler',
                                    'door_handler',
                                    'trap_handler',
                                     'enemy_handler',
                                     'item_inventory',
                                    'rune_inventory',
                                    'weapon_inventory',
                                    ]
        self.Load_Game_Data()
        