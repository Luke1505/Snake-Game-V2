from SettingsScreen import SettingsScreen
from buttons import *
import pygame
import colors
import random
import file

# Initialize Pygame
pygame.init()

# Define settings
# Game Window size
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game - Settings")



# Fonts
font = pygame.font.Font(pygame.font.get_default_font(), 36)
running = True

def quit_game():
    global running
    running = False

# Create a function to display the settings menu
def settings_menu(screen):
    global running
    settings_screen = SettingsScreen(window_x, window_y,quit_game)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            settings_screen.handle_event(event)

        screen.fill((0, 0, 0))
        settings_screen.draw(screen)
        pygame.display.flip()
