import os
import sys
import math
import pygame
import pygame.mixer
from pygame.locals import *

width = 500
height = 300
pygame.init()
pygame.display.set_mode((width, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if ball.get_rect().collidepoint(x, y):
                print("bam")
