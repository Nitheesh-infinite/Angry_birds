import pygame
import constants as c

def get_sprite(image,rect,length,width):
    pygame.init()
    sprite_sheet = pygame.image.load(image)
    sprite_part = sprite_sheet.subsurface(pygame.Rect(rect))
    sprite_part = pygame.transform.scale(sprite_part,(length,width))
    return sprite_part
