class Font():
    def __init__(self, game):
        self.game = game
        self.font = self.game.assets['font']
        self.player_damage_font = self.game.assets['player_damage_font']

        # Use dictionary for O(1) lookup time, using enumerate to number them
        self.font_lookup_table = {
            **{char: index for index, char in enumerate(
                [*map(chr, range(97, 123)),  # a-z
                *map(str, range(10)),       # 0-9
                '-', '+', ':', '!', '_', '/', ' ', '\n']
            )}
        }


    def find_char_positions(self, input_string):
        input_string = input_string.lower()  

        # Use list comprehension for optimisation and check that the char is in the dictionary
        char_positions = [
            self.font_lookup_table[char] if char in self.font_lookup_table else None
            for char in input_string
        ]
        
        return char_positions


    def Find_Font(self, font_style):
        font_styles = {
        'default': self.font,
        'player_damage': self.player_damage_font,
        }
        return font_styles.get(font_style, self.font)


    def Render_Word(self, surf, text, pos, font_style='default'):
        line_height = 16  # Adjust based on your font's line height
        original_x, original_y = pos
        current_y = original_y
        font = self.Find_Font(font_style)

        # Split by newline and then process each line
        lines = text.split('\n')

        for line in lines:
            words = line.split()  # Split the line into words
            chunks = [words[i:i+2] for i in range(0, len(words), 2)]  # Group words into chunks
            current_x = original_x  # Reset x for each line

            for chunk in chunks:
                line_text = ' '.join(chunk)
                char_positions = self.find_char_positions(line_text)
                self.Render_Chunk(surf, current_x, current_y, char_positions, font)
                current_x += len(line_text) * 14  # Adjust spacing if needed

            current_y += line_height  # Move to the next line


    def Render_Chunk(self, surf, current_x, current_y, char_positions, font):
        for font_position in char_positions:
            if font_position is None:
                continue  # Skip characters not found in font_lookup
            try:
                surf.blit(font[font_position], (current_x, current_y))
                current_x += 14  # Increment x position for next character
            except Exception as e:
                print(f"WRONG SYMBOL FONT: {e}")