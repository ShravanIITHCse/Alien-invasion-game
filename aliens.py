import pygame
from pygame.sprite import Sprite


class Aliens(Sprite):
    """Class which will represent single alien in fleet"""

    def __init__(self, window, settings):
        """Initialize all the parameters of aliens"""
        super(Aliens, self).__init__()
        self.window = window
        self.settings = settings
        # Loading the image of alien
        self.alien_image = pygame.image.load('images/alien.bmp')
        self.alien_rect = self.alien_image.get_rect()
        # Positioning the image
        self.alien_rect.x = self.alien_rect.width
        self.alien_rect.y = self.alien_rect.height

    def draw_alien(self):
        """Draws the alien"""
        self.window.blit(self.alien_image, self.alien_rect)
