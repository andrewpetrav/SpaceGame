import pygame
from Surface import SURFACE
from Spaceship import *
from Assets import *

pygame.init()

Player=Spaceship()
pygame.draw.rect(SURFACE,Player.color,Player.image)

while True:
    pygame.display.update()

def draw():
     pass
     r'''
     pygame.draw.rect(SURFACE, space.get_color(), space.get_image())
                pygame.draw.line(SURFACE,black_piece_color,(0,i*square_size),(square_size*self.boardLength,i*square_size))#These are the black lines separating squares
                pygame.draw.line(SURFACE,black_piece_color,(i*square_size,0),(i*square_size,square_size*self.boardWidth))
                if space.get_piece():
                    SURFACE.blit(space.get_piece_image(), (space.xpos, space.ypos))'
    '''