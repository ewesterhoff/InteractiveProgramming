import random, pygame, sys
from pygame.locals import *

class Apple(pygame.sprite.Sprite):
    def __init__(self, r, density, x, y, screen, color):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.r = r
        self.density = density
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color

        self.image = pygame.Surface([r, r])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.x = x
        self.y = y

    def fall(self, density):
        self.y = self.y + density

    def draw(self):
        # draw circle on Sprite surface
        #screen.blit(self.image, (self.x, self.y))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def checkCollision(self, other):
        # returns True or False if apple has collided with other object
        col = pygame.sprite.collide_rect(self, other)
        return col

class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen = screen

        self.image =  pygame.image.load("sword.png")
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
