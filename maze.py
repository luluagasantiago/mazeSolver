from window import *
import time
import random

class Maze():
    
    def __init__(self,
                x1,
                y1,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win = None,
                seed = None
    ):
    # x1,y1 is the starting poing to draw the cells
        self.x1 = x1
        self.y1 = y1 
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._cells = [[None for x in range(self.num_cols)] for y in range(self.num_rows)]
        if seed:
            self.seed = random.seed(seed)
        else:
            self.seed = random.seed(0)
    def _create_cells(self):
        # fill self._cells, each list is a column of Cell objects

        # how many cells do we need to creat?
        # rows * column
        # get middle of window
        self.win.canvas.update()
        width = self.win.canvas.winfo_width()
        height = self.win.canvas.winfo_height()
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                x1 = self.x1 + j * self.cell_size_x
                x2 = x1 + self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                y2 = y1 + self.cell_size_y
                self._cells[i][j] = Cell(x1, x2, y1, y2, self.win)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
    
    def _animate(self):
       self.win.redraw()
       time.sleep(0.05)
    
    def break_entrance_and_exit(self):
        i = len(self._cells) - 1
        j = len(self._cells[0]) - 1
        
        self._cells[0][0].has_bottom_wall = False
        self._draw_cell(0,0)
        self._cells[i][j].has_top_wall = False 
        self._draw_cell(i,j)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True 
        while True: 
            to_visit = []
            if i + 1 < self.num_rows:
                if not self._cells[i+1][j].visited: 
                    to_visit.append((i+1,j))
            if i - 1 > 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))

            if j + 1 < self.num_cols:
                if not self._cells[i][j+1].visited: 
                    to_visit.append((i, j+1))
            if j - 1 > 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = to_visit[random.randint(0, len(to_visit)-1)]            # if in different row
            if direction[0] != i:
                if i > direction[0]:
                    self._cells[i][j].has_bottom_wall = False
                else:
                    self._cells[i][j].has_top_wall = False
            else:
                if j > direction[1]:
                    self._cells[i][j].has_left_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
            
            self._draw_cell(i,j)  
            self._break_walls_r(direction[0], direction[1])

  

def main():
    win = Window(800, 600)
    m = Maze(100,100, 10, 10, 50, 50,win )
    m._create_cells()
    for i in range(10):
        for j in range(10):
            m._draw_cell(i,j)
    m.break_entrance_and_exit()
    m._break_walls_r(0,0)
    win.wait_for_close()
if __name__ == "__main__":
    main()





