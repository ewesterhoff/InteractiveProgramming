# FRUIT NINJA #
# AVA LAKMAZAHERI AND EMMA WESTERHOFF #
# SOFTWARE DESIGN FALL 2017 #

import random, pygame, sys, argparse, imutils, cv2
import numpy as np
from pygame.locals import *
from fruits import *
from Scoring import *
from collections import deque
#            R    G    B
black    = (  0,   0,   0)

# color_lowbound = (0, 0, 162)
# color_upbound = (255, 255, 255)
color_lowbound = (124, 58, 65)
color_upbound = (255, 189, 255)
camera = cv2.VideoCapture(0)
OBJMOTION = pygame.USEREVENT+1

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())
pts = deque(maxlen=args["buffer"])

def main():
    pygame.init()
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    fruits = [generate_fruit(screen)]
    pygame.mouse.set_visible(False)
    sword = Sword(0,0,screen)
    x = y = 0


    while True:
        time_passed = clock.tick(30)
        screen.fill(black)
        check_for_obj()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == OBJMOTION:
                pygame.event.clear()
                x,y = event.center
                r = event.radius

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

        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            break

def check_for_obj():
	(grabbed, frame) = camera.read()
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)

	# construct a mask for the color, then perform a series of dilations and erosions
	# to remove any small blobs left in the mask
	mask = cv2.inRange(frame, color_lowbound, color_upbound)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# print(radius)
		# only proceed if the radius meets a minimum size
		if radius > 10 and radius < 100:
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			my_event = pygame.event.Event(OBJMOTION, message="Object detected!", center = center, radius = radius)
			pygame.event.post(my_event)

	cv2.imshow("Frame", frame)


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
    n = random.randint(1,4)
    print(n)
    if n == 1:
        return generate_apple(screen)
    elif n == 2:
        return generate_banana(screen)
    else:
        return generate_strawberry(screen)

if __name__ == "__main__":
    main()
