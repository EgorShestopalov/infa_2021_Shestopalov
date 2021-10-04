

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((397, 561))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255,255,0)
gray = (153,153,153)
DarkerGray = (128,128,128)
MoreDarkerGray = (100,100,100)
VeryDarkGray = (80,80,80)
olive=(50,50,0)
brown=(139,69,19)

def cloud(colour, x , y, a, b):
    ellipse(screen, colour, (x,y,a,b))

def house(x,y):
    a = 207
    b = 286
    rect(screen,olive,(x,y,a,b))
    dx = a//9
    rect(screen, MoreDarkerGray, (x + dx , y, dx, 109))
    for i in range(3):
        rect(screen, MoreDarkerGray, (x+3*dx+2*dx*i,y,dx,109))
    rect(screen,brown,(x+23,y+202,40,50))
    rect(screen, brown, (x+86, y+202, 40, 50))
    rect(screen, yellow, (x+146, y+202, 40, 50))
    polygon(screen, black, [[x-19,y],[x+228,y],[x+194,y-23],[x+12,y-23]])
    rect(screen, VeryDarkGray, (x-7,y+73,226,12))
    rect(screen, VeryDarkGray, (x-19, y+111, 250, 29))
    rect(screen,VeryDarkGray ,(x-14,y+84,7,27))
    rect(screen, VeryDarkGray, (x+219, y+84, 7, 27))
    for i in range(5):
        rect(screen, VeryDarkGray, (11+x+38*i,y+84,13,27))
    rect(screen,VeryDarkGray,(x+41,y-73,14,64))
    rect(screen, VeryDarkGray, (x+176, y-51, 7, 42))
    rect(screen, VeryDarkGray, (x+30, y-40,7,28))
    rect(screen, VeryDarkGray, (x+124,y-34,7,11))

def ghost(x,y):
    polygon(screen,white,[[x,y],[x+29,y-3],[x+32,y+5],[x+41,y+16],[x+48,y+16],[x+65,y+3],[x+88,y+3],[x+92,y-3],[x+96,y-14],
                          [x+107,y-18],[x+112,y-22],[x+112,y-36],[x+61,y-74],[x+28,y-76]])
    circle(screen,white,(x+45,y-67),18)
    circle(screen, blue, (x+37, y-70), 5)
    circle(screen, blue, (x+50, y-72), 5)
    circle(screen, black, (x+35, y-70), 2)
    circle(screen, black, (x+48, y-72), 2)

rect(screen, gray, (0,0, 397, 235))
circle(screen,white,(355,49),35)
cloud(DarkerGray,174,35,225,35)
cloud(MoreDarkerGray, 18,55,312,37)
cloud(DarkerGray, 236,84,322,32)
cloud(VeryDarkGray, 198,127,300,35)
house(19,123)
ghost(270,487)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()