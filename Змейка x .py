import pygame
import random

class Node:
    def __init__(self, x, y, d, size, parent, child, color):
        self.x = x
        self.y = y
        self.d = d
        self.last_d  = None
        self.size = size
        self.parent = parent
        self.child = child
        self.color = color
        self.dir = None
     
    def move(self):
        # 0-вверх, 1-вправо, 2-вниз, 3-влево
        self.last_d = self.d
        if self.d == 0:
            self.dir =(0, -1)
        if self.d == 1:
            self.dir =(1, 0)
        if self.d == 2:
            self.dir =(0, 1)
        if self.d == 3:
            self.dir =(-1, 0)
        self.x += self.dir[0]
        self.y += self.dir[1]
        if self.parent is not None:
            self.d = self.parent.last_d
                
    def draw(self,sc):
        pygame.draw.rect(sc, self.color, (self.x * self.size, self.y * self.size, self.size, self.size))

    def add_child(self):
        if self.child is not None:
            return
        self.child = Node(self.x - self.dir[0],
                          self.y - self.dir[1],
                          self.d,
                          self.size,
                          self,
                          None,
                          self.color
                          )

def generate_apple(snake, num_cells_x, num_cells_y):
    all_cells = [i for i in range(num_cells_x * num_cells_y)]
    for cell in snake:
        all_cells.remove(cell.x + cell.y * num_cells_x)
    
    random_pos = all_cells[random.randint(0, len(all_cells))]
    x = random_pos % num_cells_x
    y = random_pos // num_cells_y
    return Node(x, y, -1, 50, None, None, (255,0,0))

def check_collision(snake, apple, num_cells_x, num_cells_y):
    head = snake[0]
    for i in range(len(snake)):
        if i == 0:
            continue
        if head.x == snake[i].x and head.y == snake[i].y:
            return 1
    if head.x > num_cells_x or head.x < 0 or head.y > num_cells_y or head.y < 0:
        return 1
    if head.x == apple.x and head.y == apple.y:
        return 2
    return None

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
timer = 1

while True:
    sc.fill((0,0,0))
    for event in pygame.event.get():
        pass
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake[0].d = 0
    if keys[pygame.K_d]:
        snake[0].d = 1
    if keys[pygame.K_s]:
        snake[0].d = 2
    if keys[pygame.K_a]:
        snake[0].d = 3
    if timer >= 50:
        for cell in snake:
            cell.move()
        timer = 0
    
    collisions = check_collision(snake, apple, num_cells_x, num_cells_y)
    if collisions == 1:
        break
    if collisions == 2:
        snake[-1].add_child()
        snake.append(snake[-1].child)
        apple = generate_apple(snake, num_cells_x, num_cells_y)
    
    timer += 1
    for cell in snake:
        cell.draw(sc)
    apple.draw(sc)
    pygame.display.update()
    pygame.time.delay(10)