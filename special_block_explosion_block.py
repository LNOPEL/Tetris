import pygame
import random
import time
pygame.init()
from blocks import Blocks
from straight_block import Straight_Block
from l_block import L_Block
from reverse_l_block import Reverse_L_Block
from square_block import Square_Block
from t_block import T_Block
from z_block import Z_Block
from reverse_z_block import Reverse_Z_Block


screen_width = 300
screen_height = 600

cyan = (24, 217, 204)
orange = (245, 169, 37)
red = (255, 0, 0)
blue = (66, 135, 245)
purple = (149, 24, 217)
green = (40, 184, 50)
yellow = (240, 232, 14)
black = (0, 0, 0)

class Special_Block_Explosion_Block(L_Block):
    def __init__(self, color, x, y, speed = 625):
        super().__init__(x, y, speed, (0,0,0))

        # help on this

       # self.blocks = [Straight_Block, L_Block, Reverse_L_Block, Z_Block, Square_Block, T_Block, Reverse_Z_Block]

        random_explosion_block = random.choice(self.blocks)

        # Here too
