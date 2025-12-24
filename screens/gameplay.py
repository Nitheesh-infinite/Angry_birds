import pygame
import constants as c
import math
import sys
from core.Player import Player
import core.Birdmanager as BM
import core.Bird as Bird
import core.catapult as Cat
import core.fortress_manager as fm
from screens.name_screen import name_screen 
from core.sound_manager import play_music
from screens.settings import settings_screen
from screens.winner_screen import Winner_screen
import random
def game_screen():
    pygame.init()
    play_music()

    pygame.display.set_caption("Angry Birds")
    while True:
        result = name_screen(1, 2)
        if not result:
            return  
        else:
            player1_name, player2_name = result
            break  
    Player1 = Player(1, player1_name)
    Player2 = Player(2, player2_name)
    players=[Player2,Player1]
    clock = pygame.time.Clock()
    Birds_1 = BM.BirdManager(1)
    Birds_2 = BM.BirdManager(0)

    current_bird = Bird.Bird()
    init_player = random.randint(0, 1)
    current_player = init_player
    birds = []
    fort1 = fm.Fortress(c.LEFT_FORT, c.ROWS, c.COLS, 1)
    fort2 = fm.Fortress(c.RIGHT_FORT, c.ROWS, c.COLS, 2)
    
    current_fortress = fort1 if current_player == 0 else fort2
    TURN_TIME_LIMIT = 30000
    initial_time = pygame.time.get_ticks()
    turn_start_time = pygame.time.get_ticks()

    running = True
    while running:
        current_time=pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if not current_bird.is_active:
                    if current_player == 1 and c.RECT_OF_SELECTING_BIRD_AT_1.collidepoint(mouse_pos):
                        current_bird.name = Birds_1.use_bird()
                        current_bird.set_bird(1)
                        c.screen.blit(current_bird.IMAGE,c.LEFT_CATAPULT_RECT.topleft)
                        Birds_1.generate_bird()
                    elif current_bird and  current_player == 0 and c.RECT_OF_SELECTING_BIRD_AT_2.collidepoint(mouse_pos):
                        current_bird.name = Birds_2.use_bird()
                        current_bird.set_bird(2)
                        c.screen.blit(current_bird.IMAGE,c.RIGHT_CATAPULT_RECT.topleft)
                        Birds_2.generate_bird()
                elif current_bird.is_active and current_bird.rect.collidepoint(mouse_pos):
                    if not current_bird.is_launched:
                        current_bird.is_dragging = True
                elif c.settings_rect.collidepoint(mouse_pos):
                    settings_screen()
                elif c.exit_rect.collidepoint(mouse_pos):
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if current_bird.is_launched and current_bird.is_active and not current_bird.super_power_triggered:
                    if current_bird.name == "BLUE":
                        birds=current_bird.active_super_power()
                    else:
                        current_bird.active_super_power()
                    
            elif event.type == pygame.MOUSEMOTION and current_bird.is_dragging:
                current_bird.clamp()

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if current_bird.is_dragging:
                    current_bird.initial_velocity()
                    current_bird.is_dragging = False
                    current_bird.is_launched = True


        c.screen.blit(c.bg_images[c.current_bg_mode],(0,0))
        c.screen.blit(c.rd_images[c.current_bg_mode], (0,0))
        c.screen.blit(c.settings_button, (10, 10))
        c.screen.blit(c.exit_button, (c.SCREEN_WIDTH*19//20 -10, 10))

        Player1.display_score((100,150))
        Player2.display_score((c.SCREEN_WIDTH - 600,150))

        Birds_1.show_birds()
        Birds_2.show_birds()
        Cat.load_catapult()



        
        elapsed_time = pygame.time.get_ticks() - turn_start_time
        remaining_time = max(0, (TURN_TIME_LIMIT - elapsed_time) // 1000)

        if current_player == 1:
            turn_text = c.FIRE_FONT.render(f"Player {current_player}'s Turn", True, (255, 0, 0))
        else:
            turn_text = c.FIRE_FONT.render(f"Player {current_player+2}'s Turn", True, (255, 0, 0))
        c.screen.blit(turn_text, (c.SCREEN_WIDTH // 2 - 80, c.SCREEN_HEIGHT // 20 - 40))

        timer_text = c.FIRE_FONT.render(f"Time Left: {remaining_time}s", True, (255, 0, 0))
        c.screen.blit(timer_text, (c.SCREEN_WIDTH // 2 - 80, c.SCREEN_HEIGHT // 20))

        if elapsed_time >= TURN_TIME_LIMIT:
            current_bird.reset()
            current_player = (current_player + 1) % 2
            current_fortress = fort1 if current_player == 0 else fort2
            turn_start_time = pygame.time.get_ticks()  
            continue
        
        
        b=1
        if current_bird.name=="BLUE" and current_bird.super_power_triggered:
            for bird in birds:
                if bird.is_active:
                    bird.update_position_and_velocity()
                    bird.show_bird()
                    b=b+1
                    if bird.is_launched and bird.rect.colliderect((c.ROAD_RECT[0],c.ROAD_RECT[1]+c.BLOCK_WIDTH-30,c.SCREEN_WIDTH,c.SCREEN_HEIGHT)):
                        bird.velocity[1] *= -0.7
                        bird.velocity[0] *= 0.8
                        bird.rect.bottom = c.ROAD_RECT[1]+c.SCREEN_WIDTH//50-1

                if bird.out_of_screen() :
                    bird.is_active = False
                    bird.IMAGE = None
                    bird.is_launched = False
                    continue

                if bird.is_launched:
                    if (current_player == 1 and bird.rect.centerx > c.SCREEN_WIDTH*3//5) or (current_player == 0 and bird.rect.centerx < c.SCREEN_WIDTH*2//5):
                        if not bird.collide_with_block:
                            for row in range(current_fortress.rows):
                                for col in range(current_fortress.cols):
                                    block = current_fortress.grid[row][col]
                                    if block and not block.is_destroyed:
                                        if math.hypot(bird.velocity[0],bird.velocity[1])>1 and bird.circle_rect_collision((block.x,block.y,block.width,block.height)):
                                            if block.block_type == "WOOD":
                                                block.take_damage(bird.damage_to_wood)
                                                bird.take_damage(bird.damage_to_wood)
                                                players[current_player].update_score(bird.damage_to_wood)
                                            elif block.block_type == "ROCK":
                                                block.take_damage(bird.damage_to_rock)
                                                bird.take_damage(bird.damage_to_rock)
                                                players[current_player].update_score(bird.damage_to_rock)
                                            elif block.block_type == "GLASS":
                                                block.take_damage(bird.damage_to_glass)
                                                bird.take_damage(bird.damage_to_glass)
                                                players[current_player].update_score(bird.damage_to_glass)
                                            if bird.is_active:
                                                side= bird.get_collision_side((block.x,block.y,block.width,block.height))
                                                if side == "LEFT":
                                                    bird.rect.centerx = block.x +1
                                                elif side == "RIGHT":
                                                    bird.rect.centerx = block.x + block.width + 1
                                                elif side == "TOP":
                                                    bird.rect.centery = block.y - 1
                                                elif side == "BOTTOM":
                                                    bird.rect.centery = block.y  + block.height + 1
                                                if side in ("LEFT", "RIGHT"):
                                                    bird.velocity[0] *= -1
                                                    bird.IMAGE = pygame.transform.flip(bird.IMAGE, True, False)
                                                else:
                                                    bird.velocity[1] *= -0.5
                                                    bird.velocity[0] *= 0.7
                                                if bird.bounce_time is None:
                                                    bird.bounce_time = current_time
                                                break
                                    
                    if bird.bounce_time:
                        if current_time - bird.bounce_time >= bird.bounce_survive_duration:
                            bird.is_active = False
                            bird.IMAGE = None
                            bird.is_launched = False
                            
                    if math.hypot(bird.velocity[0],bird.velocity[1])<0.5 :
                        bird.is_active = False
                        bird.IMAGE = None
                        bird.is_launched = False
        else:
            if current_bird.is_active:
                if current_bird.is_dragging:
                    Cat.get_ropes(current_bird.id,current_bird)
                    current_bird.predicted_projectile_path()
                current_bird.update_position_and_velocity()
                current_bird.show_bird()
                if current_bird.is_launched and current_bird.rect.colliderect((c.ROAD_RECT[0],c.ROAD_RECT[1]+c.BLOCK_WIDTH-30,c.SCREEN_WIDTH,c.SCREEN_HEIGHT)):
                    current_bird.velocity[1] *= -0.7
                    current_bird.velocity[0] *= 0.8
                    current_bird.rect.bottom = c.ROAD_RECT[1]+c.SCREEN_WIDTH//50-1

            if current_bird.out_of_screen() :
                current_bird.reset()
                current_player = (current_player + 1) % 2
                current_fortress = fort1 if current_player == 0 else fort2
                turn_start_time = pygame.time.get_ticks()
                continue

            if current_bird.is_launched:
                if (current_player == 1 and current_bird.rect.centerx > c.SCREEN_WIDTH*3//5) or (current_player == 0 and current_bird.rect.centerx < c.SCREEN_WIDTH*2//5):
                    if not current_bird.collide_with_block:
                        for row in range(current_fortress.rows):
                            for col in range(current_fortress.cols):
                                block = current_fortress.grid[row][col]
                                if block and not block.is_destroyed:
                                    if math.hypot(current_bird.velocity[0],current_bird.velocity[1])>2 and current_bird.circle_rect_collision((block.x,block.y,block.width,block.height)):
                                        if block.block_type == "WOOD":
                                            block.take_damage(current_bird.damage_to_wood)
                                            current_bird.take_damage(current_bird.damage_to_wood)
                                            players[current_player].update_score(current_bird.damage_to_wood)
                                        elif block.block_type == "ROCK":
                                            block.take_damage(current_bird.damage_to_rock)
                                            current_bird.take_damage(current_bird.damage_to_rock)
                                            players[current_player].update_score(current_bird.damage_to_rock)
                                        elif block.block_type == "GLASS":
                                            block.take_damage(current_bird.damage_to_glass)
                                            current_bird.take_damage(current_bird.damage_to_glass)
                                            players[current_player].update_score(current_bird.damage_to_glass)
                                        if current_bird.is_active:
                                            side= current_bird.get_collision_side((block.x,block.y,block.width,block.height))
                                            if side == "LEFT":
                                                current_bird.rect.centerx = block.x +1
                                            elif side == "RIGHT":
                                                current_bird.rect.centerx = block.x + block.width + 1
                                            elif side == "TOP":
                                                current_bird.rect.centery = block.y - 1
                                            elif side == "BOTTOM":
                                                current_bird.rect.centery = block.y  + block.height + 1
                                            if side in ("LEFT", "RIGHT"):
                                                current_bird.velocity[0] *= -1
                                                current_bird.IMAGE = pygame.transform.flip(current_bird.IMAGE, True, False)
                                            else:
                                                current_bird.velocity[1] *= -0.5
                                                current_bird.velocity[0] *= 0.7
                                            if current_bird.bounce_time is None:
                                                current_bird.bounce_time = current_time
                                            break
                                
                if current_bird.bounce_time:
                    if current_time - current_bird.bounce_time >= current_bird.bounce_survive_duration:
                        current_bird.reset()
                        current_player = (current_player + 1) % 2
                        current_fortress = fort1 if current_player == 0 else fort2
                        turn_start_time = pygame.time.get_ticks()
                if math.hypot(current_bird.velocity[0],current_bird.velocity[1])<0.5 :
                    current_bird.reset()
                    current_player = (current_player + 1) % 2
                    current_fortress = fort1 if current_player == 0 else fort2
                    turn_start_time = pygame.time.get_ticks()

        if b != 1 and all(not bird.is_active for bird in birds):
            birds.clear()  
            current_player = (current_player + 1) % 2
            current_fortress = fort1 if current_player == 0 else fort2
            turn_start_time = pygame.time.get_ticks()
            current_bird = Bird.Bird()  
        
        fort1.update_fortress()
        fort2.update_fortress()
        fort1.draw_fortress()
        fort2.draw_fortress()
        if fort1.no_of_blocks_left == 0 and not fort2.no_of_blocks_left == 0:
            if not current_player == 1:
                players[0].all_blocks_destroyed= True
                running=False
        elif fort2.no_of_blocks_left == 0 and not fort1.no_of_blocks_left == 0:
            if not current_player == 0:
                players[1].all_blocks_destroyed= True
                running=False
        elif fort1.no_of_blocks_left == 0 and fort2.no_of_blocks_left == 0:
            players[0].all_blocks_destroyed= True
            players[1].all_blocks_destroyed= True
            running=False    
        if pygame.time.get_ticks() - initial_time >= c.total_game_time:
            if init_player != current_player:
                running=False

        clock.tick(c.FPS)
        pygame.display.update()
    Winner_screen(players[1],players[0])



    pygame.quit()
    sys.exit()





