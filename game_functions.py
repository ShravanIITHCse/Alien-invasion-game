"""Contains all the functions which running the game requires"""
import pygame
import sys

"""Check the events whichever is going to happen on windows"""


def check_events(ship, settings):
    """Respond to keypress events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Move the ship to the right
            if event.key == pygame.K_RIGHT:
                ship.move_right_flag = True
            if event.key == pygame.K_LEFT:
                ship.move_left_flag = True
        elif event.type == pygame.KEYUP:
            # Move the ship to the right
            if event.key == pygame.K_RIGHT:
                ship.move_right_flag = False
            if event.key == pygame.K_LEFT:
                ship.move_left_flag = False


def update_screen(window, settings, ship):
    """This function will keep changing the window"""
    # Redraw the window with this color
    window.fill(settings.screen_color)
    # Updates the ship position by redrawing it
    ship.update_ship()
    ship.blitme()
    # Draws the window
    pygame.display.flip()
