"""Contains all the functions which running the game requires"""
import pygame
import sys
from bullet import Bullet
from aliens import Aliens
from time import sleep


def keydown_events(event, ship, window, bullets, settings, stats, aliens, score_board):
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
    if event.key == pygame.K_p:
        start_game(stats, aliens, bullets, window, settings, ship, score_board)


def update_score_board(score_board):
    score_board.update_level()
    score_board.update_score()
    score_board.update_high_score()
    score_board.update_ships()


def start_game(stats, aliens, bullets, window, settings, ship, score_board):
    # Reset the game statistics
    stats.reset_stats()
    update_score_board(score_board)
    stats.game_active_status = True
    pygame.mouse.set_visible(False)

    # Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create the new fleet and center the ship
    create_alien_fleet(window, settings, aliens, ship)
    ship.center_ship()


def check_play_button_click(mouse_coord, play_button, stats, aliens, bullets, window, settings, ship, score_board):
    """Start New game when player click play"""
    button_clicked = play_button.button_rect.collidepoint(mouse_coord)
    if button_clicked and not stats.game_active_status:
        start_game(stats, aliens, bullets, window, settings, ship, score_board)


def check_events(ship, settings, bullets, window, play_button, stats, aliens, score_board):
    """Check the events whichever is going to happen on windows"""

    # Respond to keypress events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_events(event, ship, window, bullets, settings, stats, aliens, score_board)
        elif event.type == pygame.KEYUP:
            # Move the ship to the right
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.move_right_flag = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.move_left_flag = False
        # Check if the user press play button or not
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coord = pygame.mouse.get_pos()
            check_play_button_click(mouse_coord, play_button, stats, aliens, bullets, window, settings, ship, score_board)


def check_high_score(stats, score_board):
    if stats.high_score < stats.score:
        stats.high_score = stats.score
        score_board.update_high_score()


def check_collisions(bullets, aliens, stats, settings, score_board):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # check for the collisions to increase points
    if collisions:
        for killed_aliens in collisions.values():
            stats.score += settings.alien_points * len(killed_aliens)
            score_board.update_score()
        check_high_score(stats, score_board)


def gf_update_bullet(bullets, aliens, window, settings, ship, stats, score_board):
    """Update all bullets of bullet group and draw the bullets"""
    for bullet in bullets:
        bullet.update_bullet()
        if bullet.bullet_rect.bottom < 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()

    check_collisions(bullets, aliens, stats, settings, score_board)
    check_repopulation(aliens, bullets, window, settings, ship, stats, score_board)


def repopulation_loss(bullets, aliens, stats, window, settings, ship, score_board):
    if stats.ship_left > 0:
        # Decrement ship left
        stats.ship_left -= 1
        # Empty the list of aliens and bullets
        bullets.empty()
        aliens.empty()

        # Create a new fleet and center the ship
        score_board.update_ships()
        create_alien_fleet(window, settings, aliens, ship)
        ship.ship_rect.centerx = window.get_rect().centerx

        # Pause
        sleep(0.5)
    else:
        settings.return_to_default()
        pygame.mouse.set_visible(True)
        stats.game_active_status = False


def check_repopulation(aliens, bullets, window, settings, ship, stats, score_board):
    """Repopulate the fleet if there is no alien remaining"""
    screen_rect = window.get_rect()
    if len(aliens) == 0:
        bullets.empty()
        create_alien_fleet(window, settings, aliens, ship)
        stats.level += 1
        score_board.update_level()
        settings.level_up()

    if pygame.sprite.spritecollideany(ship, aliens):
        repopulation_loss(bullets, aliens, stats, window, settings, ship, score_board)

    for alien in aliens:
        if alien.alien_rect.bottom >= screen_rect.bottom:
            repopulation_loss(bullets, aliens, stats, window, settings, ship, score_board)
            break


def update_screen(window, settings, ship, bullets, aliens, stats, play_button, score_board):
    """This function will keep changing the window"""
    # Redraw the window with this color
    window.fill(settings.screen_color)

    # Updates the ship and bullets position by redrawing it
    if stats.game_active_status:
        ship.update_ship()
        gf_update_bullet(bullets, aliens, window, settings, ship, stats, score_board)
    ship.draw_ship()
    score_board.show_score_board()
    gf_update_fleet(aliens, settings, ship, bullets, window, stats, score_board)

    # Draws the play button when game is inactive
    if not stats.game_active_status:
        window.fill(settings.pause_screen_color)
        play_button.draw_button()

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


def gf_update_fleet(aliens, settings, ship, bullets, window, stats, score_board):
    check_fleet_direction(aliens, settings)
    for alien in aliens:
        if stats.game_active_status:
            alien.update_alien()
        alien.draw_alien()
    check_repopulation(aliens, bullets, window, settings, ship, stats, score_board)
    # if pygame.sprite.spritecollideany(ship, aliens):
    #     print("Ship hit!!")
