import pygame

# Base class for all settings
class Setting:
    def __init__(self, x, y):
        self.x, self.y, self.visible = x, y, True
        self.deactivated_color = (180, 180, 180)

    def draw(self, surface):
        if self.visible:
            pass  # Draw method to be overridden by subclasses

    def update(self, surface):
        pass

    def handle_event(self, event):
        pass

    def set_visibility(self, visible):
        self.visible = visible


# Button setting
class Button(Setting):
    def __init__(self, x, y, width, height, text, text_color, button_color, action, outline_color=None):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
        self.outline_color = outline_color  # Optional outline color
        self.action = action
        self.clicked = False
        self.active = True  # Assuming the button is active by default

    def draw(self, surface):
        super().draw(surface)
        if self.visible:
            # Draw the button rectangle
            color = self.button_color if self.active else self.deactivated_color
            pygame.draw.rect(surface, color, self.rect)

            # Render and display the text with optional outline
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)

            if self.outline_color:
                # Draw the text with an outline
                outline_surface = font.render(self.text, True, self.outline_color)
                surface.blit(outline_surface, text_rect.move(1, 0))  # Move 1 pixel to the right
                surface.blit(outline_surface, text_rect.move(-1, 0))  # Move 1 pixel to the left
                surface.blit(outline_surface, text_rect.move(0, 1))  # Move 1 pixel down
                surface.blit(outline_surface, text_rect.move(0, -1))  # Move 1 pixel up

            # Draw the main text
            surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if self.visible and self.active and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is inside the button's rectangle
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if self.action:
                    self.action(self)

    def reset(self):
        self.clicked = False


# TextInput setting
class TextInput(Setting):
    def __init__(self, x, y, width, height, font, text_color, background_color, max_length=None, clickable=True):
        super().__init__(x, y)
        self.rect, self.font, self.text_color, self.background_color = pygame.Rect(
            x, y, width, height), font, text_color, background_color
        self.text, self.max_length, self.active, self.cursor_visible, self.cursor_timer = "", max_length, True, False, 0
        self.cursor_blink_interval = 500
        self.ignore_first_keyup = False  # Flag to ignore the first KEYUP event
        self.clickable = clickable  # New attribute to control clickability

    def handle_event(self, event):
        if self.visible and self.clickable:  # Check clickable attribute
            if event.type == pygame.KEYDOWN:
                if self.active:
                    # Pressed key
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                        self.ignore_first_keyup = True
                    elif event.key == pygame.K_RETURN:
                        self.active = False
                    elif (self.max_length is None or len(self.text) < self.max_length) and event.unicode.isalnum():
                        new_text = self.text + event.unicode
                        text_width, _ = self.font.size(new_text)
                        if text_width <= self.rect.width:
                            self.text = new_text
                            self.ignore_first_keyup = True

    def update(self, surface):
        if self.active:
            current_time = pygame.time.get_ticks()
            if current_time - self.cursor_timer >= self.cursor_blink_interval:
                self.cursor_visible = not self.cursor_visible
                self.cursor_timer = current_time

    def draw(self, surface):
        super().draw(surface)
        if self.visible:
            # Draw the background rectangle with rounded corners
            pygame.draw.rect(surface, self.background_color, self.rect, border_radius=5)

            # Draw the single centered bar
            bar_height = 3
            bar_width = self.rect.width - 10
            bar_rect = pygame.Rect(self.rect.x + 5, self.rect.bottom - bar_height - 2, bar_width, bar_height)
            pygame.draw.rect(surface, (0, 0, 0), bar_rect, border_radius=1)

            # Render and display the text
            text_surface = self.font.render(self.text, True, self.text_color)
            surface.blit(text_surface, (self.rect.x, self.rect.y))

            # Draw the blinking cursor when active
            if self.active and self.cursor_visible:
                cursor_x = self.rect.x + text_surface.get_width()
                cursor_height = text_surface.get_height()
                pygame.draw.rect(surface, self.text_color, (cursor_x, self.rect.y, 2, cursor_height))

    def set_visibility(self, visible):
        super().set_visibility(visible)
        if not visible:
            self.active = False  # Set active to False when making the TextInput invisible

# Checkbox setting
class Checkbox(Setting):
    def __init__(self, x, y, width, height, text_color, fill_color, callback=None):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.text_color = text_color
        self.fill_color = fill_color
        self.checked = False
        self.callback = callback

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
                if self.callback:
                    self.callback(self)

    def draw(self, surface):
        super().draw(surface)
        if self.checked:
            pygame.draw.rect(surface, self.fill_color, self.rect, 2)

            # Calculate the center of the checkbox
            center_x = self.rect.centerx
            center_y = self.rect.centery

            # Draw a symmetrical X centered in the box
            x_length = min(self.rect.width, self.rect.height) // 2 - 5
            pygame.draw.line(surface, self.fill_color, (center_x - x_length, center_y - x_length),
                             (center_x + x_length, center_y + x_length), 4)
            pygame.draw.line(surface, self.fill_color, (center_x - x_length, center_y + x_length),
                             (center_x + x_length, center_y - x_length), 4)
        else:
            pygame.draw.rect(surface, self.text_color, self.rect, 2)

# Slider setting
class Slider(Setting):
    def __init__(self, x, y, width, height, min_value, max_value, default_value, slider_color, handle_color, action):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.min_value, self.max_value, self.value = min_value, max_value, default_value
        self.slider_color, self.handle_color = slider_color, handle_color
        self.action = action
        self.dragging = False

    def draw(self, surface):
        super().draw(surface)
        if self.visible:
            # Draw the slider bar with rounded corners
            pygame.draw.rect(surface, self.slider_color, self.rect, border_radius=10)
            # Calculate handle position
            handle_width = int((self.value - self.min_value) /
                               (self.max_value - self.min_value) * self.rect.width)
            handle_rect = pygame.Rect(
                self.rect.x, self.rect.y, handle_width, self.rect.height)
            # Draw the handle with rounded corners
            pygame.draw.rect(surface, self.handle_color, handle_rect, border_radius=10)

    def handle_event(self, event):
        if self.visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # Update value based on mouse position
            normalized_x = min(
                1, max(0, (event.pos[0] - self.rect.x) / self.rect.width))
            self.value = round(self.min_value + normalized_x *
                               (self.max_value - self.min_value))
            # Trigger action if provided
            if self.action:
                self.action(self)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False


# Text setting
class Text(Setting):
    def __init__(self, x, y, text, color, font_size=36, font_name=None):
        super().__init__(x, y)
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font_name = font_name
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.surface = self.create_surface()
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def create_surface(self):
        return self.font.render(self.text, True, self.color)

    def draw(self, surface):
        if self.visible:
            surface.blit(self.surface, (self.x, self.y))

    def handle_event(self, event):
        pass

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height

    def set_visibility(self, visible):
        self.visible = visible


# ColorPicker setting
class ColorPicker(Setting):
    def __init__(self, x, y, width, height, default_color, action):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.color = default_color
        self.action = action

    def draw(self, surface):
        super().draw(surface)
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect)

    def handle_event(self, event):
        if self.visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                # Trigger action if provided
                if self.action:
                    self.action(self)


# SettingsGroup
class SettingsGroup:
    def __init__(self, x, y, buttons):
        self.x = x
        self.y = y
        self.buttons = buttons
        self.active_button = self.buttons[0]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)
