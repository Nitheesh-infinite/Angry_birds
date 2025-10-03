import constants as c
import random

class Block:
    def __init__(self, row, col, x, y, block_type):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.block_type = block_type
        self.width = c.BLOCK_WIDTH
        self.height = c.BLOCK_HEIGHT
        self.is_destroyed = False
        self.is_falling = False
        self.target_y = y

        if block_type == "WOOD":
            self.image = c.RECTANGLE_IMAGE_WOOD
            self.life = 100
        elif block_type == "ROCK":
            self.image = c.RECTANGLE_IMAGE_ROCK
            self.life = 150
        else:
            self.image = c.RECTANGLE_IMAGE_GLASS
            self.life = 80

        self.vy = 5  
        self.max_life = self.life
        self.lower_block = None

    def update_position(self):
        if self.is_falling:
            if self.y < self.target_y:
                self.y += self.vy
            else:
                self.y = self.target_y
                self.row += 1
                self.is_falling = False
            
    def draw(self):
        if not self.is_destroyed:
            c.screen.blit(self.image, (self.x, self.y))

    def take_damage(self, damage):
        
        self.life -= damage

        if self.life <= 75 and self.life > 50 and self.block_type == "WOOD":
            self.image = c.RECTANGLE_IMAGE_WOOD1
        elif self.life <= 50 and self.life > 25 and self.block_type == "WOOD":
            self.image = c.RECTANGLE_IMAGE_WOOD2
        elif self.life <= 25 and self.block_type == "WOOD":
            self.image = c.RECTANGLE_IMAGE_WOOD3
        elif self.life <= 112 and self.life > 75 and self.block_type == "ROCK":
            self.image = c.RECTANGLE_IMAGE_ROCK1
        elif self.life <= 75 and self.life > 38 and self.block_type == "ROCK":
            self.image = c.RECTANGLE_IMAGE_ROCK2
        elif self.life <= 37 and self.block_type == "ROCK":
            self.image = c.RECTANGLE_IMAGE_ROCK3
        elif self.life <= 60 and self.life > 40 and self.block_type == "GLASS":
            self.image = c.RECTANGLE_IMAGE_GLASS1
        elif self.life <= 40 and self.life > 20 and self.block_type == "GLASS":
            self.image = c.RECTANGLE_IMAGE_GLASS2
        elif self.life <= 20 and self.block_type == "GLASS":
            self.image = c.RECTANGLE_IMAGE_GLASS3

        if self.life <= 0:
            self.is_destroyed = True
