import sys
import pygame

def check_events():
    # Watch for keyboard and mouse events and respond accordingly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    # Update image on the screen and flip to new screen
     # Redraw the screen during each pass through the game loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make the most recently drawn screen available 
    pygame.display.flip()