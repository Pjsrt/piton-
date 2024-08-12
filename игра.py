import pygame
import random

class Rect:
    def __init__(self,width, height):
        self.x = random.randint(1,449)
        self.y = 70
        self.dx = random.randint(5,10)
        self.width = width
        self.height = height
        self.s = True
    def die(self):
        self.x = -100
        self.y = -100
        self.s = False

def kill_rocket():
    global rx,ry,rs
    rx = -100
    ry = -100
    rs = False

screem = pygame.display.set_mode((500,500))
y = 450
x = 225
dx = 1

rx = -100
ry = -100
rs = False
#random.randint(x,y) - рандом  диапозоне от x до y 
num_rects = random.randint(3,5)

rects = [Rect(50,50) for i in range(num_rects)]
while True:
    screem.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x < 450:
                x += 8
    if keys[pygame.K_a] and x > 0:
                x -= 8
    if keys[pygame.K_SPACE] and rs == False:
        rx = x + 50 // 4
        ry = y
        rs = True
    
    if ry <= 0:
        kill_rocket()

    if rs:
        pygame.draw.rect(screem,(255,0,0),(rx,ry,25,25))
        ry -= 9
    
    for i in range(len(rects)):
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].dx = -rects[i].dx
        if (rx >= rects[i].x and rx <= rects[i].x + rects[i].width or \
            rx + 25 <= rects[i].width and rx + 25 >= rects[i].x) and \
            ry <= rects[i].y + rects[i].height:
             kill_rocket()
             rects[i].die()
        
        if rects[i].s:
            rects[i].x += rects[i].dx
            pygame.draw.rect(screem,(0,0,150),(rects[i].x,rects[i].y,rects[i].width,rects[i].height))
    pygame.draw.rect(screem,(0,150,0),(x,y,50,50))
    pygame.display.update()
    pygame.time.delay(20)
    