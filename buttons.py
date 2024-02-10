import pygame.font


class Button():

    def __init__(self, settings, window, message):
        """Initialize button attributes"""
        self.settings = settings
        self.screen = window
        self.screen_rect = self.screen.get_rect()

        # Set dimension properties of the button
        self.height, self.width = self.settings.button_height, self.settings.button_width
        self.button_color = self.settings.button_color
        self.text_color = self.settings.button_text_color
        self.font = pygame.font.SysFont(self.settings.button_text_font_style, self.settings.button_text_size)

        # Build the buttons rectangle and place it at proper position
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)
        self.button_rect.center = self.screen_rect.center

        # The button message should be prepped just once
        self.prep_msg(message)

    def prep_msg(self, message):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_img = self.font.render(message, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.button_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.button_rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
