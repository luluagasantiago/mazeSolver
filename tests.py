import unittest

from maze import Maze
from window import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
    def test_maze_break_entrance_and_exit(self):
        win = Window(100,100)
        m1 = Maze(0,0,10, 10 , 10, 10, win)
        m1._create_cells()
        m1.break_entrance_and_exit()
        i = len(m1._cells) - 1
        j = len(m1._cells[0]) - 1 
        
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[i][j].has_bottom_wall, False)
        
    def test_reset_cells(self):
        win = Window(100,100)
        m1 = Maze(0,0,10,10,10,10, win)
        m1._create_cells()
        for row in m1._cells:
            for cell in row:
                cell.visited = True
        m1._reset_cells_visited()
        for row in m1._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)

if __name__ == "__main__":
    unittest.main()

 
