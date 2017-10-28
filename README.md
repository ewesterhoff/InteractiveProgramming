# Interactive Programming

Software Design MP4 <br />
Hand-Tracking Fruit Ninja

In this immersive gaming experience, Fruit Ninja moves off of your phone screen and into 3D! Swipe your hand through space and slice the fruit on the screen in real time. The game is infinite, and so is the fun.

## Getting Started:

### Installing Packages
This game makes use of OpenCV and Pygame libraries. For everything you need, run the following. <br />

pip install cv2, pygame, numpy, imutils, argparse

### Downloading Files
Download the following files, as well as all fruit images, from the repository: <br />

ninja.py: main game file <br />
all_fruits.py: holds fruit class and apple, banana, strawberry subclasses <br />
Scoring.py: holds scoreboard class <br />

### Usage
To run the game, run ninja.py with Python 3.

### Calibration
The game requires a still image from the webcam to begin hand detection. A camera display will pop up when you run ninja.py, in which the captured frame is contained within the blue rectangle. Make sure your hand is not in this area! Click on the webcam screen and press "b" on the keyboard when you're ready to take a picture. <br />

When the image has been taken, you're ready to play! Navigate to the game screen and slice the fruit by gesturing. Try to keep the rest of the background as static as possible for the best results (i.e., don't move your computer, have people walking behind you, etc.) <br />

Enjoy!
