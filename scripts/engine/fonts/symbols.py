import pygame

class Symbols():
    def __init__(self, game):
        self.game = game
        self.symbols = self.game.assets['symbols']
        self.symbols_lookup = ['health', 'strength', 'speed',
                               'soul', 'invisibility',
                               'slash', 'blunt', 'electric',
                               'hardness', 'regen', 'silence',
                               'luck', 'vampiric', 'fire',
                               'freeze', 'poison', 'wet',
                               'block', 'fire_resistance',
                               'freeze_resistance', 'poison_resistance',
                               'power', 'gold', 'arrow']



    def find_symbol_position(self, input_string):
        effect = input_string
        
        if effect.lower() in self.symbols_lookup:
            position = self.symbols_lookup.index(effect)
            return position

        return None

    def Render_Symbol(self, surf, text, pos, scale = 1):
        # Get the positions of the characters in font_lookup
        try:
            symbol_position = self.find_symbol_position(text)

            # Iterate over the list of positions to render each character
            item_image = self.symbols[symbol_position]
            item_image = pygame.transform.scale(item_image, (16 * scale, 16 * scale))
            surf.blit(item_image, pos)
        except Exception as e:
            print(f'WRONG Symbol INPUT {e}', text, pos)