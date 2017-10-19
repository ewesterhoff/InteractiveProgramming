
import os
import sys
import math
import pygame
import pygame.mixer
from pygame.locals import *

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = pygame.image.load("balloon.jpg")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

width = 500
height = 300
pygame.init()
pygame.display.set_mode((width, height))

b1 = Balloon()
b2 = Balloon()


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif  pygame.sprite.spritecollide(b1, b2, False, pygame.sprite.collide_mask):
        print("sprites have collided!")
