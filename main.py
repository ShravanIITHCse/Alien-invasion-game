import pygame
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

    # Loop which will keep the window alive till we dont do anything
    while True:
        print(".")

    pygame.display.flip()


    



run_game()