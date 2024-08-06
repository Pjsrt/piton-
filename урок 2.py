import pygame
screem = pygame.display.set_mode((500, 500))
x = 25
dx = 1
while True:
    screem.fill((0,0,0))
    for event in pygame.event.get():
        pass
    if x >= 450:
        dx *= -1
    if x <= 0:
        dx *= -1
    
    pygame.draw.rect(screem, (255, 0, 0), (x, 240, 50, 50))
    x += dx
    pygame.display.update() 
    pygame.time.delay(2)