import random, pygame, sys
from pygame.locals import *

class Apple:
    def __init__(self, r, density, starting_position, screen, color):
        self.r = r
        self.density = density
        self.starting_position = starting_position
        self.screen = screen
        self.color = color

    def fall(density):
        #TODO: returns falling speed
        pass

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.starting_position, self.r)
