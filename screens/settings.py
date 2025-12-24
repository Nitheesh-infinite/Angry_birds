import pygame
import constants as c
from core.sound_manager import play_music, stop_music, toggle_music 

def settings_screen():
    clock = pygame.time.Clock()
    play_music()

    # Define buttons
    sound_button = pygame.Rect(c.SCREEN_WIDTH//2 - 100, c.SCREEN_HEIGHT//2 - 50, 200, 50)
    mode_button = pygame.Rect(c.SCREEN_WIDTH//2 - 100, c.SCREEN_HEIGHT//2 + 50, 200, 50)
    back_button = pygame.Rect(20, 20, 100, 40)

    settings_running = True

    while settings_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sound_button.collidepoint(event.pos):
                    toggle_music()

                elif mode_button.collidepoint(event.pos):
                    c.current_bg_mode = "Night" if c.current_bg_mode == "Day" else "Day"

                elif back_button.collidepoint(event.pos):
                    settings_running = False

        c.screen.blit(c.bg_images[c.current_bg_mode], (0, 0))

        # Apply translucent dark overlay for blur/fade effect
        overlay = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        c.screen.blit(overlay, (0, 0))

        # Draw Buttons
        sound_text = c.FIRE_FONT.render("Sound: {}".format(
            "Mute" if c.sound_files[c.current_sound_index] is None else f"{c.current_sound_index+1}"), True, (255, 255, 0))
        mode_text = c.FIRE_FONT.render("Mode: {}".format(c.current_bg_mode), True, (255, 255, 0))
        back_text = c.FIRE_FONT.render("Back", True, (255, 255, 0))

        c.screen.blit(sound_text, (sound_button.x + 20, sound_button.y + 10))
        c.screen.blit(mode_text, (mode_button.x + 20, mode_button.y + 10))
        c.screen.blit(back_text, (back_button.x + 10, back_button.y + 5))

        pygame.display.flip()
        clock.tick(c.FPS)

    pygame.mixer.music.stop()
    return "menu"