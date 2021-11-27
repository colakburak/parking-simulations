import pygame, math, time

from pygame import image
from pygame.transform import scale
from utils import *

WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CAR_WIDTH, CAR_HEIGHT = 200, 350
BLACK_CAR_IMAGE = pygame.image.load("imgs/black-car.png")
BLACK_CAR = pygame.transform.scale(BLACK_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT))

RECT_WIDTH, RECT_HEIGHT = 50, 85
RECT_IMAGE = pygame.image.load("imgs/rect.png")
RECT = pygame.transform.scale(RECT_IMAGE, (RECT_WIDTH, RECT_HEIGHT))
RECT_MASK = pygame.mask.from_surface(RECT)

CIRCLE_RADIUS = 50
CIRCLE_IMAGE = pygame.image.load("imgs/circle.png")
CIRCLE = pygame.transform.scale(CIRCLE_IMAGE, (CIRCLE_RADIUS, CIRCLE_RADIUS))
CIRCLE_MASK = pygame.mask.from_surface(CIRCLE)

pygame.display.set_caption("Parking Simulation")


class Car:
    def __init__(self, rotation_vel):
        self.img = self.IMG
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
    
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    
    def move_foward(self):
        self.vel +=10
        self.move()
    
    def move_backward(self):
        self.vel -=10
        self.move_back()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians)
        horizontal = math.sin(radians) 

        self.y -= vertical * 3
        self.x -= horizontal * 3

    def move_back(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians)
        horizontal = math.sin(radians)

        self.y += vertical * 3
        self.x += horizontal * 3

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi


class Driver(Car):
    IMG = BLACK_CAR
    START_POS = (400,400)

    def bounce(self):
        self.vel = 0
        self.move()


RECT_X = 300
RECT_Y = 200
CIRCLE_X = 200
CIRCLE_Y = 200

images = [(RECT, (RECT_X, RECT_X)) ,(CIRCLE, (CIRCLE_X, CIRCLE_Y)), (RECT, (RECT_X+500, RECT_X+100)), (RECT, (RECT_X+300, RECT_X+300)), (CIRCLE, (CIRCLE_X+600, CIRCLE_Y+100)), (CIRCLE, (CIRCLE_X+1000, CIRCLE_Y))]
driver = Driver(4)

def draw(win, images, driver):
    for img, pos in images:
        win.blit(img, pos)
    driver.draw(win)

SKY_BLUE = (135, 206, 235)
FPS = 80
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    WIN.fill(SKY_BLUE)

    draw(WIN, images, driver)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        driver.rotate(left=True)
    if keys[pygame.K_RIGHT]:
        driver.rotate(right=True)
    if keys[pygame.K_UP]:
        driver.move_foward()
    if keys[pygame.K_DOWN]:
        driver.move_backward()

    # I need to use for loop to make this if statements much more easy but i dont have time for it sorry for your eyes :')
    if driver.collide(RECT_MASK, RECT_X, RECT_Y) != None:
        driver.bounce()
    if driver.collide(CIRCLE_MASK, CIRCLE_X, CIRCLE_Y) != None:
        driver.bounce()
    if driver.collide(RECT_MASK, RECT_X+500, RECT_X+100) != None:
        driver.bounce()
    if driver.collide(CIRCLE_MASK, CIRCLE_X+600, CIRCLE_Y+100) != None:
        driver.bounce()
    if driver.collide(RECT_MASK, RECT_X+300, RECT_X+300) != None:
        driver.bounce()
    if driver.collide(CIRCLE_MASK, CIRCLE_X+1000, CIRCLE_Y) != None:
        driver.bounce()
    
pygame.quit()