# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *
from fruits import Apple

#            R    G    B
gray     = (100, 100, 100)
navyblue = ( 60,  60, 100)
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   =  (255, 255,  0)
orange   = (255, 128,   0)
purple   = (255,   0, 255)
cyan     = (  0, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Shitty Fruit Ninja')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        fruits = generate_fruit(screen)

        for a in fruits:
            a.draw()
        pygame.display.update()

def generate_fruit(screen):
    apple1 = Apple(20, 1, (40,60), screen, red)
    apple2 = Apple(12, 1, (150,120), screen, green)
    fruits = [apple1, apple2]
    return fruits

if __name__ == "__main__":
    main()
