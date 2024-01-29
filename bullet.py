import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage all the bullets from the ship"""

    def __init__(self, window, settings, ship):
        super(Bullet, self).__init__()
        self.screen = window

        # Create bullet at origin then shift it to its correct position
        self.bullet_rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect = self.bullet_rect
        self.bullet_rect.top = ship.ship_rect.top
        self.bullet_rect.centerx = ship.ship_rect.centerx

        # Store y coordinate of bullet in decimal value
        self.y = float(self.bullet_rect.y)

        # Parameters of the bullet
        self.color = settings.bullet_color
        self.bullet_speed = settings.bullet_speed

    def update_bullet(self):
        """Updates the bullet position"""
        self.y -= self.bullet_speed
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet"""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
