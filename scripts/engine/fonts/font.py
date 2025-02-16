class Font():
    def __init__(self, game):
        self.game = game
        self.font = self.game.assets['font']
        self.player_damage_font = self.game.assets['player_damage_font']
        self.font_lookup = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '-', '+', ':', '!', '_', ' '
        ]

    def find_char_positions(self, input_string):
        characters = list(input_string.lower())  
        char_positions = []
        spaces = 0  # Initialize spaces counter

        for char in characters:
            if char == ' ':
                spaces += 1
            if char in self.font_lookup:                
                position = self.font_lookup.index(char)
                char_positions.append(position)  
            else:
                print("Char position not found", char)
                char_positions.append(None) 
        
        return char_positions, spaces

    def Find_Font(self, font_style):
        if font_style == 'default':
            return self.font
        elif font_style == 'player_damage':
            return self.player_damage_font
        else:
            return self.font

    def Render_Word(self, surf, text, pos, alpha_level=0, font_style='default'):
        # Split the text into words, handling any whitespace
        words = text.split()
        # Split into chunks of up to 5 words each
        chunks = [words[i:i+2] for i in range(0, len(words), 2)]
        line_height = 16  # Adjust based on your font's line height
        original_x, original_y = pos
        current_y = original_y

        for chunk in chunks:
            line_text = ' '.join(chunk)
            char_positions, _ = self.find_char_positions(line_text)
            font = self.Find_Font(font_style)
            current_x = original_x  # Reset x for each line

            for font_position in char_positions:
                if font_position is None:
                    continue  # Skip characters not found in font_lookup
                try:
                    item_image = font[font_position].convert_alpha()
                    if alpha_level:
                        alpha_value = max(0, min(255, 255 - alpha_level))
                        item_image.set_alpha(alpha_value)
                    surf.blit(item_image, (current_x, current_y))
                    current_x += 14  # Increment x position for next character
                except Exception as e:
                    print(f"WRONG SYMBOL FONT: {e}")

            current_y += line_height  # Move to the next line after rendering the chunk