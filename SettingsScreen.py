import pygame
from buttons import *
from colors import *
import random
from game import *

window_x = 720
window_y = 480

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

class SettingsScreen:
    def __init__(self, screen_width, screen_height, quit_screen):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.settings = []
        self.is_settings_open = False
        self.quit_screen = quit_screen
        self.init_settings()

    def init_settings(self):
        spacing = 0
        font = pygame.font.Font(None, 36)

        label_nickname = Text(130, 35, "Nickname:", white)
        nickname_input = TextInput(
            130 + label_nickname.get_width() + 35, 35, 200, label_nickname.get_height(), font, Dark_gray, Light_goldenrod_yellow, 50, True)

        spacing = label_nickname.get_height() + 65

        label_speed = Text(130, spacing, "Speed:", white)
        speed_slider = Slider(130 + label_speed.get_width() + 35, spacing, 200, label_speed.get_height(), 10, 50, 20,
                              Light_goldenrod_yellow, light_sea_blue, self.speed_changed)

        spacing += label_speed.get_height() + 35

        label_size = Text(130, spacing, "Size:", white)
        size_slider = Slider(130 + label_size.get_width() + 35, spacing, 200, label_size.get_height(), 15, 35, 25,
                             Light_goldenrod_yellow, light_sea_blue, self.size_changed)

        spacing += label_size.get_height() + 35

        label_controls = Text(130, spacing, "Controls:", white)
        label_player_one = Text(
            130 + label_controls.get_width() + 35, spacing - 20, "Player 1 :", Light_gray, 15)
        label_player_two = Text(
            130 + label_controls.get_width() + 200, spacing - 20, "Player 2 :", Light_gray, 15)
        label_player_one.set_visibility(False)
        label_player_two.set_visibility(False)
        controls_buttons = [
            Button((130 + label_controls.get_width() + 35), spacing - 10, 150,
                   label_controls.get_height() + 15, "Arrow Keys", black, Light_goldenrod_yellow, self.arrow_keys_pressed),
            Button(130 + label_controls.get_width() + 200, spacing - 10, 130,
                    label_controls.get_height() + 15, "WASD", black,
                    light_sea_blue, self.wasd_pressed,None)
        ]

        spacing += label_controls.get_height() + 35

        label_two_player = Text(130, spacing, "Two player mode:", white)
        two_player_checkbox = Checkbox(
            130 + label_two_player.get_width() + 35, spacing - label_two_player.get_height() * 0.1, label_two_player.get_height() * 1.25, label_two_player.get_height() * 1.25, Light_goldenrod_yellow, light_sea_blue, self.two_player_toggle)

        spacing += label_two_player.get_height() + 35

        color_picker_p1 = ColorPicker(
            self.screen_width - 50, self.screen_height - 50, 40, 40, green, self.color_picker_changed)
        color_picker_p2 = ColorPicker(
            self.screen_width - 100, self.screen_height - 50, 40, 40, Teal, self.color_picker2_changed)
        color_picker_p2.set_visibility(False)

        start = Button(self.screen_width / 2, self.screen_height -
                       60, 60, 50, "Start", black, Light_goldenrod_yellow, self.start_game,light_green)
        quit_game = Button(self.screen_width / 2 - 70, self.screen_height -
                           60, 60, 50, "Quit", black, Light_goldenrod_yellow, self.quit_settings,Indian_red)
        start.active = True
        quit_game.active = True
        # Add other settings similarly

        self.settings = [
            (label_nickname, nickname_input),
            (label_speed, speed_slider),
            (label_size, size_slider),
            (label_player_one, label_player_two),
            (label_controls, SettingsGroup(0, 0, controls_buttons)),
            (label_two_player, two_player_checkbox),
            (None, color_picker_p1),
            (None, color_picker_p2),
            (None, start),
            (None, quit_game)
            # Add other settings similarly
        ]

    def update_setting_visibility(self, target_setting, is_visible):
        for label, setting in self.settings:
            if setting == target_setting:
                setting.set_visibility(is_visible)
                break

    def draw(self, surface):
        self.is_settings_open = True
        for label, setting in self.settings:
            if label:
                label.draw(surface)
            if setting:
                setting.draw(surface)

    def handle_event(self, event):
        for label, setting in self.settings:
            if setting:
                setting.handle_event(event)

    def speed_changed(self, slider):
        print("Speed changed:", slider.value)
        # Handle speed change logic here

    def size_changed(self, slider):
        print(f"Size changed: {slider.value}")

    def arrow_keys_pressed(self, button):
        _, setting = self.settings[4]
        setting.active_button = button

    def wasd_pressed(self, button):
        _, setting = self.settings[4]
        setting.active_button = button

    def two_player_toggle(self, checkbox):
        _, nickname = self.settings[0]
        p1, p2 = self.settings[3]
        _, group = self.settings[4]
        _, setting = self.settings[7]
        if checkbox.checked:
            nickname.clickable = False
            nickname.active = False
            for button in group.buttons:
                button.active = False
            setting.set_visibility(True)
            p1.set_visibility(True)
            p2.set_visibility(True)
        else:
            nickname.clickable = True
            nickname.active = True
            for button in group.buttons:
                button.active = True
            setting.set_visibility(False)
            p1.set_visibility(False)
            p2.set_visibility(False)

    def color_picker_changed(self, color_picker):
        _, color_picker2 = self.settings[7]
        available_colors = [
            color for color in colors if color != color_picker2.color]
        color_picker.color = random.choice(available_colors)

    def color_picker2_changed(self, color_picker):
        _, color_picker1 = self.settings[6]
        available_colors = [
            color for color in colors if color != color_picker1.color]
        color_picker.color = random.choice(available_colors)

    def start_game(self, start):
        _, nickname = self.settings[0]
        _, speed = self.settings[1]
        _, size = self.settings[2]
        #_, controls_buttons = self.settings[4]
        _, two_player = self.settings[5]
        _, color_p1 = self.settings[6]
        _, color_p2 = self.settings[7]
        if two_player.checked:
            pass
        else:
            oneplayer(change_to,direction,fruit_position,fruit_spawn,speed.value,score,snake_position,snake_body,size.value,color_p1.color,two_player.checked,change_to2,direction2,score2,snake_position2,snake_body2,color_p2.color)
    
    def quit_settings(self, quiter):
        self.quit_screen()
