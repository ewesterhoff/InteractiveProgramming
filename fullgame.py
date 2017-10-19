import random, pygame, sys
from pygame.locals import *
from fruits import Apple, Sword

#            R    G    B
gray     = (100, 100, 100)
navyblue = ( 60,  60, 100)
white    = (255, 255, 255)
red      = (255,   0,   0)
green    = (  0, 255,   0)
blue     = (  0,   0, 255)
yellow   = (255, 255,   0)
orange   = (255, 128,   0)
purple   = (255,   0, 255)
cyan     = (  0, 255, 255)
black    = (  0,   0,   0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Shitty Fruit Ninja')
    fruits = generate_fruit(screen, 3)
    pygame.mouse.set_visible(False)
    sword = Sword(0,0,screen)

    while True:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos

        # move sword to mouse position
        sword.move(x,y)
        sword.draw()

        for a in fruits:
            a.draw()
            if a.checkCollision(sword):
                print("COLLIDE")
                fruits.remove(a)

        pygame.display.update()

def generate_fruit(screen, n):
    positions = []
    radii = []
    colors = []
    fruits = []

    start_x = random.sample(range(20, 370), n)
    start_y = random.sample(range(20, 370), n)

    for b in range(0, n):
        positions.append((start_x[b], start_y[b]))

    for i in range(0, n):
        radii.append(random.randint(8, 20))

    set_colors = [red, green, gray]
    for j in range(0,n):
        c = random.choice(set_colors)
        colors.append(c)

    for a in range(0,n):
        temp_apple = Apple(radii[a], 1, positions[a], screen, colors[a])
        print(radii[a])
        print(positions[a])
        print(colors[a])
        fruits.append(temp_apple)

    return fruits

if __name__ == "__main__":
    main()
