# FRUIT NINJA #
# MP4: INTERACTIVE PROGRAMMING #
# AVA LAKMAZAHERI AND EMMA WESTERHOFF #
# SOFTWARE DESIGN FALL 2017 #

import random, pygame, sys, argparse, imutils, cv2, copy, math
import numpy as np
import inspect
from pygame.locals import *
from all_fruits import *
from Scoring import *

# Hand Tracking Parameters
threshold = 60                          #  BINARY threshold
blurValue = 41                          #  GaussianBlur parameter
bgSubThreshold = 50                     #  Background subtraction threshold
cap_region_x_begin=0.3                  #  Background region limit
cap_region_y_end=0.9                    #  Background region limit
isBgCaptured = 0                        #  Boolean: whether the background has been captured
center = (0,0)                          #  Default position for sword object
OBJMOTION = pygame.USEREVENT+1          #  User event when object detected

# Game Interface Parameters
black = (0, 0, 0)                       #  Define background color
screen_width = 800                      #  Define game screen size
screen_height = 500                     #  Define game screen size


def generate_fruit(screen):
    """
    Returns Apple, Banana, or Straberry object
    Fruit choice occurs randomly for maximum novelty in game experience
    """

    n = random.randint(1,3)
    if n == 1:
        return Apple(screen)
    elif n == 2:
        return Banana(screen)
    else:
        return Strawberry(screen)

def half_fruit(screen, fruit):
    """
    Returns two fruit halves based on classification of fruit object input
    """
    halves = []

    if isinstance(fruit, Apple):
        halves = [Half_Apple1(screen, fruit.x, fruit.y), Half_Apple2(screen, fruit.x, fruit.y)]
    elif isinstance(fruit, Banana):
        halves = [Half_Banana1(screen, fruit.x, fruit.y), Half_Banana2(screen, fruit.x, fruit.y)]
    elif isinstance(fruit, Strawberry):
        halves = [Half_Strawberry1(screen, fruit.x, fruit.y), Half_Strawberry2(screen, fruit.x, fruit.y)]
    return halves

def printThreshold(thr):
    """
    Helper function for background removal/object detection
    """
    print("Changed threshold to " + str(thr))

def removeBG(frame, bgModel):
    """
    Subtracts background model (defined by user-keyed screen capture) from current frame
    Returns resulting frame
    """
    fgmask = bgModel.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    return res


def obj_tracker(frame, bgModel):
    """
    Perform background removal and object detection in current frame
    """

    img = removeBG(frame, bgModel)                                              # Remove background from current scaled frame
    img = img[0:int(cap_region_y_end * frame.shape[0]), int(cap_region_x_begin*
        frame.shape[1]):frame.shape[1]]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Convert image to binary
    blur = cv2.GaussianBlur(gray, (blurValue, blurValue), 0)                    # Apply Gaussian Blur
    #cv2.imshow('Blur', blur)
    ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow('Original', thresh)

    thresh1 = copy.deepcopy(thresh)                                             # Get contours
    _, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)

    length = len(contours)
    maxArea = -1
    if length > 0:                                                              # If any contours were found:
        for i in range(length):                                                 # Find the largest area contour
            temp = contours[i]                                                      # Isolate one contour
            area = cv2.contourArea(temp)                                            # Find area
            if area > maxArea:                                                      # If greater than max (-1 originally)
                maxArea = area                                                      # Update max area
                ci = i                                                              # Store index
        res = contours[ci]                                                      # Isolate contour at index

        hull = cv2.convexHull(res)                                              # Find region that encloses contour
        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)                     # Draw contour
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)                    # Draw enclosing region

        M = cv2.moments(res)                                                    # Find image moments (spatial distribution of object)
        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))       # Center of mass of detected object
        except:                                                                 # Reset sword position if moment m00 is returned as 0s
            center = (0, 0)
            print("Can't divide by 0!")

        cv2.circle(drawing, center, 8, [100, 100, 100], -1)                     # Draw center of object -- sword location
        my_event = pygame.event.Event(OBJMOTION, message="Object detected!",    # Create object detection event with sword location parameter
            center = center)
        pygame.event.post(my_event)                                             # Post event

        cv2.imshow('Object Detection', drawing)                                 # Show drawing of contour, hull, and center

