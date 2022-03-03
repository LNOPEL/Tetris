import pygame
import random
import time
import sys

pygame.init()

screen_width = 300
screen_height = 600
score = 0
level = 1

cyan = (24, 217, 204)
orange = (245, 169, 37)
red = (255, 0, 0)
blue = (66, 135, 245)
purple = (149, 24, 217)
green = (40, 184, 50)
yellow = (240, 232, 14)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris game screen")

from blocks import Blocks
from straight_block import Straight_Block
from l_block import L_Block
from reverse_l_block import Reverse_L_Block
from square_block import Square_Block
from t_block import T_Block
from z_block import Z_Block
from reverse_z_block import Reverse_Z_Block
from checker_sprite import Checker_Sprite
from around_checker_sprite import Around_Checker_Sprite
from words import draw_text
from special_block_explosion_block import Special_Block_Explosion_Block


def at_bottom(piece):
    for block in piece.get_blocks():
        if pygame.sprite.spritecollide(block, frozen_sprites, False):
            # print("in here")
            return True
        if block.rect.bottom >= 600:
            # print(block.rect.bottom, block.rect.top)
            return True

    return False


# function that generates random block
def gen_block(all_sprites, level=1):
    # create a random block adds to all_sprites
    # and returns the block that was created

    # debuggin gonly

    straight_block = Straight_Block(100, 20, 200 // level)
    l_block = L_Block(100, 20, 200 // level)
    reverse_l_block = Reverse_L_Block(100, 20, 200 // level)
    square_block = Square_Block(100, 20, 200 // level)
    t_block = T_Block(100, 20, 200 // level)
    z_block = Z_Block(100, 20, 200 // level)
    reverse_z_block = Reverse_Z_Block(100, 20, 200 // level)
    special_block_explosion_block = Special_Block_Explosion_Block(100, 20, 200 // level)

    block_list = [straight_block, special_block_explosion_block]
    random_number = random.randint(0, len(block_list) - 1)
    generation = block_list[random_number]

    # once pieces hit the bottom they leave moving_sprites
    for block in generation.get_blocks():
        print(block)
        print(generation, generation.get_blocks())
        all_sprites.add(block)

    return generation


def explosion(all_sprites):
    pass


all_sprites = pygame.sprite.Group()
frozen_sprites = pygame.sprite.Group()
special_sprites = pygame.sprite.Group()
# special_sprites.add(Special_Block_Explosion_Block)
piece = gen_block(all_sprites)

single = 100
double = 300
triple = 500
tetris = 900

# game loop
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if at_bottom(piece):
        for block in piece.get_blocks():
            frozen_sprites.add(block)

        checker_sprite = Checker_Sprite(150, 590)
        around_checker_sprite = Around_Checker_Sprite(0, 590)
        deleted_rows = 0
        # collision check is the list of blocks
        # on a given row of the game
        collision_check = pygame.sprite.spritecollide(checker_sprite, frozen_sprites, False)

        lines = 0
        check_group = pygame.sprite.Group()
        checker_sprite.add(check_group)
        around_checker_sprite.add(check_group)

        while collision_check:
            block_count = 0
            exploding_blocks = set()
            # Find all the blocks next to explosion blocks, add them to the list, and then delete them
            for collision in collision_check:
                # collision is the block that is frozen
                block_count += 1
                around_checker_sprite.x = collision.x
                around_checker_sprite.y = collision.y
                around_checker_sprite.x = collision.x + 30
                explosion_check = pygame.sprite.spritecollide(around_checker_sprite, frozen_sprites, False)
                for blocks in explosion_check:
                    exploding_blocks.add(blocks)

                around_checker_sprite.y = collision.y - 30
                explosion_check = pygame.sprite.spritecollide(around_checker_sprite, frozen_sprites, False)
                for blocks in explosion_check:
                    exploding_blocks.add(blocks)

                around_checker_sprite.x = collision.x - 30
                explosion_check = pygame.sprite.spritecollide(around_checker_sprite, frozen_sprites, False)
                for blocks in explosion_check:
                    exploding_blocks.add(blocks)

                around_checker_sprite.y = collision.y + 30
                explosion_check = pygame.sprite.spritecollide(around_checker_sprite, frozen_sprites, False)

                for blocks in exploding_blocks:
                    all_sprites.remove(blocks)

                explosion_check = pygame.sprite.spritecollide(around_checker_sprite, frozen_sprites, False)
                print("There are", len(explosion_check), "exploding collisions")
                print(around_checker_sprite.x, around_checker_sprite.y)

                # check (210, 570) -- phantom block

                # check if the around_checking_sprite is in the correct coordinate #
                # HW: fix repeats of the list.
                # explosion_blocks = set()
                # explosion_blocks.add(blocks)


                if len(explosion_check) != 0:
                    for collision in explosion_check:
                        frozen_sprites.remove(collision)


                        all_sprites.remove(collision)
                        print(collision)

            print(block_count, checker_sprite.rect.y)
            if block_count >= 10:
                for collision in collision_check:
                    frozen_sprites.remove(collision)

                    all_sprites.remove(collision)
                    print(collision)
                deleted_rows += 1


            else:
                for collision in collision_check:
                    collision.rect.y += deleted_rows * 30
            checker_sprite.rect.y -= 30
            collision_check = pygame.sprite.spritecollide(checker_sprite, frozen_sprites, False)
            lines += 1
            # if too many lines, end the game
            if lines >= 18:
                print("Your final score is" , score)
                pygame.quit()
                sys.exit()
        piece = gen_block(all_sprites, level)
        if deleted_rows == 1:
            score += single
        if deleted_rows == 2:
            score += double
        if deleted_rows == 3:
            score += triple
        if deleted_rows == 4:
            score += tetris

    level = 1.5 ** (score // 700)

    for block in piece.get_blocks():
        hits = pygame.sprite.spritecollide(block, frozen_sprites, False)

    piece.update()

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)
    pygame.display.flip()