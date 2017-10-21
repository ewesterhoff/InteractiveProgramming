# FRUIT NINJA #
# AVA LAKMAZAHERI AND EMMA WESTERHOFF #
# SOFTWARE DESIGN FALL 2017 #

import random, pygame, sys
from pygame.locals import *
#from fruits import *
from all_fruits import *
from Scoring import *
import inspect

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
    screen_width = 800
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    fruits = [generate_fruit(screen)]
    fruit_parts = []
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
            a.toss(time_passed)
            #a.projectile(time_passed)
            a.move(a.x, a.y)
            a.draw()
            if a.checkCollision(sword):
                print("COLLIDE")
                scoreboard.fruit_sliced +=1
                halves = half_fruit(screen, a)
                for half in halves:
                    fruit_parts.append(half)
                print(fruit_parts)
                fruits.remove(a)
            elif a.y > (screen_height+a.image.get_width()):
                print('missed')
                print(scoreboard.fruit_missed)
                scoreboard.fruit_missed +=1
                fruits.remove(a)

        for h in fruit_parts:
            h.fall(time_passed)
            h.move(h.x, h.y)
            h.draw()
            if h.y > (screen_height+h.image.get_width()):
                fruit_parts.remove(h)

        scoreboard.show()
        pygame.display.update()

def generate_fruit(screen):
    n = random.randint(1,3)
    if n == 1:
        return Apple(screen)
    if n == 2:
        return Banana(screen)
    else:
        return Strawberry(screen)

def half_fruit(screen, fruit):
    halves = []

    if isinstance(fruit, Apple):
        halves = [Half_Apple1(screen, fruit.x, fruit.y), Half_Apple2(screen, fruit.x, fruit.y)]
    elif isinstance(fruit, Banana):
        halves = [Half_Banana1(screen, fruit.x, fruit.y), Half_Banana2(screen, fruit.x, fruit.y)]
    elif isinstance(fruit, Strawberry):
        halves = [Half_Strawberry1(screen, fruit.x, fruit.y), Half_Strawberry2(screen, fruit.x, fruit.y)]
    return halves

if __name__ == "__main__":
    main()
