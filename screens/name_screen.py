import pygame
import constants as c
import sys
from core.sound_manager import play_music
from screens.menu_screen import show_menu

def name_screen(id1,id2):
    play_music()
    pygame.display.set_caption("Name Screen")
    text_before1= c.FIRE_FONT.render(f"Player {id1}", True, c.BLACK)
    text_before2= c.FIRE_FONT.render(f"Player {id2}", True, c.BLACK)
    input_box1= pygame.Rect(c.SCREEN_WIDTH//3 - 250, c.SCREEN_HEIGHT//3, 500, 50)
    input_box2= pygame.Rect(c.SCREEN_WIDTH//3 - 250, c.SCREEN_HEIGHT//3 + 150, 500, 50)
    back_button = pygame.Rect(20, 20, 100, 40)
    color_active = pygame.Color('dodgerblue2')
    color_inactive = pygame.Color('lightskyblue3')
    active_box = None
    active = False
    text1 = ''
    text2 = ''
    clock = pygame.time.Clock()
    txt = 'Name of the players should not be incomplete.'
    txt_same = 'Name of the players should not be same.'
    text_surface = c.FIRE_FONT.render(txt, True, c.BLACK)
    text_surface_same = c.FIRE_FONT.render(txt_same, True, c.BLACK)
    while True:
        c.screen.blit(c.menu_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if input_box1.collidepoint(event.pos):
                        active_box = 1
                    elif input_box2.collidepoint(event.pos):
                        active_box = 2
                    elif back_button.collidepoint(event.pos):
                        show_menu()
                        return False
                    else:
                        active_box = None

            elif event.type == pygame.KEYDOWN and (active_box == 1 or active_box == 2):
                if event.key == pygame.K_RETURN:
                    if text1 == '' or text2 == '':
                        c.screen.blit(text_surface, (c.SCREEN_WIDTH//3 -input_box1.x, c.SCREEN_HEIGHT//3 - input_box1.y*3))
                    elif text1 == text2:
                        c.screen.blit(text_surface_same, (c.SCREEN_WIDTH//3 -input_box1.x, c.SCREEN_HEIGHT//3 - input_box1.y*3))
                    else:
                        return text1,text2 
                elif event.key == pygame.K_BACKSPACE and active_box == 1:
                    text1 = text1[:-1]
                elif event.key == pygame.K_BACKSPACE and active_box == 2:
                    text2 = text2[:-1]
                elif active_box == 1:
                    text1 += event.unicode 
                elif active_box == 2:
                    text2 += event.unicode
                    

        txt_surface1 = c.FIRE_FONT.render(text1, True, c.BLACK)
        txt_surface2 = c.FIRE_FONT.render(text2, True, c.BLACK)
        input_box1.w = max(500, txt_surface1.get_width() + 10)
        input_box2.w = max(500, txt_surface2.get_width() + 10)

        if active_box == 1:
            pygame.draw.rect(c.screen, color_active, input_box1, 2)
            pygame.draw.rect(c.screen, color_inactive, input_box2, 2)
        else:
            pygame.draw.rect(c.screen, color_inactive, input_box1, 2)
            pygame.draw.rect(c.screen, color_active, input_box2, 2)
        back_text = c.FIRE_FONT.render("Back", True, (255, 255, 0))
        c.screen.blit(txt_surface1, (input_box1.x + 5, input_box1.y ))
        c.screen.blit(txt_surface2, (input_box2.x + 5, input_box2.y ))
        c.screen.blit(back_text, (back_button.x + 10, back_button.y + 5))
        c.screen.blit(text_before1, (c.SCREEN_WIDTH//3 - 450, c.SCREEN_HEIGHT//3 - 50))
        c.screen.blit(text_before2, (c.SCREEN_WIDTH//3 - 450, c.SCREEN_HEIGHT//3 + 100))
        pygame.display.flip()
        clock.tick(30)
