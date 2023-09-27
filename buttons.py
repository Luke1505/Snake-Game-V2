import pygame


# Base class for all settings
class Setting:
    def __init__(self, x, y):
        self.x, self.y, self.visible = x, y, True

    def draw(self, surface):
        if self.visible:
            pass  # Draw method to be overridden by subclasses

    def update(self, surface):
        pass

    def handle_event(self, event):
        pass

    def set_visibility(self, visible):
        self.visible = visible


class Text:
    def __init__(self, x, y, text, color, font_size=36, font_name=None):
        self.x = x
        self.y = y
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
        surface.blit(self.surface, (self.x, self.y))

    def handle_event(self, event):
        pass

    def get_width(self):
        return self.rect.width

    def get_height(self):
        return self.rect.height


# Button setting
class Button(Setting):
    def __init__(self, x, y, width, height, text, text_color, button_color, action):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.text, self.text_color, self.button_color, self.action, self.clicked = text, text_color, button_color, action, False
        self.active = False

    def draw(self, surface):
        super().draw(surface)
        if self.visible:
            # Draw the button rectangle
            pygame.draw.rect(surface, self.button_color, self.rect)

            # Render and display the text
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if self.visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is inside the button's rectangle
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                if self.action:
                    self.action(self)

    def reset(self):
        self.clicked = False
        
    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

# TextInput setting
class TextInput(Setting):
    def __init__(self, x, y, width, height, font, text_color, background_color, max_length=None):
        super().__init__(x, y)
        self.rect, self.font, self.text_color, self.background_color = pygame.Rect(
            x, y, width, height), font, text_color, background_color
        self.text, self.max_length, self.active, self.cursor_visible, self.cursor_timer = "", max_length, False, False, 0
        self.cursor_blink_interval = 500
        self.ignore_first_keyup = False  # Flag to ignore the first KEYUP event

    def handle_event(self, event):
        if self.visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN:
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
        elif event.type == pygame.KEYUP:
            if self.active:
                # Released key
                if event.key == pygame.K_BACKSPACE:
                    if not self.ignore_first_keyup:
                        self.text = self.text[:-1]
                    self.ignore_first_keyup = False  # Reset the flag
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
            # Draw the background
            pygame.draw.rect(surface, self.background_color, self.rect)
            # Render and display the text
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)
            # Draw the blinking cursor when active
            if self.active and self.cursor_visible:
                cursor_x = text_rect.right
                cursor_height = text_surface.get_height()
                pygame.draw.rect(surface, self.text_color,
                                 (cursor_x, text_rect.y, 2, cursor_height))

    def set_visibility(self, visible):
        super().set_visibility(visible)


# Checkbox setting
class Checkbox(Setting):
    def __init__(self, x, y, width, height, label, text_color, fill_color, callback=None):
        super().__init__(x, y)
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
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
        pygame.draw.rect(surface, self.text_color, self.rect, 2)

        if self.checked:
            # Draw a symmetrical X
            pygame.draw.line(surface, self.text_color, (self.rect.left + 5, self.rect.top + 5),
                             (self.rect.right - 5, self.rect.bottom - 5), 4)
            pygame.draw.line(surface, self.text_color, (self.rect.left + 5, self.rect.bottom - 5),
                             (self.rect.right - 5, self.rect.top + 5), 4)

        if self.label:
            label_surface = pygame.font.Font(None, 24).render(self.label, True, self.text_color)
            surface.blit(label_surface, (self.rect.right + 10, self.rect.centery - label_surface.get_height() // 2))


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
            # Draw the slider bar
            pygame.draw.rect(surface, self.slider_color, self.rect)
            # Calculate handle position
            handle_width = int((self.value - self.min_value) /
                               (self.max_value - self.min_value) * self.rect.width)
            handle_rect = pygame.Rect(
                self.rect.x, self.rect.y, handle_width, self.rect.height)
            # Draw the handle
            pygame.draw.rect(surface, self.handle_color, handle_rect)

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

# Group of settings
class SettingsGroup:
    def __init__(self, x, y, buttons):
        self.x = x
        self.y = y
        self.buttons = buttons
        self.active_button = None

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)
            if button.is_active():
                self.active_button = button
            else:
                button.deactivate()

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface)

    def get_active_button(self):
        return self.active_button

    def set_active_button(self, button):
        self.active_button = button
        button.activate()



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
