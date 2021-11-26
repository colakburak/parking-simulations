import pygame, time, math

from pygame import image
from utils import *

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

CAR_WIDTH, CAR_HEIGHT = 60, 100
BLACK_CAR_IMAGE = pygame.image.load("imgs/black-car.png")
BLACK_CAR = pygame.transform.scale(BLACK_CAR_IMAGE, (CAR_WIDTH, CAR_HEIGHT))

RECT_WIDTH, RECT_HEIGHT = 50, 85
RECT_IMAGE = pygame.image.load("imgs/rect.png")
RECT = pygame.transform.scale(RECT_IMAGE, (RECT_WIDTH, RECT_HEIGHT))

CIRCLE_RADIUS = 50
CIRCLE_IMAGE = pygame.image.load("imgs/circle.png")
CIRCLE = pygame.transform.scale(CIRCLE_IMAGE, (CIRCLE_RADIUS, CIRCLE_RADIUS))


pygame.display.set_caption("Parking Simulation")


class Car:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
    
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
    
    def move_foward(self):
        #self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.vel +=0.1
        self.move()
    
    def move_backward(self):
        self.vel -=0.1
        self.moveb()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) #* self.vel
        horizontal = math.sin(radians) #* self.vel

        self.y -= vertical
        self.x -= horizontal

    def moveb(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) #* self.vel
        horizontal = math.sin(radians) #* self.vel

        self.y += vertical
        self.x += horizontal

class Driver(Car):
    IMG = BLACK_CAR
    START_POS = (400,400)


images = [(RECT, (300, 200)) ,(CIRCLE, (200,200))]
driver = Driver(4, 2)

def draw(win, images, driver):
    for img, pos in images:
        win.blit(img, pos)
    driver.draw(win)

SKY_BLUE = (135, 206, 235)
FPS = 60
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

    
pygame.quit()