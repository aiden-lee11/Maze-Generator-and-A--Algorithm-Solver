import pygame as pg
import maze


screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()
running = True
cols = 0
rows = 0
block_size = 40
grid = maze.total_grid()
openList, closedList, path = [], [], []
start = grid[len(grid) - 1]
end = grid[0]
openList.append(start)
finished = False


def draw_sets():
    for op in openList:
        pg.draw.rect(
                screen,
                "green",
                (op.i * block_size, op.j * block_size, block_size + 1, block_size + 1),
                0,
            )
   
    for closed in closedList:
        pg.draw.rect(
                screen,
                "red",
                (closed.i * block_size, closed.j * block_size, block_size + 1, block_size + 1),
                0,
            )
        
    for best in path:
        pg.draw.rect(
                screen,
                "purple",
                (best.i * block_size, best.j * block_size, block_size, block_size),
                0,
            )
    if path != [] and not finished:
        pg.draw.rect(
                screen,
                "white",
                (end.i * block_size, end.j * block_size, block_size + 1, block_size + 1),
                0,
            )
            
    # for best in path:
    #     x = best.i * block_size 
    #     y = best.j * block_size
    #     pg.draw.rect(
    #         screen,
    #         "gold",
    #         True,
    #         ((x // 2, y), (endx , endy))
    #     )

    for cells in grid:
        cells.show()

def lists():
    global openList
    global closedList
    global current
    global path
    global finished
    if not finished:
        if len(openList) > 0:
            lowestIndex = 0
            i = 0
            for cell in openList:
                if cell.f < openList[lowestIndex].f:
                    lowestIndex = i
                i += 1
            current = openList[lowestIndex]
            if current == end:
                temp = current
                path.append(temp)
                while temp.previous != None:
                    path.append(temp.previous)
                    temp = temp.previous
                print("DONE!")
                finished = True
            openList.remove(current)
            closedList.append(current)
        else:
            print("No Solution")
            finished = True
def values():
    global openList
    global closedList
    global current
    global path
    global finished
    if not finished:
        walls = current.walls
        neighbors = current.valid_neighbors()
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if not neighbors[i] in closedList and not walls[i]:
                neighbor = neighbors[i]
                tempG = current.g + 1
                if neighbor in openList:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openList.append(neighbors[i])
                neighbor.h = heuristic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous = current
            
def heuristic(curr, end):
    return pg.math.Vector2(curr.i, curr.j).distance_to((end.i, end.j))
   
       
def main():
    global running
    global finished
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        if not finished:
            lists()
            values()
            draw_sets()
            clock.tick(90)
            pg.display.flip()
        
        else:
            for cells in grid:
                cells.show()
            pg.display.flip()


if __name__ == "__main__":
    main()





