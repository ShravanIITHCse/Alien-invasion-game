import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from aliens import Aliens
from pygame.sprite import Group


def run_game():
    """This is the main function which will run the game"""

    # Initialize pygame
    pygame.init()
    # Creating object to store all the settings data
    settings = Settings()
    # Create screen object
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion Game")
    # Create ship object
    ship = Ship(window, settings)
    # Group of bullets
    bullets = Group()
    aliens = Group()

    # Create fleet of the aliens
    gf.create_alien_fleet(window, settings, aliens, ship)

    # Loop which will keep the window alive till we don't do anything
    while True:
        gf.check_events(ship, settings, bullets, window)
        gf.update_screen(window, settings, ship, bullets, aliens)


run_game()
