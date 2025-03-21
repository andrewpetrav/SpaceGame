import pygame, sys
from pygame.locals import *
from Assets import *

WINDOWWIDTH=800
WINDOWHEIGHT=800
pygame.init()
SURFACE=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.RESIZABLE)
SURFACE.fill(BLACK)