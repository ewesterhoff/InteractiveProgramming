import pygame, sys
from fruits import Apple, Sword

bgcolor = 255, 255, 255
running = 1
x = y = 0
screen = pygame.display.set_mode((600, 400))
pygame.mouse.set_visible(False)

sword = Sword(x,y,screen)
myfruit = Apple(25, 0, (300, 200), screen, (255,0,0))

while True:
    screen.fill((0,0,0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        sys.exit()
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos

    sword.move(x,y)
    sword.draw()
    myfruit.draw()

    if myfruit.checkCollision(sword):
        myfruit.remove()
        print("COLLIDE")
    pygame.display.flip()
