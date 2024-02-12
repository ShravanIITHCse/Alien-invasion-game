import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from buttons import Button
from scoreboard import Scoreboard
from aliens import Aliens
from game_stats import GameStats
from pygame.sprite import Group


def run_game():
    """This is the main function which will run the game"""

    # Initialize pygame
    pygame.init()
    # Creating object to store all the settings data
    settings = Settings()
    # Create an instance of the game
    stats = GameStats(settings)
    # Create screen object
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion Game")
    # Create ship object
    ship = Ship(window, settings)
    # Group of bullets
    bullets = Group()
    aliens = Group()
    # Make Play Button
    play_button = Button(settings, window, message="Play")
    # Create a Scoreboard object
    score_board = Scoreboard(window, settings, stats)

    # Create fleet of the aliens
    gf.create_alien_fleet(window, settings, aliens, ship)

    # Loop which will keep the window alive till we don't do anything
    while True:
        gf.check_events(ship, settings, bullets, window, play_button, stats, aliens, score_board)
        gf.update_screen(window, settings, ship, bullets, aliens, stats, play_button, score_board)


run_game()
