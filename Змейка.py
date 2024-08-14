import pygame
import random

class Node:
    def __init__(self, x, y, d, size, parent, child, color):
        self.x = x
        self.y = y
        self.d = d
        self.size = size
        self.parent = parent
        self.child = child
        self.color = color
    def move(self):
        # 0-вверх, 1-вправо, 2-вниз, 3-влево
        if self.d == 0:
            dir =(0, -self.size)
        if self.d == 1:
            dir =(self.size, 0)
        if self.d == 2:
            dir =(0, self.size)
        if self.d == 3:
            dir =(-self.size, 0)
        self.x += dir[0]
        self.y += dir[1]
        if self.child:
            self.child.d = self.d
    
    def draw(self,sc):
        pygame.draw.rect(sc, self.color, (self.x * self.size, self.y * self.size, self.size, self.size))

def generate_apple(snake, num_cells_x, num_cells_y):
    all_cells = [i for i in range(num_cells_x * num_cells_y)]
    for cell in snake:
        all_cells.remove(cell.x + cell.y * num_cells_x)
    
    random_pos = all_cells[random.randint(0, len(all_cells))]
    x = random_pos % num_cells_x
    y = random_pos // num_cells_y
    return Node(x, y, -1, 50, None, None, (255,0,0))
    
WIDTH, HEIGHT = 500, 500
cell_size = 50
num_cells_x,num_cells_y = WIDTH // cell_size, HEIGHT // cell_size

snake =[Node(random.randint(2, num_cells_x - 2),
             random.randint(2, num_cells_y - 2),
             random.randint(0,3),
             cell_size,
             None,
             None,
             (0,255,0))]

apple = generate_apple(snake, num_cells_x, num_cells_y)

sc = pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    sc.fill((0,0,0))
    for event in pygame.event.get():
        pass
    
    for cell in snake:
        cell.draw(sc)
    apple.draw(sc)
    pygame.display.update()
    pygame.time.delay(1000)
