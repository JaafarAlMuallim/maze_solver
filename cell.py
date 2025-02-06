from line import Line
from point import Point
from window import Window


class Cell:
    def __init__(
        self,
        point1: Point,
        point2: Point,
        visited: bool = False,
        window: Window | None = None,
    ):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = visited
        self._x1 = point1.x
        self._y1 = point1.y
        self._x2 = point2.x
        self._y2 = point2.y
        self._win = window

    def draw(self):
        """
        Draw A Cell Depending on Wall Existance
        """
        if self._win is None:
            return
        fill = "white"
        nofill = "#323232"
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, fill if self.has_left_wall else nofill)
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, fill if self.has_top_wall else nofill)
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, fill if self.has_right_wall else nofill)
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, fill if self.has_bottom_wall else nofill)

    def get_point1(self):
        """
        Get Point 1
        """
        return Point(self._x1, self._y1)

    def get_point2(self):
        """
        Get Point 2
        """
        return Point(self._x2, self._y2)

    def mid_point(self):
        """
        Get Mid Point
        """
        mid_x = abs(self._x2 - self._x1) // 2
        mid_y = abs(self._y2 - self._y1) // 2
        return Point(mid_x + self._x1, mid_y + self._y1)

    def draw_move(self, to_cell, undo=False):
        """
        Track Path Between Two Cells
        """
        if self._win is None:
            return
        mid = self.mid_point()
        mid_to_cell = to_cell.mid_point()
        line = Line(mid, mid_to_cell)
        color = "red" if undo else "gray"
        line = Line(mid, mid_to_cell)
        self._win.draw_line(line, color)
