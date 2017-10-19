import random, pygame, sys
from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)

class Apple(pygame.sprite.Sprite):
    def __init__(self, speed, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.screen = screen

        self.image =  pygame.image.load("apple.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        self.y -= time_passed * self.speed

    def projectile(self, time_passed):
        #TODO: go up, then come back down
        self.x += (direction*speed)*time_passed*cos(theta)
        self.y += (direction*speed)*time_passed*sin(theta) - .5(g)(time_passed**2)
        pass

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def checkCollision(self, other):
        # returns True or False if apple has collided with other object
        col = pygame.sprite.collide_rect(self, other)
        return col

class Banana(pygame.sprite.Sprite):
    def __init__(self, speed, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.screen = screen

        self.image =  pygame.image.load("banana.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        self.y -= time_passed * self.speed

    def projectile(self, time_passed):
        #TODO: go up, then come back down
        self.x += (direction*speed)*time_passed*cos(theta)
        self.y += (direction*speed)*time_passed*sin(theta) - .5(g)(time_passed**2)
        pass

    def draw(self):
        # draw circle on Sprite surface
        #draw_pos = self.rect.move(self.x-self.screen.get_width(), self.y - self.screen.get_height())
        self.screen.blit(self.image, (self.x, self.y))
        #self.screen.fill(green, self.rect)
        #pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def checkCollision(self, other):
        # returns True or False if apple has collided with other object
        col = pygame.sprite.collide_rect(self, other)
        return col

class Strawberry(pygame.sprite.Sprite):
    def __init__(self, speed, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.screen = screen

        self.image =  pygame.image.load("strawberry.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        self.y -= time_passed * self.speed

    def projectile(self, time_passed):
        #TODO: go up, then come back down
        self.x += (direction*speed)*time_passed*cos(theta)
        self.y += (direction*speed)*time_passed*sin(theta) - .5(g)(time_passed**2)
        pass

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

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
        self.rect.centerx = x
        self.rect.centery = y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def printrect(self):
        print(self.rect.centerx, ", ", self.rect.centery)
