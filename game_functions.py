"""Contains all the functions which running the game requires"""
import pygame
import sys
from bullet import Bullet
from aliens import Aliens


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


def gf_update_bullet(bullets):
    """Update all bullets of bullet group and draw the bullets"""
    for bullet in bullets:
        bullet.update_bullet()
        if bullet.bullet_rect.bottom < 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()


def update_screen(window, settings, ship, bullets, aliens):
    """This function will keep changing the window"""
    # Redraw the window with this color
    window.fill(settings.screen_color)
    # Updates the ship and bullets position by redrawing it
    ship.update_ship()
    gf_update_bullet(bullets)
    ship.draw_ship()
    gf_update_fleet(aliens, settings)

    # Draws the window
    pygame.display.flip()


def get_number_aliens_x(settings, alien_width):
    """Gives the no. of aliens in x"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_rows(settings, alien_height, ship_height):
    """Gives the no. of rows for the fleet"""
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(window, settings, aliens, i_index, j_index):
    alien = Aliens(window, settings)
    alien_width = alien.alien_rect.width
    alien_height = alien.alien_rect.height
    alien.alien_rect.x = alien_width + 2 * j_index * alien_width
    alien.alien_rect.y = alien_height + 2 * i_index * alien_height
    aliens.add(alien)


def create_alien_fleet(window, settings, aliens, ship):
    """Creates the alien fleet"""
    # Create alien and find no. of aliens in row
    alien = Aliens(window, settings)
    number_aliens_x = get_number_aliens_x(settings, alien.alien_rect.width)
    number_rows = get_rows(settings, alien.alien_rect.height, ship.ship_rect.height)

    # Create the fleet of aliens
    for i_index in range(number_rows):
        for j_index in range(number_aliens_x):
            create_alien(window, settings, aliens, i_index, j_index)


def check_fleet_direction(aliens, settings):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(aliens, settings)
            break


def change_fleet_direction(aliens, settings):
    """Drop the entire fleet and change the direction of motion"""
    for alien in aliens:
        alien.alien_rect.y += settings.alien_drop_rate
    settings.alien_direction *= -1


def gf_update_fleet(aliens, settings):
    check_fleet_direction(aliens, settings)
    for alien in aliens:
        alien.update_alien()
        alien.draw_alien()
