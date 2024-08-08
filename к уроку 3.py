import pygame
import random

class Rect:
    def __init__(self,width, height):
        self.x = random.randint(1,449)
        self.y = 225
        self.dx = random.randint(5,10)
        self.width = height
        self.height = width

screem = pygame.display.set_mode((500,500))
v = 255
x = 225
dx = 1
#random.randint(x,y) - рандом от x до y 
num_rects = random.randint(3,5)

rects = [Rect(50,50) for i in range(num_rects)]
while True:
    screem.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and v > 0:
                v -= 5
    if keys[pygame.K_s] and v < 465:
                v += 5
    if keys[pygame.K_d] and x < 465:
                x += 5
    if keys[pygame.K_a] and x > 0:
                x -= 5
    
    for i in range(len(rects)):
        if rects[i].x >= 465 or rects[i].x <= 0:
            rects[i].dx = -rects[i].dx
        rects[i].x += rects[i].dx
        pygame.draw.rect(screem,(255,0,0),(rects[i].x,rects[i].y,rects[i].width,rects[i].height))
    pygame.draw.rect(screem,(0,150,0),(x,v,35,35))
    pygame.display.update()
    pygame.time.delay(15)
    