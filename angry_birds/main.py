import pygame
import constants as c

from screens.menu_screen import show_menu
from screens.settings import settings_screen
from screens.gameplay import game_screen
from screens.init_screen import init_screen
def main():
    # Setup game screen, load assets, create players, etc.
    init_screen()

    
    # Create a surface for fade-in effect
    fade_surface = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))  # Create the fade surface
    fade_surface.fill((0, 0, 0))  # Fill the surface with black
    
    # Fade-in effect (alpha gradually decreases from 255 to 0)
    for alpha in range(255, 0, -5):  # Decrease alpha from 255 to 0
        fade_surface.set_alpha(alpha)
        c.screen.fill((0, 0, 0))  # Clear the screen with black
        pygame.display.update()
        c.screen.blit(fade_surface, (0, 0))  # Draw the fade surface over everything
        pygame.display.update()
        pygame.time.delay(15)




    while True:
        selected = show_menu()

        if selected == "play":
            game_screen()

        elif selected == "settings":
            settings_screen()
            pass

        elif selected == "exit":
            break
    

if __name__ == "__main__":
    main()