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

    #   x1,y1 is the starting poing to draw the cells
        self.x1 = x1
        self.y1 = y1 
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._cells = [[None for x in range(self.num_cols)] for y in range(self.num_rows)]
        if seed:
            random.seed(seed)
   
            
    

    def _create_cells(self):
        # fill self._cells, each list is a column of Cell objects

        # rows * columns
        self.win.canvas.update() # update to get the actuall values of widget canvas
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
       time.sleep(0.005)

    
    def break_entrance_and_exit(self):
        # end is always 
        #self._cells[len(number_rows][number_columns]
        i = self.num_rows - 1
        j = self.num_cols - 1
        
        self.open_top(0,0)
        self.open_bottom(i,j)
    count = 0    
    def _break_walls_r(self, i, j, count=0):
        self._cells[i][j].visited = True 
        while True: 
            to_visit = []
            self._animate()
            to_visit = self.get_unvisited_directions(i,j)
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            direction = to_visit[random.randint(0, len(to_visit)-1)]            # if in different row
            if direction[0] != i:
                if i > direction[0]:
                    self.open_top(i,j)
                else:
                    self.open_bottom(i,j)
            else:
                if j > direction[1]:
                    self.open_left(i,j)
                else:
                    self.open_right(i, j)
           
            self._break_walls_r(direction[0], direction[1])
       
    
    def open_top(self, i, j):
        self._cells[i][j].has_top_wall = False
        # have to open floor of above cell (double wall)
        if i > 0:
            self._cells[i-1][j].has_bottom_wall = False
        self._draw_cell(i,j)

    def open_bottom(self, i, j):
        self._cells[i][j].has_bottom_wall = False
        if i < self.num_rows - 1:
            self._cells[i+1][j].has_top_wall = False
        self._draw_cell(i,j)


    
    def open_left(self, i, j):
        self._cells[i][j].has_left_wall = False
        
        if j > 0:
            self._cells[i][j - 1].has_right_wall = False
        self._draw_cell(i, j)
   
    
    def open_right(self, i, j):
        self._cells[i][j].has_right_wall = False
        if j < self.num_cols - 1:
            self._cells[i][j + 1].has_left_wall = False
        self._draw_cell(i,j)


    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def get_unvisited_directions(self, i, j):
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
        return to_visit 

    def without_wall(self,i, j, possible_directions):
        # return directions without wall in between
        # cell 0 and cell 1
        ## same row ?
        #open
        directions_without_wall = []
        for direction in possible_directions:
            i1 = direction[0]
            j1 = direction[1] 
            if i != i1:
                if i < i1:
                    if not self._cells[i][j].has_bottom_wall:
                        directions_without_wall.append(direction)
                else:
                    if not self._cells[i][j].has_top_wall:
                        directions_without_wall.append(direction)
            if j != j1:
                if j < j1:
                    if not self._cells[i][j].has_right_wall:
                        directions_without_wall.append(direction)
                else:
                    if not self._cells[i][j].has_left_wall:
                        directions_without_wall.append(direction)


        return directions_without_wall            
                
            
            


    def solve(self, i = 0, j = 0):
        self._reset_cells_visited()
        return self._solve_r(i, j)
    
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        directions = self.get_unvisited_directions(i,j)
        directions = self.without_wall(i, j, directions)
        for direction in directions:
            i1 = direction[0]
            j1 = direction[1]
            self._cells[i][j].draw_move(self._cells[i1][j1])
            if self._solve_r(direction[0], direction[1]):
                return True
            self._cells[i1][j1].draw_move(self._cells[i][j], undo = True)
        return False
            


        
         

def main():
    win = Window(800, 600)
    m = Maze(100,100, 10, 10, 50, 50,win)
    m._create_cells()
    #for i in range(10):
    #    for j in range(10):
    #        m._draw_cell(i,j)
    m.break_entrance_and_exit()
    m._break_walls_r(0,0)
    if m.solve(5,5):
        print("FOUND THE  EXIT!")
    win.wait_for_close()


if __name__ == "__main__":
    main()
