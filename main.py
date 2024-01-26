import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


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

    # Loop which will keep the window alive till we don't do anything
    while True:
        gf.check_events(ship, settings)
        gf.update_screen(window, settings, ship)


run_game()
