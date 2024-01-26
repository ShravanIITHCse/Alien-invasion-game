import pygame
import sys
import game_functions as gf
from settings import Settings
import sys

def run_game():
    """This is the main function which will run the game"""

    # Intialize pygame
    pygame.init()
    # Creating object to store all the settings data
    settings = Settings()
    # Create screen object
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion Game")
    # Screen colour

    # Loop which will keep the window alive till we dont do anything
    while True:
        gf.check_events()
        gf.update_screen(window,settings.screen_color)



    



run_game()