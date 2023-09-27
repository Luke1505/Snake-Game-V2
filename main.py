import pygame
import colors
import sys
import random
import file
import settings
from buttons import *

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((settings.window_x, settings.window_y))

# Fonts
font = settings.font

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Open the settings menu when 's' key is pressed
                settings.settings_menu(screen)
    
    # Clear the screen
    screen.fill(colors.white)

    # Create a text for starting the game
    text = font.render("Press 'S' to open Settings", True, colors.black)
    screen.blit(text, (settings.window_x // 2 - text.get_width() // 2, settings.window_y // 2))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
