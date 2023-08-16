import sys
import pygame

from settings import Settings

def run_game():
    # Initialize the game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # start the main game loop
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # Redraw the screen during each pass through the game loop
        screen.fill(ai_settings.bg_color)

        # make the most recently drawn screen available 
        pygame.display.flip()


run_game()