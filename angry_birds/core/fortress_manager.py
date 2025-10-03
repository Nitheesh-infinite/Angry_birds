import pygame
import constants as c
import core.blocks as bl
import random

class Fortress:
    def __init__(self, position, rows, cols, id):
        self.rows = rows
        self.cols = cols
        self.id = id
        self.top_left = position
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.rects = []
        self.no_of_blocks_left = rows * cols
        for row in range(rows):
            for col in range(cols):
                block_type = random.choice(c.BLOCKS)
                x_ini = position[0] + col * (c.BLOCK_WIDTH + 1)
                y_ini = position[1] - row * (c.BLOCK_HEIGHT + 1)
                block = bl.Block(row, col, x_ini, y_ini, block_type)
                self.grid[row][col] = block
                self.rects.append(pygame.Rect(x_ini, y_ini, block.width, block.height))

    def update_fortress(self):
        for row in range(1, self.rows):
            for col in range(self.cols):
                block = self.grid[row][col]
                if block and not block.is_falling and not block.is_destroyed:
                    below = self.grid[row - 1][col]
                    if below is None or below.is_destroyed:
                        block.is_falling = True
                        block.target_y = block.y + block.height + 1
                        self.grid[row - 1][col] = block
                        self.grid[row][col] = None

        self.rects.clear()
        for row in range(self.rows):
            for col in range(self.cols):
                block = self.grid[row][col]
                if block:
                    block.update_position()
                    if block.is_destroyed:
                        self.grid[row][col] = None
                    else:
                        self.rects.append(pygame.Rect(block.x, block.y, block.width, block.height))
        self.no_of_blocks_left = len(self.rects)
    def draw_fortress(self):
        for row in range(self.rows):
            for col in range(self.cols):
                block = self.grid[row][col]
                if block:
                    block.draw()