def get_background():
    """
    Before Fruit Ninja begins, the system must be calibrated to the player's webcam background.
    This function displays the user's background and waits for them to press 'b' to set calibration
    """
    camera = cv2.VideoCapture(0)                                                # Start video capture with webcam
    camera.set(10,200)

    while True:
        (grabbed, frame) = camera.read()
        frame = imutils.resize(frame, width=1000)                               #  Resize frame
        frame = cv2.bilateralFilter(frame, 5, 50, 100)                          #  Apply smoothing filter
        frame = cv2.flip(frame, 1)                                              #  Flip frame horizontally for intuitive motion
        cv2.rectangle(frame, (int(cap_region_x_begin * frame.shape[1]), 0),
            (frame.shape[1], int(cap_region_y_end * frame.shape[0])), (255, 0, 0), 2)
        cv2.imshow('Webcam', frame)                                             #  Display background area for user

        k = cv2.waitKey(1) & 0xFF
        if k == 27:                                                             # Press ESC key to exit
            sys.exit()
        if k == ord('b'):                                                       # Press 'b' to capture background
            bgModel = cv2.createBackgroundSubtractorMOG2(0, bgSubThreshold)     # Generate background model from current frame
            print('Background Captured')
            break

    return camera, bgModel


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))             # Set up PyGame screen

    scoreboard = Scoreboard(screen)
    pygame.display.set_caption('Fruit Ninja')
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    camera, bgModel = get_background()                                          # Wait for user to calibrate background

    fruits = [generate_fruit(screen)]                                           # Generate fruit and sword objects
    fruit_parts = []
    sword = Sword(0,0,screen)
    x = y = 0

    while True:
        time_passed = clock.tick(30)
        screen.fill(black)

        (grabbed, frame) = camera.read()                                        # Read from camera
        frame = imutils.resize(frame, width=1000)
        frame = cv2.bilateralFilter(frame, 5, 50, 100)                          # Apply smoothing filter
        frame = cv2.flip(frame, 1)                                              # Flip the frame horizontally
        obj_tracker(frame, bgModel)                                             # Live object detection!

        for event in pygame.event.get():                                        # Check for events
            if event.type == QUIT:                                              # Allow the user to end the game at any time
                pygame.quit()
                sys.exit()
            elif event.type == OBJMOTION:                                       # Get hand position from object detection
                pygame.event.clear()
                x,y = event.center

        sword.move(x,y)                                                         # Move sword to hand position
        sword.draw()                                                            # Draw sword on screen

        if len(fruits) == 0:                                                    # Make sure there is always fruit on the screen!
            fruits.append(generate_fruit(screen))

        for a in fruits:
            a.toss(time_passed)                                                 # Launch fruit into projectile motion
            a.move(a.x, a.y)                                                    # Update fruit position for collisions
            a.draw()                                                            # Draw fruit in updated position

            # COLLISION DETECTION
            # If fruit position and sword position (centroid of hand object) are in the same location, we have hit fruit
            if a.checkCollision(sword):
                print("COLLIDE")
                scoreboard.fruit_sliced +=1                                     # Add to scoreboard
                halves = half_fruit(screen, a)                                  # Split fruit --> generate halved objects
                for half in halves:
                    fruit_parts.append(half)
                #print(fruit_parts)
                fruits.remove(a)                                                # Remove original fruit
            elif a.y > (screen_height+a.image.get_width()):                     # If the fruit fell off screen without being hit...
                print('Missed')
                #print(scoreboard.fruit_missed)
                scoreboard.fruit_missed +=1                                     # Count as missed object
                fruits.remove(a)

        for h in fruit_parts:                                                   # Have all split fruit fall down screen
            h.fall(time_passed)
            h.move(h.x, h.y)
            h.draw()
            if h.y > (screen_height+h.image.get_width()):
                fruit_parts.remove(h)

        scoreboard.show()
        pygame.display.update()                                                 # Update screen display

        k = cv2.waitKey(1) & 0xFF
        if k == 27:                                                             # ESC key to exit
            sys.exit()
            camera.release()                                                    # End/close webcam display
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()
