import pygame
from scripts.engine.assets.keys import keys

class Symbols():
    def __init__(self, game):
        self.game = game
        self.symbols = self.game.assets[keys.symbols]
        # Use dictionary for O(1) lookup time, using enumerate to number them
        self.symbols_lookup = {
            symbol: index for index, symbol in enumerate([
                keys.healing, 'increase_strength', keys.speed,
                'soul', keys.invisibility,
                'slash', 'blunt', keys.electric,
                keys.resistance, keys.regen, keys.silence,
                'luck', keys.vampiric, keys.fire,
                keys.frozen, keys.poison, keys.wet,
                'block', keys.fire_resistance,
                keys.frozen_resistance, keys.poison_resistance,
                keys.power, keys.gold, 'range', 'key',
                keys.arcane_conduit, keys.magnet, keys.arcane_hunger, 
                keys.invulnerable, keys.snare, keys.thorns,
                keys.electric_resistance,
                'chain', keys.enemy, keys.curse,
                keys.weakness, 'vulnerable', 'luck',
                'anchor', keys.blood_tomb, keys.halo,
                keys.demonic_bargain, keys.temptress_embrace,
                'slow',
            ])
        }

    def Check_If_Symbol_Exist(self, symbol):
        return symbol in self.symbols_lookup


    def find_symbol_position(self, input_string):
        effect = input_string
        
        if effect.lower() in self.symbols_lookup:
            position = self.symbols_lookup.get(effect)
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
            print(f'WRONG Symbol INPUT {e}', text, pos, symbol_position)