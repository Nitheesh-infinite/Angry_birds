import constants as c
import pygame
import time

def init_screen():
    pygame.init()
    
    pygame.display.set_caption('Angry Birds')

    font = pygame.font.SysFont(None, 50)
    clock = pygame.time.Clock()

    c.screen.fill((0, 0, 0))  
    pygame.display.update()  

    init_image_logo = pygame.image.load('resources/images/init_image_logo.jpg').convert_alpha()
    init_image_logo = pygame.transform.scale(init_image_logo, (c.SCREEN_WIDTH*4//5, c.SCREEN_HEIGHT*4//5))

    start_time = time.time()
    loading_duration = 2 
    dot_count = 0
    running = True

    while running:
        elapsed_time = time.time() - start_time
        dot_count = int(elapsed_time * 3) % 4
        
        c.screen.fill((0, 0, 0)) 

        c.screen.blit(init_image_logo, (c.SCREEN_WIDTH//10, c.SCREEN_HEIGHT//10))  

        loading_text = font.render('Loading' + '.' * dot_count, True, (255, 0, 0)) 
        text_rect = loading_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT * 9 // 10))  

        c.screen.blit(loading_text, text_rect)

        pygame.display.update()
        
        clock.tick(60)

        if elapsed_time > loading_duration:
            running = False

    fade_surface = pygame.Surface((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))  # Create a surface for the fade effect
    fade_surface.fill((0, 0, 0))  # Fill it with black color
    for alpha in range(0, 255, 5):  # Increase alpha (opacity) gradually to create fade-out
        fade_surface.set_alpha(alpha)
        c.screen.fill((0, 0, 0))  # Fill the screen with black (start of fade)
        c.screen.blit(init_image_logo, (c.SCREEN_WIDTH // 10, c.SCREEN_HEIGHT // 10))  # Draw logo
        c.screen.blit(loading_text, text_rect)  # Draw loading text
        c.screen.blit(fade_surface, (0, 0))  # Draw the fade surface over everything
        pygame.display.update()
        clock.tick(60)

    return
    
