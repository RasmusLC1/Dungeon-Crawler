import re

class Mixed_Symbols():
    def __init__(self, game, symbols, font):
        self.game = game
        self.font = font
        self.symbols = symbols

    def parse_mixed_elements(self, input_str):
        parts = re.split(r'(\s+)', input_str)
        elements = []
        current_text = ''

        for part in parts:
            if not part:
                continue
            if part.isspace():
                current_text += part
            else:
                if self.symbols.Check_If_Symbol_Exist(part.lower()):
                    if current_text:
                        elements.append({'type': 'text', 'content': current_text})
                        current_text = ''
                    elements.append({'type': 'symbol', 'content': part})
                else:
                    current_text += part

        if current_text:
            elements.append({'type': 'text', 'content': current_text})
        return elements

    def Render_Mixed_Text(self, surf, input_str, pos, alpha_level=0, scale=1):
        elements = self.parse_mixed_elements(input_str)
        current_x, current_y = pos
        for element in elements:
            if element['type'] == 'text':
                self.font.Render_Word(surf, element['content'], (current_x, current_y), alpha_level, self.font)
                # Update x position based on number of characters (14 pixels per character)
                current_x += 14 * len(element['content'])
            elif element['type'] == 'symbol':
                # Render the symbol and update x position
                self.symbols.Render_Symbol(surf, element['content'], (current_x, current_y), scale)
                current_x += 16 * scale  # Assuming each symbol is 16 pixels wide, scaled
            
            