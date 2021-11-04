import pygame
import random
import time
pygame.init()
from blocks import Blocks

screen_width = 300
screen_height = 600

cyan = (24, 217, 204)
orange = (245, 169, 37)
red = (255, 0, 0)
blue = (66, 135, 245)
purple = (149, 24, 217)
green = (40, 184, 50)
yellow = (240, 232, 14)

class Reverse_Z_Block():
    def __init__(self, x, y, speed = 625):
        self.state = 0
        self.x = x
        self.y = y
        self.move_down = speed

        block_1 = Blocks(green, 135, 15, 30, 30)
        block_2 = Blocks(green, 135, 45, 30, 30)
        block_3 = Blocks(green, 165, 15, 30, 30)
        block_4 = Blocks(green, 105, 45, 30, 30)

        self.blocks = [block_1, block_2, block_3, block_4]

        self.x_speed = 0
        self.y_speed = 0
        self.prev_move = ''
        self.up_press = False
        self.i = 0

    def get_blocks(self):
        return self.blocks

    def update(self):
        keystate = pygame.key.get_pressed()
        self.i += 1
        if self.valid_move(keystate):
            for block in self.blocks:
                if self.i % self.move_down == 0:
                    block.move_down()
                    self.prev_move = "down"
                block.update()
                # print(block.rect.left)

        if keystate[pygame.K_UP] and not self.up_press:
            self.rotate()
            self.up_press = True
        elif not keystate[pygame.K_UP]:
            self.up_press = False

    def valid_move(self, move):
        if move[pygame.K_LEFT]:
            self.prev_move = 'left'
            for block in self.blocks:
                rect = block.rect
                if rect.left <= 0:
                   return False

        if move[pygame.K_RIGHT]:
            self.prev_move = 'right'
            for block in self.blocks:
                rect = block.rect
                if rect.right >= 300:
                    return False

        if move[pygame.K_DOWN]:
            self.prev_move = 'down'
            for block in self.blocks:
                rect = block.rect
                if rect.bottom >= 600:
                    return False


        # returns true/false if move is possible
        #check if any block is touching a wall
        # if it is, then block cannot move in that direction

        return True

    # def finish_move(self):
    #     # will return true if at the bottom
    #     # return not valid_move(self, down)
    #     return False

    def rotate(self):
        if self.can_rotate():
            self.state = (self.state + 1) % 2
            if self.state == 0:
                block_1 = self.blocks[0]
                x_1, y_1 = block_1.rect.x, block_1.rect.y
                block_1.setPos(x_1, y_1)

                block_2 = self.blocks[1]
                x_2, y_2 = block_2.rect.x, block_2.rect.y
                block_2.setPos(x_2, y_2)

                block_3 = self.blocks[2]
                x_3, y_3 = block_3.rect.x, block_3.rect.y
                block_3.setPos(x_3 + 60, y_3 + 30)

                block_4 = self.blocks[3]
                x_4, y_4 = block_4.rect.x, block_4.rect.y
                block_4.setPos(x_4, y_4 + 30)



            if self.state == 1:
                block_1 = self.blocks[0]
                x_1, y_1 = block_1.rect.x, block_1.rect.y
                block_1.setPos(x_1, y_1)

                block_2 = self.blocks[1]
                x_2, y_2 = block_2.rect.x, block_2.rect.y
                block_2.setPos(x_2, y_2)

                block_3 = self.blocks[2]
                x_3, y_3 = block_3.rect.x, block_3.rect.y
                block_3.setPos(x_3 - 60, y_3 - 30)

                block_4 = self.blocks[3]
                x_4, y_4 = block_4.rect.x, block_4.rect.y
                block_4.setPos(x_4, y_4 - 30)

    def can_rotate(self):
        for block in self.blocks:
            rect = block.rect
            if rect.left < 30:
                return False

        for block in self.blocks:
            rect = block.rect
            if rect.right > 270:
               return False

        return True

    def set_prev(self):
        print("debug uncusses")
        print(self.prev_move, self.prev_move == 'down', self.prev_move == 'left', self.prev_move == 'right')
        if self.prev_move == 'down':
            for block in self.blocks:
                block.rect.y = block.rect.y - 30

        if self.prev_move == 'right':
            for block in self.blocks:
                block.rect.x = block.rect.x - 30

        if self.prev_move == 'left':
            for block in self.blocks:
                block.rect.x = block.rect.x + 30

