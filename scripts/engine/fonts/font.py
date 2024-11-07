import pygame

class Font():
    def __init__(self, game):
        self.game = game
        self.font = self.game.assets['font']
        self.player_damage_font = self.game.assets['player_damage_font']
        self.font_lookup = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '-', '+', ':','!', '_', ' ']



    def find_char_positions(self, input_string):
        # Convert input_string to lowercase to handle case-insensitivity
        characters = list(input_string.lower())  
        
        # List to store the positions of the characters in font_lookup
        char_positions = []

        
        # Iterate over each character in the input string
        for char in characters:
            # Append the position to the list
            if char in self.font_lookup:
                
                position = self.font_lookup.index(char)
                char_positions.append(position)  
            else:  # Append None if no char is found
                print("Char position not found", char)
                char_positions.append(None) 
        
        return char_positions

    # Find the appropriate Font
    def Find_Font(self, font_style):
        if font_style == 'default':
            return self.font
        elif font_style == 'player_damage':
            return self.player_damage_font
        else:
            return self.font

    # Render word by rendering characters in order
    def Render_Word(self, surf, text, pos, alpha_level = 0, font_style = 'default',):
        
        # Get the positions of the characters in font_lookup
        char_positions = self.find_char_positions(text)

        if not char_positions:
            return
        font = self.Find_Font(font_style)
        
        # Iterate over the list of positions to render each character
        for i, font_position in enumerate(char_positions):

            try:
                item_image = font[font_position].convert_alpha()

                # Set alpha value for fadeout
                if alpha_level:
                    alpha_value = max(0, min(255, 255 - alpha_level))
                    item_image.set_alpha(alpha_value)

                surf.blit(item_image, pos)
                pos = (pos[0] + 14, pos[1])
            except Exception as e:
                print(f"WRONG SYMBOL: {e}")
            
