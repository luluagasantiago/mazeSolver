from window import *
import time
class Maze():
    
    def __init__(self,
                x1,
                y1,
                num_rows,
                num_cols,
                cell_size_x,
                cell_size_y,
                win
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
        self._create_cells()      
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


def main():
    win = Window(800, 600)
    m = Maze(100,100, 10, 10, 50, 50,win)
    for i in range(10):
        for j in range(10):
            m._draw_cell(i,j)
    win.wait_for_close()
if __name__ == "__main__":
    main()





