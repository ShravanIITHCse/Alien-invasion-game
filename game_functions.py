"""Contains all the functions which running the game requires"""
import pygame
import sys
from bullet import Bullet


def keydown_events(event, ship, window, bullets, settings):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.move_right_flag = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.move_left_flag = True
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_SPACE:
        if settings.bullet_limit > len(bullets):
            new_bullet = Bullet(window, settings, ship)
            bullets.add(new_bullet)


def check_events(ship, settings, bullets, window):
    """Check the events whichever is going to happen on windows"""

    # Respond to keypress events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, ship, window, bullets, settings)
        elif event.type == pygame.KEYUP:
            # Move the ship to the right
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.move_right_flag = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.move_left_flag = False


def update_screen(window, settings, ship, bullets):
    """This function will keep changing the window"""
    # Redraw the window with this color
    window.fill(settings.screen_color)
    # Updates the ship and bullets position by redrawing it
    ship.update_ship()
    for bullet in bullets:
        bullet.update_bullet()
        if bullet.bullet_rect.bottom < 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()
    ship.draw_ship()
    # Draws the window
    pygame.display.flip()
