import pygame
from buttons import *
from colors import *
import random


class SettingsScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.settings = []
        self.is_settings_open = False
        self.init_settings()

    def init_settings(self):
        spacing = 0
        font = pygame.font.Font(None, 36)

        label_nickname = Text(130, 35, "Nickname:", white)
        nickname_input = TextInput(
            130 + label_nickname.get_width() + 35, 35, 200, label_nickname.get_height(), font, white, Tan, 50)

        spacing = label_nickname.get_height() + 65

        label_speed = Text(130, spacing, "Speed:", white)
        speed_slider = Slider(130 + label_speed.get_width() + 35, spacing, 200, label_speed.get_height(), 10, 50, 20,
                              red, green, self.speed_changed)

        spacing += label_speed.get_height() + 35

        label_size = Text(130, spacing, "Size:", white)
        size_slider = Slider(130 + label_size.get_width() + 35, spacing, 200, label_size.get_height(), 15, 35, 25,
                             purple, yellow, self.size_changed)

        spacing += label_size.get_height() + 35

        label_controls = Text(130, spacing, "Controls:", white)
        controls_buttons = [
            Button(130 + label_controls.get_width() + 35, spacing - 10, 150, label_controls.get_height() + 15, "Arrow keys", white,
                   blue, self.arrow_keys_pressed),
            Button(130 + label_controls.get_width() + 200, spacing - 10, 130,
                   label_controls.get_height() + 15, "WASD", white, baby_blue, self.wasd_pressed)
        ]

        spacing += label_controls.get_height() + 35

        label_two_player = Text(130, spacing, "Two player mode:", white)
        two_player_checkbox = Checkbox(
            130 + label_two_player.get_width() + 35, spacing - label_two_player.get_height() * 0.1, label_two_player.get_height() * 1.25, label_two_player.get_height() * 1.25, "", white, dark_green, self.two_player_toggle)

        spacing += label_two_player.get_height() + 35

        label_color_picker_p1 = Text(130, spacing, "Color :", white)
        color_picker_p1 = ColorPicker(
            130 + label_color_picker_p1.get_width() + 35, spacing - 7, 40, 40, green, self.color_picker_changed)

        # Add other settings similarly

        self.settings = [
            (label_nickname, nickname_input),
            (label_speed, speed_slider),
            (label_size, size_slider),
            (label_controls, SettingsGroup(0, 0, controls_buttons)),
            (label_two_player, two_player_checkbox),
            (label_color_picker_p1, color_picker_p1),
            # Add other settings similarly
        ]

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
        print("Arrow keys pressed")
        # Add your logic for handling arrow keys button press here

    def wasd_pressed(self, button):
        print("WASD pressed")
        # Add your logic for handling WASD button press here

    def two_player_toggle(self, checkbox):
        print("Two player mode:", checkbox.checked)

    def color_picker_changed(self, color_picker):
        color_picker.color = random.choice(colors)
