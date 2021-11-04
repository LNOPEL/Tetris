import pygame
pygame.init()

font_name = pygame.font.match_font('arial')

def draw_text(screen, text, size, x, y, color = (0,0,0)):
    # create font
    font = pygame.font.Font(font_name, size)

    # make something that we put the text on
    text_surface = font.render(text, True, color)
    # what we want to type
    # aliasing
    # the text color

    # get the rectangle that the text is written on
    text_rect = text_surface.get_rect()

    # set's the location of the rectangle
    text_rect.midtop = (x, y)

    # writes the score to the screen
    screen.blit(text_surface, text_rect)