# Memory Puzzle
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *
from fruits import *
from Scoring import *

#            R    G    B
gray     = (100, 100, 100)
black    = (  0,   0,   0)
navyblue = ( 60,  60, 100)
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   = (255, 255,   0)
orange   = (255, 128,   0)
purple   = (255,   0, 255)
cyan     = (  0, 255, 255)

def main():
    pygame.init()
    screen_width = 400
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    fruits = [generate_fruit(screen)]
    pygame.mouse.set_visible(False)
    sword = Sword(0,0,screen)

    while True:
        time_passed = clock.tick(30)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x,y = event.pos

        sword.move(x,y)
        sword.draw()

        if len(fruits) == 0:
            fruits.append(generate_fruit(screen))

        for a in fruits:
            a.fall(time_passed)
            a.move(a.x, a.y)
            a.draw()
            if a.checkCollision(sword):
                print("COLLIDE")
                scoreboard.fruit_sliced +=1
                fruits.remove(a)
            elif a.y < (-screen_height+a.image.get_width()):
                fruits.remove(a)

        scoreboard.show()
        pygame.display.update()

def generate_apple(screen):
    apple = Apple(.3, screen)
    return apple

def generate_banana(screen):
    banana = Banana(.3, screen)
    return banana

def generate_strawberry(screen):
    strawberry = Strawberry(.3, screen)
    return strawberry

def generate_fruit(screen):
    n = random.randint(1,1)
    print(n)
    if n == 1:
        return generate_apple(screen)
    elif n == 2:
        return generate_banana(screen)
    else:
        return generate_strawberry(screen)

if __name__ == "__main__":
    main()
