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

    def Save_Data(self):
        self.game.player.Save_Data()
        self.game.item_handler.Save_Item_Data()



    def Load_Data_Structure(self):
        self.entities_to_load = [self.game.player,
                                self.game.item_handler,
                                # self.game.light_handler,
                                # self.game.tilemap,
                                # self.game.enemy_handler,
                                # self.game.trap_handler,
                                # self.game.chest_handler,
                                # self.game.door_handler,
                                # self.game.rune_handler,
                                ]
        
        self.entities_to_load_names = ['player',
                                    'item_handler',
                                    #  'light_handler',
                                    #  'tilemap',
                                    #  'enemy_handler',
                                    # 'trap_handler',
                                    # 'chest_handler',
                                    # 'door_handler',
                                    # 'rune_handler',
                                    ]
        self.Load_Game_Data()
        


    def Save_Data_Structure(self):
        self.Save_Data()

        self.data_structures = [self.game.player.saved_data,
                                self.game.item_handler.saved_data,
                                # self.game.tilemap,
                                # self.game.enemy_handler,
                                # self.game.trap_handler,
                                # self.game.chest_handler,
                                # self.game.light_handler.saved_data,
                                # self.game.door_handler,
                                # self.game.rune_handler,
                                ]
        
        self.data_structure_names = ['player',
                                    'item_handler',
                                    #  'light_handler',
                                    #  'tilemap',
                                    #  'enemy_handler',
                                    # 'trap_handler',
                                    # 'chest_handler',
                                    # 'door_handler',
                                    # 'rune_handler',
                                    ]

        self.Save_Game_Data()