import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((900, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x=0
y=0
r=0
A=[]
dx=0
dy=0
number = 0
def new_balls():
    '''
    Функция рисует 10 шариков и создаёт эффект их движения
    '''
    for i in range(10):
        x = randint(100,500)
        y = randint(100,500)
        r = randint(30,50)
        color = COLORS[randint(0, 5)]
        dx = randint(-5,5)
        dy = randint(-5, 5)
        A.append([x,y,r,color,dx,dy])
    for i in range(10):
        circle(screen, A[i][3], (A[i][0], A[i][1]), A[i][2])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (event.x,event.y)=event.pos
            for i in range(10):
                if (event.x-A[i][0])**2+(event.y-A[i][1])**2<A[i][2]**2:
                    number+=1
                    A[i][0] = randint(100, 500)
                    A[i][1] = randint(100, 500)
                    A[i][2] = randint(30, 50)
                    A[i][3] = COLORS[randint(0, 5)]
                    A[i][4] = randint(-5, 5)
                    A[i][5] = randint(-5, 5)
    new_balls()
    for i in range(10):
        if A[i][0] < (900 - A[i][2]) and A[i][0] > A[i][2] and A[i][1] < (700 - A[i][2]) and A[i][1] > A[i][2]:
            A[i][0] = A[i][0] + A[i][4]
            A[i][1] = A[i][1] + A[i][5]
        elif A[i][0] >= (900 - A[i][2]) or A[i][0] <= A[i][2]:
            A[i][4] = -A[i][4]
            A[i][0] = A[i][0] + A[i][4]
            A[i][1] = A[i][1] + A[i][5]
        elif A[i][1] >= (700 - A[i][2]) or A[i][1] <= A[i][2]:
            A[i][5] = -A[i][5]
            A[i][0] = A[i][0] + A[i][4]
            A[i][1] = A[i][1] + A[i][5]

    pygame.display.update()
    screen.fill(BLACK)
print('Ваш счёт:', number)
pygame.quit()