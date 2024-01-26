"""Contains all the functions which running the game requires"""
import pygame
import sys

"""Check the events whichever is going to happen on windows"""


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(window, bg_color):
    """This function will keep changing the window"""
    # Redraw the window with this color
    window.fill(bg_color)
    # Draws the window
    pygame.display.flip()
