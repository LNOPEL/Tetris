import pygame
import random
pygame.init()

screen_width = 300
screen_height = 600

cyan = (24, 217, 204)
orange = (245, 169, 37)
red = (255, 0, 0)
blue = (66, 135, 245)
purple = (149, 24, 217)
green = (40, 184, 50)
yellow = (240, 232, 14)

class Blocks(pygame.sprite.Sprite):
    def __init__(self, color, x, y, w = 120, h = 30,):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.x_speed = 0
        self.y_speed = 0

        self.down_press = False
        self.right_press = False
        self.left_press = False

        self.image = pygame.Surface((30, 32))
        self.inside = self.image.subsurface((2, 2, 26, 28))
        self.image.fill((0, 0, 0))
        self.inside.fill(color)
        self.rect = self.image.get_rect(center = (x, y))
        self.i = 0

    def is_explosion(self):
        return self.color == (0,0,0)


    def __repr__(self):
        return f'{self.color} Block with rect {self.rect}'

    def move_down(self):
        self.y_speed = 30
    def update(self):
        self.x_speed = 0


        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_DOWN] and not self.down_press:
            self.y_speed += 30
            self.down_press = True
        elif not keystate[pygame.K_DOWN]:
            self.down_press = False

        if keystate[pygame.K_LEFT] and not self.left_press:
            self.x_speed -= 30
            self.left_press = True
        elif not keystate[pygame.K_LEFT]:
            self.left_press = False

        if keystate[pygame.K_RIGHT] and not self.right_press:
            self.x_speed += 30
            self.right_press = True
        elif not keystate[pygame.K_RIGHT]:
            self.right_press = False

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    #Keep blocks inside screen bounds
        if self.rect.right >= screen_width:
            self.rect.right = screen_width
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
        self.y_speed = 0
    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y



