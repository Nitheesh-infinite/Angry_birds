import pygame
import constants as c
 
def load_catapult():
    IMAGE=c.LEFT_CATAPULT_IMAGE
    c.screen.blit(IMAGE,c.LEFT_CATAPULT_RECT.topleft)
    IMAGE=c.RIGHT_CATAPULT_IMAGE
    c.screen.blit(IMAGE,c.RIGHT_CATAPULT_RECT.topleft)

def get_ropes(id,bird):
    mx,my=bird.rect.center
    if id==1:
        pygame.draw.line(c.screen,c.BROWN,pygame.math.Vector2(c.LEFT_CATAPULT_RECT[0],c.LEFT_CATAPULT_RECT[1]),pygame.math.Vector2(mx,my),5)
        pygame.draw.line(c.screen,c.BROWN,pygame.math.Vector2(c.LEFT_CATAPULT_RECT[0]+c.SCREEN_WIDTH//25,c.LEFT_CATAPULT_RECT[1]),pygame.math.Vector2(mx,my),5)
    else:
        pygame.draw.line(c.screen,c.BROWN,pygame.math.Vector2(c.RIGHT_CATAPULT_RECT[0],c.RIGHT_CATAPULT_RECT[1]),pygame.math.Vector2(mx,my),5)
        pygame.draw.line(c.screen,c.BROWN,pygame.math.Vector2(c.RIGHT_CATAPULT_RECT[0]+c.SCREEN_WIDTH//25,c.RIGHT_CATAPULT_RECT[1]),pygame.math.Vector2(mx,my),5)