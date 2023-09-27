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

# Player 1 Standart Settings
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0

# Player 2 Standart Settings
snake_position2 = [100, 100]
snake_body2 = [[100, 100],
               [90, 100],
               [80, 100],
               [70, 100]
               ]
direction2 = 'RIGHT'
change_to2 = direction2
score2 = 0

# Game Standart Settings
snake_speed = 15
game_size = 10
fps = pygame.time.Clock()
nicknames = file.loadscore()
player = ""
Button = 1
counter = 0
active = 0
Multiplayer = False
color = colors.color
color2 = colors.color2
pycolor = pygame.Color(colors.green)
pycolor2 = pygame.Color(colors.cyan)

# Button colors
button_color = colors.green
button_hover_color = colors.Alice_blue

# Fonts
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# Create a function to display the settings menu
def settings_menu(screen):
    settings_screen = SettingsScreen(window_x, window_y)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            settings_screen.handle_event(event)

        screen.fill((0, 0, 0))
        settings_screen.draw(screen)
        pygame.display.flip()
