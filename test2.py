import pygame

linecolor = 0, 0, 0
bgcolor = 255, 255, 255
x = y = 0
running = 1
screen = pygame.display.set_mode((600, 400))
pygame.mouse.set_visible(False)

sword = pygame.image.load("sword.png")
#sword2 = pygame.transform.scale(screen, (100, 200))


while running:
    screen.fill(bgcolor)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    #sword = pygame.draw.rect(screen, linecolor, [[x, y], [x+100, y],[x, y+10]], 2)
    #
    fruit = pygame.draw.circle(screen, (255,0,0), (320, 200), 10, 5)
    print(x, ", " , y)
    if sword.get_rect().collidepoint(320,200):
        print("bam")

    screen.blit(sword, (x,y))
    pygame.display.flip()
