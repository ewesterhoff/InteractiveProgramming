import random, pygame, sys, math
from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)

class Apple(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = .3
        self.screen = screen
        self.total_time = 0
        self.time = 0

        self.image =  pygame.image.load("apple.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

        #figure out direction to fruit to move based on spawn position (left or right)
        border = screen.get_width()/2
        #if starts to the left, move over right
        if (self.x < border):
            self.direction = 1
        #if starts over on the right, move left
        else:
            self.direction = -1

        #determine realistic trajectory angle that will clear minimum height and not exceed maximum
        min_height = .6*screen.get_height()
        max_height = .9*screen.get_height()

        start_distance_from_border = abs(self.x - border)
        distance_from_border = random.randint(0, int(start_distance_from_border))

        try:
            min_angle = math.atan(min_height/distance_from_border)
            max_angle = math.atan(max_height/distance_from_border)

            self.angle = random.randint(int(min_angle), int(max_angle))
        except:
            self.angle = math.pi/2

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        #self.y -= self.speed*time_passed
        self.total_time = self.total_time+time_passed
        self.time = self.total_time/300

        x_speed = random.randint(0,25)
        add_x = math.sin(self.time) * x_speed
        self.x += self.direction*add_x

        y_speed = random.randint(120,170)
        add_y = math.cos(self.time) * self.speed*y_speed
        self.y -= add_y


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def checkCollision(self, other):
        # returns True or False if apple has collided with other object
        col = pygame.sprite.collide_rect(self, other)
        return col

class Banana(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = .3
        self.screen = screen
        self.total_time = 0
        self.time = 0

        self.image =  pygame.image.load("banana.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

        #figure out direction to fruit to move based on spawn position (left or right)
        border = screen.get_width()/2
        #if starts to the left, move over right
        if (self.x < border):
            self.direction = 1
        #if starts over on the right, move left
        else:
            self.direction = -1

        #determine realistic trajectory angle that will clear minimum height and not exceed maximum
        min_height = .6*screen.get_height()
        max_height = .9*screen.get_height()

        start_distance_from_border = abs(self.x - border)
        distance_from_border = random.randint(0, int(start_distance_from_border))

        try:
            min_angle = math.atan(min_height/distance_from_border)
            max_angle = math.atan(max_height/distance_from_border)

            self.angle = random.randint(int(min_angle), int(max_angle))
        except:
            self.angle = math.pi/2

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        #self.y -= time_passed * self.speed
        self.total_time = self.total_time+time_passed
        self.time = self.total_time/300

        x_speed = random.randint(0,25)
        add_x = math.sin(self.time) * x_speed
        self.x += self.direction*add_x

        y_speed = random.randint(120,170)
        add_y = math.cos(self.time) * self.speed*y_speed
        self.y -= add_y

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
    def __init__(self, screen):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.speed = .3
        self.screen = screen
        self.total_time = 0
        self.time = 0

        self.image =  pygame.image.load("strawberry.png").convert_alpha()
        self.image.set_colorkey(white)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.x = random.randint(0, self.screen.get_width()-int(self.image.get_width()/2))
        self.y = self.screen.get_height()+self.image.get_width()

        self.rect.centerx = self.x + (self.image.get_width()/2)
        self.rect.centery = self.y + (self.image.get_height()/2)

        #figure out direction to fruit to move based on spawn position (left or right)
        border = screen.get_width()/2
        #if starts to the left, move over right
        if (self.x < border):
            self.direction = 1
        #if starts over on the right, move left
        else:
            self.direction = -1

        #determine realistic trajectory angle that will clear minimum height and not exceed maximum
        min_height = .6*screen.get_height()
        max_height = .9*screen.get_height()

        start_distance_from_border = abs(self.x - border)
        distance_from_border = random.randint(0, int(start_distance_from_border))

        try:
            min_angle = math.atan(min_height/distance_from_border)
            max_angle = math.atan(max_height/distance_from_border)

            self.angle = random.randint(int(min_angle), int(max_angle))
        except:
            self.angle = math.pi/2

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = x + (self.image.get_width()/2)
        self.rect.centery = y + (self.image.get_height()/2)

    def fall(self, time_passed):
        #self.y -= time_passed * self.speed
        self.total_time = self.total_time+time_passed
        self.time = self.total_time/300

        x_speed = random.randint(0,25)
        add_x = math.sin(self.time) * x_speed
        self.x += self.direction*add_x

        y_speed = random.randint(120,170)
        add_y = math.cos(self.time) * self.speed*y_speed
        self.y -= add_y

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
