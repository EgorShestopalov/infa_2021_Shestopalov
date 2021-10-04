

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
    n=1.95
    rect(screen,olive,(x,y,a//n,b//n))
    dx = a//9
    rect(screen, MoreDarkerGray, ((x + dx//n) , y, dx//n, 109//n))
    for i in range(3):
        rect(screen, MoreDarkerGray, (x+(3*dx+2*dx*i)//n,y,dx//n,109//n))
    rect(screen,brown,(x+23//n,y+202//n,40//n,50//n))
    rect(screen, brown, (x+86//n, y+202//n, 40//n, 50//n))
    rect(screen, yellow, (x+146//n, y+202//n, 40//n, 50//n))
    polygon(screen, black, [[x-19//n,y],[x+228//n,y],[x+194//n,y-23//n],[x+12//n,y-23//n]])
    rect(screen, VeryDarkGray, (x-7//n,y+73//n,226//n,12//n))
    rect(screen, VeryDarkGray, (x-19//n, y+111//n, 250//n, 29//n))
    rect(screen,VeryDarkGray ,(x-14//n,y+84//n,7//n,27//n))
    rect(screen, VeryDarkGray, (x+219//n, y+84//n, 7//n, 27//n))
    for i in range(5):
        rect(screen, VeryDarkGray, (11//n+x+38*i//n,y+84//n,13//n,27//n))
    rect(screen,VeryDarkGray,(x+41//n,y-73//n,14//n,64//n))
    rect(screen, VeryDarkGray, (x+176//n, y-51//n, 7//n, 42//n))
    rect(screen, VeryDarkGray, (x+30//n, y-40//n,7//n,28//n))
    rect(screen, VeryDarkGray, (x+124//n,y-34//n,7//n,11//n))

def ghost(x,y,m):
    polygon(screen,white,[[x,y],[x+29//m,y-3//m],[x+32//m,y+5//m],[x+41//m,y+16//m],[x+48//m,y+16//m],[x+65//m,y+3//m],[x+88//m,y+3//m],[x+92//m,y-3//m],[x+96//m,y-14//m],
                          [x+107//m,y-18//m],[x+112//m,y-22//m],[x+112//m,y-36//m],[x+61//m,y-74//m],[x+28//m,y-76//m]])
    circle(screen,white,(x+45//m,y-67//m),18//m)
    circle(screen, blue, (x+37//m, y-70//m), 5//m)
    circle(screen, blue, (x+50//m, y-72//m), 5//m)
    circle(screen, black, (x+35//m, y-70//m), 2//m)
    circle(screen, black, (x+48//m, y-72//m), 2//m)

def ghost2(x,y,m):
    polygon(screen, white, [[x, y], [x - 29 // m, y - 3 // m], [x - 32 // m, y + 5 // m], [x - 41 // m, y + 16 // m],
                            [x - 48 // m, y + 16 // m], [x - 65 // m, y + 3 // m], [x - 88 // m, y + 3 // m],
                            [x - 92 // m, y - 3 // m], [x - 96 // m, y - 14 // m],
                            [x - 107 // m, y - 18 // m], [x - 112 // m, y - 22 // m], [x - 112 // m, y - 36 // m],
                            [x - 61 // m, y - 74 // m], [x - 28 // m, y - 76 // m]])
    circle(screen, white, (x - 45 // m, y - 67 // m), 18 // m)
    circle(screen, blue, (x - 37 // m, y - 70 // m), 5 // m)
    circle(screen, blue, (x - 50 // m, y - 72 // m), 5 // m)
    circle(screen, black, (x - 35 // m, y - 70 // m), 2 // m)
    circle(screen, black, (x - 48 // m, y - 72 // m), 2 // m)

rect(screen, gray, (0,0, 397, 235))
circle(screen,white,(355,49),35)
cloud(DarkerGray,174,35,225,35)
cloud(MoreDarkerGray, 18,55,312,37)
cloud(DarkerGray, 236,84,322,32)
cloud(VeryDarkGray, 198,127,300,35)
house(135,207)
cloud(DarkerGray,-60,300,263,40)
house(8,264)
house(287,132)
ghost(270,487,1)
ghost(244,463,2)
ghost(333,369,2)
ghost(346,397,2)
ghost2(88,481,2)
ghost2(104,508,2)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()