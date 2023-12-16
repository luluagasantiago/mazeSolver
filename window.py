
from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("This is a title")
        self.canvas = Canvas(self.__root, width = width, height = height)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
        

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y, 
            fill = fill_color, width=2
            )
        canvas.pack()


class Cell():

    def __init__(self,x1, x2, y1, y2, window = None , color="red"):
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2 
        self._win = window
        self.color = color
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw(self):
        upper_left = Point(self._x1, self._y1)
        upper_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        left = Line(bottom_left, upper_left)
        BACKGROUND = "black"  
        if self.has_left_wall:
            self._win.draw_line(left, self.color)
        else:
            self._win.draw_line(left, BACKGROUND)
                  
        right = Line(bottom_right, upper_right)
        if self.has_right_wall:
            self._win.draw_line(right, self.color)
        else:
            self._win.draw_line(right, BACKGROUND)
        
        bottom = Line(bottom_left, bottom_right)
        if self.has_bottom_wall:
            self._win.draw_line(bottom, self.color)
        else:
            self._win.draw_line(bottom, BACKGROUND)
        
        top = Line(upper_right, upper_left)
        if self.has_top_wall:
           self._win.draw_line(top, self.color)
        else:
           self._win.draw_line(top, BACKGROUND)

    def draw_move(self, to_cell, undo = False):
        p_start = Point((self._x1 + self._x2) // 2,
        (self._y1 + self._y2) // 2)

        p_end = Point((to_cell._x1  + to_cell._x2) // 2,
        (to_cell._y1 + to_cell._y2) // 2)
        l1 = Line(p_start, p_end)
        
        if undo:
            self._win.draw_line(l1, "gray")
        else:
            self._win.draw_line(l1, "red")



def main():
    win = Window(800, 600)
    win.canvas.update()
    p1 = Point(win.canvas.winfo_width() // 2, win.canvas.winfo_width() // 2)
    p2 = Point(0,0)
    l1 = Line(p2, p1)
    win.draw_line(l1, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()
