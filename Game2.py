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
A=[0,0,0,0,0,0,0,0,0,0]
B=[0]*10
dx=0
dy=0
number = 0
screen = pygame.display.set_mode((900, 700))
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
        A[i]=[x,y,r,color,dx,dy]


def draw_ball():
    for i in range(10):
        circle(screen, A[i][3], (A[i][0], A[i][1]), A[i][2])

def new_ring():
    for i in range(2):
        x = randint(100,300)
        y = randint(100,300)
        r = randint(40,60)
        color = COLORS[randint(0, 5)]
        dx = randint(-5,5)
        dy = randint(-5, 5)
        B[i]=[x,y,r,color,dx,dy]

def draw_ring():
    for i in range(2):
        circle(screen, B[i][3], (B[i][0], B[i][1]), B[i][2],20)

def move_balls():
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

def move_rings():
    for i in range(2):
        if B[i][0] < (900 - B[i][2]) and B[i][0] > B[i][2] and B[i][1] < (700 - B[i][2]) and B[i][1] > B[i][2]:
            B[i][0] = B[i][0] + B[i][4]
            B[i][1] = B[i][1] + B[i][5]
            B[i][3]=COLORS[randint(0, 5)]
        elif B[i][0] >= (900 - B[i][2]) or B[i][0] <= B[i][2]:
            B[i][4] = -B[i][4]
            B[i][0] = B[i][0] + B[i][4]
            B[i][1] = B[i][1] + B[i][5]
            B[i][3] = COLORS[randint(0, 5)]
        elif B[i][1] >= (700 - B[i][2]) or B[i][1] <= B[i][2]:
            B[i][5] = -B[i][5]
            B[i][0] = B[i][0] + B[i][4]
            B[i][1] = B[i][1] + B[i][5]
            B[i][3] = COLORS[randint(0, 5)]

def score_to_screen(score):
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(score), False, (0, 180, 0))
    screen.blit(textsurface, (10, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_balls()
new_ring()
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
            for i in range(2):
                if (event.x-B[i][0])**2+(event.y-B[i][1])**2<B[i][2]**2 and (event.x-B[i][0])**2+(event.y-B[i][1])**2>=(B[i][2]-20)**2:
                    B[i][0] = randint(100, 300)
                    B[i][1] = randint(100, 300)
                    B[i][2] = randint(30, 50)
                    B[i][3] = COLORS[randint(0, 5)]
                    B[i][4] = randint(-5, 5)
                    B[i][5] = randint(-5, 5)
                    number+=7
    draw_ball()
    draw_ring()
    move_balls()
    move_rings()
    score_to_screen(number)
    pygame.display.update()
    screen.fill(BLACK)
print('Ваш счёт:', number)
pygame.quit()