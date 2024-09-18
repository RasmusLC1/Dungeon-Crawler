import pygame

class Damage_Symbols():
    def __init__(self, game):
        self.game = game
        self.damage_symbols = self.game.assets['damage_symbols']
        self.damage_symbols_lookup = [
                                    'slash', 'blunt', 'electric',
                                    'fire', 'ice', 'poison']



    def find_symbol_position(self, input_string):
    
        if input_string.lower() in self.damage_symbols_lookup:
            position = self.damage_symbols_lookup.index(input_string)
            return position

        return None

    def Render_Symbol(self, surf, text, pos):

        
        # Get the positions of the characters in font_lookup
        symbol_position = self.find_symbol_position(text)
        if not symbol_position:
            return
        
        # Iterate over the list of positions to render each character
        item_image = self.damage_symbols[symbol_position]
        surf.blit(item_image, pos)
