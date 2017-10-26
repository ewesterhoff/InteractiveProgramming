# FRUIT NINJA #
# AVA LAKMAZAHERI AND EMMA WESTERHOFF #
# SOFTWARE DESIGN FALL 2017 #

import random, pygame, sys, argparse, imutils, cv2, copy, math
import numpy as np
import inspect
from pygame.locals import *
from all_fruits import *
from Scoring import *

threshold = 60  #  BINARY threshold
blurValue = 41  # GaussianBlur parameter
bgSubThreshold = 50
black = (0, 0, 0)
cap_region_x_begin=0.3  # start point/total width
cap_region_y_end=0.9  # start point/total width
screen_width = 800
screen_height = 500
isBgCaptured = 0   # bool, whether the background captured

center = (0,0)
OBJMOTION = pygame.USEREVENT+1

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    camera, bgModel = get_background()

    return screen, scoreboard, clock, camera, bgModel

def generate_fruit(screen):
    n = random.randint(1,3)
    if n == 1:
        return Apple(screen)
    elif n == 2:
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
def printThreshold(thr):
    print("! Changed threshold to "+str(thr))
def removeBG(frame, bgModel):
    fgmask = bgModel.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res
def obj_tracker(frame, bgModel):
    img = removeBG(frame, bgModel)
    img = img[0:int(cap_region_y_end * frame.shape[0]), int(cap_region_x_begin * frame.shape[1]):frame.shape[1]]

    # convert the image into binary image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)
    #cv2.imshow('blur', blur)
    ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('ori', thresh)

    # get the coutours
    thresh1 = copy.deepcopy(thresh)
    _, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    maxArea = -1
    if length > 0: # only do the following if contours were found:
        for i in range(length):  # find the biggest contour (according to area)
            temp = contours[i]
            area = cv2.contourArea(temp)
            if area > maxArea:
                maxArea = area
                ci = i

        res = contours[ci]
        hull = cv2.convexHull(res)
        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

        M = cv2.moments(res)
        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        except:
            center = (0, 0)
            print("can't divide by 0")
        cv2.circle(drawing, center, 8, [100, 100, 100], -1)
        my_event = pygame.event.Event(OBJMOTION, message="Object detected!", center = center)
        pygame.event.post(my_event)

        cv2.imshow('output', drawing)

def get_background():
    camera = cv2.VideoCapture(0)
    camera.set(10,200)

    while True:
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=1000)
        frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
        frame = cv2.flip(frame, 1)  # flip the frame horizontally
        cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0), (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow('original', frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            sys.exit()
        if k == ord('b'):  # press 'b' to capture the background
            bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)
            print('!!!Background Captured!!!')
            break

    return camera, bgModel


def main():
    #screen, scoreboard, clock, camera, bgModel = initialize()
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    camera, bgModel = get_background()

    fruits = [generate_fruit(screen)]
    fruit_parts = []
    sword = Sword(0,0,screen)
    x = y = 0

    while True:
        time_passed = clock.tick(30)
        screen.fill(black)

        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=1000)
        frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
        frame = cv2.flip(frame, 1)  # flip the frame horizontally
        obj_tracker(frame, bgModel)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == OBJMOTION:
                pygame.event.clear()
                x,y = event.center

        sword.move(x,y)
        sword.draw()

        if len(fruits) == 0:
            fruits.append(generate_fruit(screen))

        for a in fruits:
            a.toss(time_passed)
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

        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            sys.exit()
            camera.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()
