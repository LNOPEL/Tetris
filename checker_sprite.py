import pygame
import random
pygame.init()

screen_width = 300
screen_height = 600

class Checker_Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w = 400, h = 10):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.image = pygame.Surface((400, 10))
        self.rect = self.image.get_rect(center = (x + 200, y))

        # self.image.fill((0, 0, 0))

