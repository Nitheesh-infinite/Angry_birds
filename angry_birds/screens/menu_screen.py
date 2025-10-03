import pygame
import constants as c
from core import sprites  # You should have play_btn, settings_btn, exit_btn
from core.sound_manager import play_music

def show_menu():
    pygame.init()
    play_music()
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    print("Menu screen initialized")



    for i, btn in enumerate(c.buttons):
        if i == 0:
            x = c.SCREEN_WIDTH*8//15
            y = c.SCREEN_HEIGHT*4//15
            btn["rect"] = pygame.Rect(x, y, c.btn_width_Play, c.btn_height_play)
        elif i == 1:
            x = 10
            y = 10
            btn["rect"] = pygame.Rect(x, y, c.btn_width_Settings, c.btn_height_Settings)
        else:
            x = c.SCREEN_WIDTH*19//20 -10 
            y = 10
            btn["rect"] = pygame.Rect(x, y, c.btn_width_Exit, c.btn_height_Exit)
        

    selected_index = 0
    menu_running = True

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    for btn in c.buttons:
                        if btn["rect"].collidepoint(event.pos):
                            return btn["name"].lower()

        c.screen.blit(c.menu_background, (0, 0))

        for i, btn in enumerate(c.buttons):
            image = btn["image"].copy()
            if i == selected_index:
                image.set_alpha(200)
            c.screen.blit(image, btn["rect"].topleft)

        c.screen.blit(c.menu_logo, (c.SCREEN_WIDTH//10, c.SCREEN_HEIGHT//10))
        pygame.display.flip()
        clock.tick(c.FPS)

    pygame.quit()
    exit()
