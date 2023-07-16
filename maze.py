import pygame as pg
import random


screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
cols = 0
rows = 0
block_size = 40
grid = []
start = True
current = None
stack = []




def setup():
    global current
    global cols
    global rows
    global grid
    cols = screen.get_width() // block_size
    rows = screen.get_height() // block_size
    screen.fill("white")


    for y in range(rows):
        for x in range(cols):
            cell = Cell(x, y)
            grid.append(cell)


    for cells in grid:
        cells.show()


    current = grid[0]




def draw():
    global current
    global next


    current.visited = True
    current.visit_color()
    grids = current.checkNeighbors()
    next = current.maze_usage(grids)
    if next != None and next not in stack:
        next.visited = True
        next.highlight()


        stack.append(current)
        removeWalls(current, next)
        current = next
    elif len(stack) > 0:
        current = stack.pop()
        current.highlight()


    for cells in grid:
        cells.show()




def index(i, j):
    if i < 0 or j < 0 or i > cols - 1 or j > rows - 1:
        return None
    return i + j * cols




def return_cell(position):
    try:
        return grid[position]
    except:
        return -1




def removeWalls(a, b):
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False
    a.show()
    b.show()




class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.walls = [True, True, True, True]
        self.visited = False
        self.f = 0
        self.g = 0
        self.h = 0
        self.index = index(self.i, self.j)
        self.previous = None


    def show(self):
        x = self.i * block_size
        y = self.j * block_size
        if self.walls[0]:
            pg.draw.line(screen, "black", (x, y), (x + block_size, y), 1)
        if self.walls[1]:
            pg.draw.line(
                screen,
                "black",
                (x + block_size, y),
                (x + block_size, y + block_size),
                1,
            )
        if self.walls[2]:
            pg.draw.line(
                screen,
                "black",
                (x + block_size, y + block_size),
                (x, y + block_size),
                1,
            )
        if self.walls[3]:
            pg.draw.line(screen, "black", (x, y + block_size), (x, y), 1)


    def visit_color(self):
        if self.visited:
            pg.draw.rect(
                screen,
                "white",
                (self.i * block_size, self.j * block_size, block_size, block_size),
                0,
            )


    def highlight(self):
        if self.visited:
            pg.draw.rect(
                screen,
                "green",
                (self.i * block_size, self.j * block_size, block_size, block_size),
                0,
            )


    def checkNeighbors(self) -> list:
        i = self.i
        j = self.j
        neighbors = []
        top = None
        right = None
        bottom = None
        left = None
        top = return_cell(index(i, j - 1))
        right = return_cell(index(i + 1, j))
        bottom = return_cell(index(i, j + 1))
        left = return_cell(index(i - 1, j))


        if top != -1 and not top.visited:
            neighbors.append(top)
        if right != -1 and not right.visited:
            neighbors.append(right)
        if bottom != -1 and not bottom.visited:
            neighbors.append(bottom)
        if left != -1 and not left.visited:
            neighbors.append(left)
        return neighbors
   
    def valid_neighbors(self):
        i = self.i
        j = self.j
        neighbors = []
        top = return_cell(index(i, j - 1))
        right = return_cell(index(i + 1, j))
        bottom = return_cell(index(i, j + 1))
        left = return_cell(index(i - 1, j))
        if top != -1 and not self.walls[0]:
            neighbors.append(top)
        else:
            neighbors.append(top)
        if right != -1 and not self.walls[0]:
            neighbors.append(right)
        else:
            neighbors.append(right)
        if bottom != -1 and not self.walls[0]:
            neighbors.append(bottom)
        else:
            neighbors.append(bottom)
        if left != -1 and not self.walls[0]:
            neighbors.append(left)
        else:
            neighbors.append(left)
        return neighbors


    def maze_usage(self, neighbors):
        for _ in range(len(neighbors)):
            r = random.randint(0, len(neighbors) - 1)
            if len(neighbors) != 0 and neighbors[r] != -1:
                return neighbors[r]
        return None


    def algorithm_usage(self, neighbors):
        return neighbors




def total_grid():
    global running
    global start
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        if start:
            setup()
            start = False


        draw()
        clock.tick(120)
        pg.display.flip()
       
        if current == grid[0] and not start:
            return grid
           
       
if __name__ == "__main__":
    total_grid()