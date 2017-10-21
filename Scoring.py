import random, pygame, sys, pygame.font
from pygame.locals import *

navyblue = (60,60,100)
white = (255,255,255)

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.fruit_sliced = 0
        self.fruit_missed = 0
        self.screen = screen

        self.sb_height, self.sb_width = 50, self.screen.get_width()
        self.rect = pygame.Rect(0,0, self.sb_width, self.sb_height)
        self.bg_color = navyblue
        self.text_color = white
        self.font = pygame.font.SysFont('Arial', 18)

        self.x_sliced_position, self.y_sliced_position = 20.0, 10.0
        self.x_missed_position, self.y_missed_position = self.screen.get_width()-100, 10.0

    def prep_scores(self):
        self.sliced_string = "Sliced: " + str(self.fruit_sliced)
        self.sliced_image = self.font.render(self.sliced_string, True, self.text_color)

        self.missed_string = "Missed: " + str(self.fruit_missed)
        self.missed_image = self.font.render(self.missed_string, True, self.text_color)

    def show(self):
        self.prep_scores()
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.sliced_image, (self.x_sliced_position, self.y_sliced_position))
        self.screen.blit(self.missed_image, (self.x_missed_position, self.y_missed_position))
