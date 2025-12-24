import core.sprites as sp
import pygame

pygame.init()
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
FPS=60
FONT_NAME="Arial"
FONT_SIZE=30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
ROWS=4
COLS=3

FIRE_FONT = pygame.font.Font('resources/fonts/myfont.ttf', FONT_SIZE)

WHITE=(255,255,255)
BLACK=(0,0,0)
BIRDS=["RED","BLUE","YELLOW","BLACK"]

MAX_LENGTH = SCREEN_WIDTH//25
MAX_POWER=15
CATAPULT_RECT_IN_SPRITE=(120,0,55,170)
RECT_OF_SELECTING_BIRD_AT_1=pygame.Rect((SCREEN_WIDTH*23//100+10,0.74*SCREEN_HEIGHT,SCREEN_WIDTH//50,SCREEN_WIDTH//50))
RECT_OF_SELECTING_BIRD_AT_2=pygame.Rect((SCREEN_WIDTH*75//100-10,0.74*SCREEN_HEIGHT,SCREEN_WIDTH//50,SCREEN_WIDTH//50))
ROAD_RECT=pygame.Rect((0,0.77*SCREEN_HEIGHT,SCREEN_WIDTH,SCREEN_HEIGHT))
Buttons_image="resources/images/selected-buttons.png"

menu_logo = pygame.image.load('resources/images/ANGRY_BIRDS_FRIENDS_LOGO_MENU.jpg')
menu_logo = pygame.transform.scale(menu_logo, (SCREEN_WIDTH*4//10, SCREEN_HEIGHT*4//10))

menu_background = pygame.image.load('resources/images/menu_background.jpg')
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
play_button = pygame.image.load('resources/images/play_button.jpg')
play_button = pygame.transform.scale(play_button, (SCREEN_WIDTH//8, SCREEN_WIDTH//15))
settings_button = sp.get_sprite(Buttons_image, (29, 323, 94, 103),SCREEN_WIDTH//20,SCREEN_WIDTH//20)
exit_button = sp.get_sprite(Buttons_image, (154, 113, 94, 103),SCREEN_WIDTH//20,SCREEN_WIDTH//20)

BLOCK_WIDTH=SCREEN_WIDTH//20
BLOCK_HEIGHT=SCREEN_WIDTH//20


LEFT_FORT=(10,ROAD_RECT[1]-BLOCK_HEIGHT,COLS*BLOCK_WIDTH,ROWS*BLOCK_HEIGHT)
RIGHT_FORT=(SCREEN_WIDTH-10-COLS*BLOCK_WIDTH,ROAD_RECT[1]-BLOCK_HEIGHT,COLS*BLOCK_WIDTH,ROWS*BLOCK_HEIGHT)


BLOCKS=["WOOD","ROCK","GLASS"]
BROWN=(139,69,19)
GRAVITY=0.5

total_game_time = 600000



winner_background = pygame.image.load('resources/images/winner_background.jpg').convert_alpha()
winner_background = pygame.transform.scale(winner_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

RED_IMAGE=pygame.image.load('resources/images/RED.jpg').convert_alpha()
RED_IMAGE=pygame.transform.scale(RED_IMAGE,(SCREEN_WIDTH//50,SCREEN_WIDTH//50))
BLUE_IMAGE=pygame.image.load('resources/images/BLUE.jpg').convert_alpha()
BLUE_IMAGE=pygame.transform.scale(BLUE_IMAGE,(SCREEN_WIDTH//50,SCREEN_WIDTH//50))
YELLOW_IMAGE=pygame.image.load('resources/images/YELLOW.jpg').convert_alpha()
YELLOW_IMAGE=pygame.transform.scale(YELLOW_IMAGE,(SCREEN_WIDTH//50,SCREEN_WIDTH//50))
BLACK_IMAGE=pygame.image.load('resources/images/BLACK.jpg').convert_alpha()
BLACK_IMAGE=pygame.transform.scale(BLACK_IMAGE,(SCREEN_WIDTH//50,SCREEN_WIDTH//50))
BIRD_IMAGES={"RED":RED_IMAGE,"BLUE":BLUE_IMAGE,"YELLOW":YELLOW_IMAGE,"BLACK":BLACK_IMAGE}

CATAPULT_IMAGE=pygame.image.load('resources/images/LEFT_CATAPULT.jpg')
CATAPULT_IMAGE1=pygame.image.load('resources/images/LEFT_CATAPULT.jpg')
LEFT_CATAPULT_IMAGE=pygame.transform.scale(CATAPULT_IMAGE1,(SCREEN_WIDTH*2//50,SCREEN_WIDTH*3//50))
LEFT_CATAPULT_RECT=pygame.Rect((SCREEN_WIDTH*17//100+10,ROAD_RECT[1]-SCREEN_WIDTH*3//50,SCREEN_WIDTH*2//50,SCREEN_WIDTH*3//50))
RIGHT_CATAPULT_RECT=pygame.Rect((SCREEN_WIDTH*79//100-10,ROAD_RECT[1]-SCREEN_WIDTH*3//50,SCREEN_WIDTH*2//50,SCREEN_WIDTH*3//50))
RIGHT_CATAPULT_IMAGE=pygame.transform.flip(CATAPULT_IMAGE,True,False)
RIGHT_CATAPULT_IMAGE=pygame.transform.scale(RIGHT_CATAPULT_IMAGE,(SCREEN_WIDTH*2//50,SCREEN_WIDTH*3//50))



WOOD_RECTANGLE_RECT_IN_SPRITE=(250,84,80,40)
WOOD_RECTANGLE_RECT_IN_SPRITE1=(331,84,80,40)
WOOD_RECTANGLE_RECT_IN_SPRITE2=(412,84,80,40)
WOOD_RECTANGLE_RECT_IN_SPRITE3=(250,125,80,40)
WOOD_SQUARE_RECT_IN_SPRITE=(0,0,80,80)
ROCK_RECTANGLE_RECT_IN_SPRITE=(250,84,80,40)
ROCK_RECTANGLE_RECT_IN_SPRITE1=(331,84,80,40)
ROCK_RECTANGLE_RECT_IN_SPRITE2=(412,84,80,40)
ROCK_RECTANGLE_RECT_IN_SPRITE3=(250,125,80,40)
ROCK_SQUARE_RECT_IN_SPRITE=(0,0,80,80)
GLASS_RECTANGLE_RECT_IN_SPRITE=(331,84,80,40)
GLASS_RECTANGLE_RECT_IN_SPRITE1=(412,84,80,40)
GLASS_RECTANGLE_RECT_IN_SPRITE2=(250,125,80,40)
GLASS_RECTANGLE_RECT_IN_SPRITE3=(331,125,80,40)
GLASS_SQUARE_RECT_IN_SPRITE=(0,0,80,80)

RECTANGLE_IMAGE_WOOD=sp.get_sprite("resources/images/WOOD.jpg",WOOD_RECTANGLE_RECT_IN_SPRITE,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_WOOD1=sp.get_sprite("resources/images/WOOD.jpg",WOOD_RECTANGLE_RECT_IN_SPRITE1,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_WOOD2=sp.get_sprite("resources/images/WOOD.jpg",WOOD_RECTANGLE_RECT_IN_SPRITE2,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_WOOD3=sp.get_sprite("resources/images/WOOD.jpg",WOOD_RECTANGLE_RECT_IN_SPRITE3,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_ROCK=sp.get_sprite("resources/images/ROCK.jpg",ROCK_RECTANGLE_RECT_IN_SPRITE,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_ROCK1=sp.get_sprite("resources/images/ROCK.jpg",ROCK_RECTANGLE_RECT_IN_SPRITE1,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_ROCK2=sp.get_sprite("resources/images/ROCK.jpg",ROCK_RECTANGLE_RECT_IN_SPRITE2,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_ROCK3=sp.get_sprite("resources/images/ROCK.jpg",ROCK_RECTANGLE_RECT_IN_SPRITE3,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_GLASS=sp.get_sprite("resources/images/GLASS.jpg",GLASS_RECTANGLE_RECT_IN_SPRITE,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_GLASS1=sp.get_sprite("resources/images/GLASS.jpg",GLASS_RECTANGLE_RECT_IN_SPRITE1,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_GLASS2=sp.get_sprite("resources/images/GLASS.jpg",GLASS_RECTANGLE_RECT_IN_SPRITE2,BLOCK_WIDTH,BLOCK_HEIGHT)
RECTANGLE_IMAGE_GLASS3=sp.get_sprite("resources/images/GLASS.jpg",GLASS_RECTANGLE_RECT_IN_SPRITE3,BLOCK_WIDTH,BLOCK_HEIGHT)

bg_images = {
    "Day": pygame.image.load('resources/images/bg_2.jpg'),
    "Night": pygame.image.load('resources/images/bg_1.jpg')
}
bg_images["Day"] = pygame.transform.scale(bg_images["Day"], (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_images["Night"] = pygame.transform.scale(bg_images["Night"], (SCREEN_WIDTH, SCREEN_HEIGHT))
current_bg_mode = "Day"

rd_images = {
    "Day": pygame.image.load('resources/images/road.png'),
    "Night": pygame.image.load('resources/images/dark_road.png')
}
rd_images["Day"] = pygame.transform.scale(rd_images["Day"], (SCREEN_WIDTH, SCREEN_HEIGHT))
rd_images["Night"] = pygame.transform.scale(rd_images["Night"], (SCREEN_WIDTH, SCREEN_HEIGHT))


    # Load sounds
sound_files = [
    "resources/sounds/sound1.mp3",
    "resources/sounds/sound2.mp3",
    "resources/sounds/sound3.mp3",
    "resources/sounds/sound4.mp3",
    "resources/sounds/sound5.mp3",
    None
]
current_sound_index = 0

buttons = [
    {"name": "Play", "image": play_button},       
    {"name": "Settings", "image": settings_button},
    {"name": "Exit", "image": exit_button}
]

# Set button positions
btn_width_Play, btn_height_play = buttons[0]["image"].get_size()
btn_width_Settings, btn_height_Settings = buttons[1]["image"].get_size()
btn_width_Exit, btn_height_Exit = buttons[2]["image"].get_size()
settings_rect= pygame.Rect(10, 10, btn_width_Settings, btn_height_Settings)
exit_rect=pygame.Rect(SCREEN_WIDTH*19//20 -10, 10, btn_width_Exit, btn_height_Exit)