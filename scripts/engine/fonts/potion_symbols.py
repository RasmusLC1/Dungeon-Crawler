import pygame

class Potion_Symbols():
    def __init__(self, game):
        self.game = game
        self.potion_symbols = self.game.assets['potion_symbols']
        self.potion_symbols_lookup = ['health', 'strength', 'movement',
                                      'soul', 'poison', 'invisibility',
                                      'fire', 'ice', 'hardness',
                                      'regen', 'silence', 'luck',
                                      'vampiric']

    def find_symbol_position(self, input_string):
    
        if input_string.lower() in self.potion_symbols_lookup:
            position = self.potion_symbols_lookup.index(input_string)
            return position

        return None

    def Render_Symbol(self, surf, text, pos):
        # Get the positions of the characters in font_lookup
        symbol_position = self.find_symbol_position(text)

        # Iterate over the list of positions to render each character
        item_image = self.potion_symbols[symbol_position]
        surf.blit(item_image, pos)
