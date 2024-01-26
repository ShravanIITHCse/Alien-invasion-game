import pygame.image


class Ship:

    def __init__(self, window, settings):
        """Initialize the ship and its starting position"""
        self.window = window
        self.settings = settings
        # Load the image of the ship and get its rect
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.ship_rect = self.ship_image.get_rect()
        self.screen_rect = self.window.get_rect()

        # Flag to allow continuous movement
        self.move_right_flag = False
        self.move_left_flag = False

        # Fix the position of the ship
        self.ship_rect.bottom = self.screen_rect.bottom
        self.ship_rect.centerx = self.screen_rect.centerx

    def update_ship(self):
        """Update ship position"""
        if self.move_right_flag:
            self.ship_rect.centerx += 1 * self.settings.ship_speed
        if self.move_left_flag:
            self.ship_rect.centerx -= 1 * self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location"""
        self.window.blit(self.ship_image,self.ship_rect)
