import pygame
import sys

def get_image(sheet, x, y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (x, y, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

# Initialize Pygame
pygame.init()

# Load the sprite sheet
sprite_sheet = pygame.image.load('dungeon_.png')

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Sprite Sheet Example')

# Define the coordinates and size of the specific sprite
# Assuming the sprite starts at (x, y) and is 32x32 pixels
x, y = 80, 112  # Modify these values based on the exact location of the sprite
sprite_width = 17
sprite_height = 17
sprite_scale = 2
sprite_color_key = (0, 0, 0)  # Assuming black is the color key

# Get the specific sprite
sprite = get_image(sprite_sheet, x, y, sprite_width, sprite_height, sprite_scale, sprite_color_key)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear screen
    screen.fill((0, 0, 0))
    
    # Draw the specific sprite
    screen.blit(sprite, (100, 100))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
