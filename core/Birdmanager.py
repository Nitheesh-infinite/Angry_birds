import pygame
import constants as c
import random

class BirdManager():
    def __init__(self,id):
        self.birds=["RED","BLUE","YELLOW","BLACK"]
        self.player_id=id
        active_bird=None

    def show_birds(self):
        i=0
        for bird in self.birds:
            self.IMAGE=c.BIRD_IMAGES[bird]
            if self.player_id==1:
                c.screen.blit(self.IMAGE,(c.RECT_OF_SELECTING_BIRD_AT_1[0]+i*c.SCREEN_WIDTH//50,c.RECT_OF_SELECTING_BIRD_AT_1[1]))
            else:
                self.IMAGE=pygame.transform.flip(self.IMAGE,True,False)
                c.screen.blit(self.IMAGE,(c.RECT_OF_SELECTING_BIRD_AT_2[0]-i*c.SCREEN_WIDTH//50,c.RECT_OF_SELECTING_BIRD_AT_2[1]))
            i+=1


    def use_bird(self):
        self.active_bird=self.birds.pop(0)
        return self.active_bird
        
    def generate_bird(self):
        Random_bird=random.choice(c.BIRDS)
        self.birds.append(Random_bird)