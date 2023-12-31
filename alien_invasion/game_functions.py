import sys
import pygame

def check_keydown_events(event, ship):
    # responds to keypresses
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right/left position
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    # responds to keyreleases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    # Watch for keyboard and mouse events and respond accordingly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)            

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)       

def update_screen(ai_settings, screen, ship):
    # Update image on the screen and flip to new screen
     # Redraw the screen during each pass through the game loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen available 
    pygame.display.flip()